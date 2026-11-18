"""
Modulo compartido para los scripts generar_<categoria1>_<categoria2>[_<categoria3>].py

Convencion del proyecto:
  - Script:  generar_<cat1>_<cat2>[_<cat3>].py
  - Salida:  wordlist_<cat1>_<cat2>[_<cat3>].txt
  - El orden de las categorias en el nombre = orden de concatenacion en ARCHIVOS.

Cada script "generar_*.py" solo define ARCHIVOS y ARCHIVO_SALIDA (y opcionalmente
LARGO_MIN/LARGO_MAX) y llama a generar(...) de este modulo.
"""

import itertools
import time
import unicodedata
from pathlib import Path

LARGO_MIN_DEFAULT = 8
LARGO_MAX_DEFAULT = 10

# Raiz del proyecto = carpeta que contiene a "generadores/" (donde vive este
# archivo). Las rutas de ARCHIVOS y ARCHIVO_SALIDA de cada script se escriben
# relativas a esa raiz (ej. "personas/nombres.txt"), y se resuelven aqui para
# que funcionen sin importar desde donde se ejecute python (la raiz del
# proyecto, dentro de generadores/, etc).
RAIZ = Path(__file__).resolve().parent.parent


def _resolver(ruta):
    p = Path(ruta)
    return p if p.is_absolute() else RAIZ / p


def limpiar(texto):
    """Quita espacios, tildes y cualquier caracter que no sea alfanumerico."""
    texto = texto.strip()
    texto_norm = unicodedata.normalize("NFD", texto)
    sin_tildes = "".join(c for c in texto_norm if unicodedata.category(c) != "Mn")
    return "".join(c for c in sin_tildes if c.isalnum())


def cargar_buckets(ruta):
    """Devuelve dict: largo -> lista de palabras unicas de ese largo (ya limpias)."""
    vistas = set()
    buckets = {}
    with open(_resolver(ruta), "r", encoding="utf-8") as f:
        for linea in f:
            palabra = limpiar(linea)
            if not palabra or palabra in vistas:
                continue
            vistas.add(palabra)
            buckets.setdefault(len(palabra), []).append(palabra)
    return buckets


def generar(archivos, archivo_salida, largo_min=LARGO_MIN_DEFAULT,
            largo_max=LARGO_MAX_DEFAULT, reportar_cada=20_000_000):
    """
    Combina las lineas completas (sin truncar) de `archivos` en todos los
    ordenes y subconjuntos posibles (1..N archivos), filtrando por largo
    total entre largo_min y largo_max, y escribe el resultado en
    `archivo_salida`.
    """
    buckets_por_archivo = [cargar_buckets(a) for a in archivos]
    for ruta, buckets in zip(archivos, buckets_por_archivo):
        total = sum(len(v) for v in buckets.values())
        print(f"{ruta}: {total} palabras unicas")

    n = len(buckets_por_archivo)
    inicio = time.time()
    escritas = 0
    ultimo_reporte = 0

    with open(_resolver(archivo_salida), "w", encoding="utf-8", buffering=1024 * 1024) as salida:
        for cantidad in range(1, n + 1):
            for combo_indices in itertools.permutations(range(n), cantidad):
                buckets_elegidos = [buckets_por_archivo[i] for i in combo_indices]
                largos_posibles = [sorted(b.keys()) for b in buckets_elegidos]

                for combo_largos in itertools.product(*largos_posibles):
                    suma = sum(combo_largos)
                    if suma < largo_min or suma > largo_max:
                        continue
                    listas_palabras = [
                        buckets_elegidos[idx][largo]
                        for idx, largo in enumerate(combo_largos)
                    ]
                    buffer_lineas = []
                    for combinacion in itertools.product(*listas_palabras):
                        buffer_lineas.append("".join(combinacion))
                        if len(buffer_lineas) >= 100_000:
                            salida.write("\n".join(buffer_lineas) + "\n")
                            escritas += len(buffer_lineas)
                            buffer_lineas.clear()
                    if buffer_lineas:
                        salida.write("\n".join(buffer_lineas) + "\n")
                        escritas += len(buffer_lineas)

                    if escritas - ultimo_reporte >= reportar_cada:
                        ultimo_reporte = escritas
                        transcurrido = time.time() - inicio
                        print(f"{escritas:,} lineas escritas en {transcurrido:.1f}s "
                              f"({escritas/transcurrido:,.0f} lineas/s)", flush=True)

    transcurrido = time.time() - inicio
    print(f"TOTAL: {escritas:,} lineas en '{archivo_salida}' ({transcurrido:.1f}s)")
    return escritas
