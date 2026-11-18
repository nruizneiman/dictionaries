"""
Valida las listas .txt del repo (no las wordlists generadas, que no se versionan).

Chequea por cada archivo:
  - Que sea UTF-8 valido.
  - Que no tenga lineas vacias.
  - Que no tenga duplicados ignorando mayusculas y tildes.

Uso: python validar_listas.py
Sale con codigo 1 si encuentra algun problema (pensado para correr en CI).
"""

import sys
import unicodedata
from pathlib import Path

CARPETAS = [
    "personas", "lugares", "organizaciones", "cultura",
    "vocabulario", "naturaleza", "cosas",
]


def normalizar(texto):
    """minusculas + sin tildes, para comparar duplicados."""
    texto = texto.strip().lower()
    texto_norm = unicodedata.normalize("NFD", texto)
    return "".join(c for c in texto_norm if unicodedata.category(c) != "Mn")


def validar_archivo(ruta):
    problemas = []
    try:
        contenido = ruta.read_text(encoding="utf-8")
    except UnicodeDecodeError as e:
        return [f"no es UTF-8 valido: {e}"]

    vistos = {}
    for num_linea, linea in enumerate(contenido.splitlines(), start=1):
        if linea.strip() == "":
            problemas.append(f"linea {num_linea} vacia")
            continue
        clave = normalizar(linea)
        if clave in vistos:
            problemas.append(
                f"linea {num_linea} ('{linea}') duplica a la linea "
                f"{vistos[clave]} ('{clave}' normalizado)"
            )
        else:
            vistos[clave] = num_linea

    return problemas


def main():
    raiz = Path(__file__).resolve().parent
    hubo_problemas = False

    for carpeta in CARPETAS:
        dir_carpeta = raiz / carpeta
        if not dir_carpeta.is_dir():
            continue
        for archivo in sorted(dir_carpeta.glob("*.txt")):
            problemas = validar_archivo(archivo)
            if problemas:
                hubo_problemas = True
                print(f"\n{archivo.relative_to(raiz)}: {len(problemas)} problema(s)")
                for p in problemas[:20]:
                    print(f"  - {p}")
                if len(problemas) > 20:
                    print(f"  ... y {len(problemas) - 20} mas")

    if hubo_problemas:
        print("\nValidacion FALLIDA.")
        sys.exit(1)
    else:
        print("Todas las listas pasaron la validacion.")


if __name__ == "__main__":
    main()
