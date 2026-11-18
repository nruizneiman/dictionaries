# Diccionarios de Argentina

Colección de listas de palabras sobre Argentina, en archivos `.txt` de texto plano: un valor por línea, codificación UTF-8, sin valores repetidos (se compara sin distinguir mayúsculas ni tildes).

## Estructura

| Carpeta | Archivo | Entradas | Origen |
|---|---|---:|---|
| `personas/` | `nombres.txt` | 14.920 | RENAPER, ordenado por frecuencia (2012–2024) |
| | `apellidos.txt` | 135.986 | RENAPER, ordenado por frecuencia (diciembre 2021) |
| | `famosos_y_artistas.txt` | 6.040 | Wikidata, ordenado por relevancia |
| | `escritores_argentinos.txt` | 1.078 | Wikidata, ordenado por relevancia |
| | `profesiones_oficios.txt` | 656 | Memoria |
| | `bandas_artistas.txt` | 275 | Memoria |
| | `apodos.txt` | 245 | Memoria |
| | `personajes_historicos.txt` | 215 | Memoria |
| | `futbolistas_tecnicos.txt` | 125 | Memoria |
| `lugares/` | `calles.txt` | 81.367 | API Georef (datos.gob.ar) |
| | `lugares_argentina.txt` | 4.022 | API Georef: provincias, departamentos, municipios, localidades |
| | `estaciones_trenes_subte.txt` | 2.544 | Wikidata |
| | `rios_lagos_montanas.txt` | 377 | Memoria |
| | `aeropuertos_aerodromos.txt` | 204 | Wikidata |
| | `barrios.txt` | 92 | Memoria |
| `organizaciones/` | `empresas.txt` | 875.249 | Registro Nacional de Sociedades (2026), más 559 empresas conocidas al inicio |
| | `escuelas.txt` | 54.093 | Padrón Oficial de Establecimientos Educativos (2026) |
| | `marcas.txt` | 936 | Memoria |
| | `hospitales_sanatorios.txt` | 185 | Memoria |
| | `partidos_politicos.txt` | 189 | Wikidata |
| | `bancos_financieras.txt` | 142 | Memoria |
| | `clubes_futbol.txt` | 124 | Memoria |
| | `universidades_institutos.txt` | 119 | Memoria |
| | `organismos_publicos.txt` | 107 | Wikidata |
| `cultura/` | `peliculas_argentinas.txt` | 3.346 | Wikidata, ordenado por relevancia |
| | `series_argentinas.txt` | 810 | Wikidata, ordenado por relevancia |
| | `libros_argentinos.txt` | 193 | Wikidata, ordenado por relevancia |
| | `tv_y_radio.txt` | 138 | Memoria |
| | `canciones_argentinas.txt` | 85 | Memoria |
| `vocabulario/` | `adjetivos_argentinos.txt` | 995 | Memoria |
| | `verbos_argentinos.txt` | 547 | Memoria |
| | `sustantivos.txt` | 517 | Memoria |
| | `lunfardo.txt` | 259 | Memoria |
| | `frases_refranes.txt` | 103 | Memoria |
| `naturaleza/` | `mascotas.txt` | 570 | Memoria |
| | `animales.txt` | 274 | Memoria |
| | `plantas.txt` | 244 | Memoria |
| `cosas/` | `vehiculos_modelos.txt` | 418 | Memoria |
| | `medicamentos.txt` | 346 | Memoria y vademécum nacional |
| | `alimentos_cultivos_cortes.txt` | 342 | Memoria |
| | `siglas.txt` | 339 | Memoria |
| | `fechas_anios_argentina.txt` | 323 | Memoria |
| | `carreras_universitarias.txt` | 278 | Memoria y datos de educación superior |
| | `deportes.txt` | 248 | Memoria |
| | `colores.txt` | 245 | Memoria |
| | `comidas.txt` | 441 | Memoria |
| | `instrumentos_musicales.txt` | 128 | Memoria |

## Orden de las listas

- `nombres.txt`, `apellidos.txt`: de más a menos frecuente. Los nombres suman 2012–2024, incluidos los que ya no aparecen en el último año.
- Listas de Wikidata: de más a menos relevante (cantidad de idiomas con artículo en Wikipedia).
- `empresas.txt`: primero las conocidas, después las del registro en orden alfabético (en mayúsculas, sin forma legal).
- El resto: sin orden de frecuencia (alfabético o aproximado por popularidad).

## Fuentes y confiabilidad

**Datos oficiales o abiertos**
- RENAPER, datos abiertos: nombres propios y apellidos.
- API Georef, datos.gob.ar: calles y lugares.
- Registro Nacional de Sociedades, datos.jus.gob.ar: empresas.
- Padrón Oficial de Establecimientos Educativos: escuelas.
- Wikidata: famosos, escritores, películas, series, libros, estaciones, aeropuertos, partidos y organismos.

**De memoria:** las listas marcadas como "Memoria" las escribió el asistente sin contrastarlas con una fuente. No son exhaustivas y pueden tener errores de escritura o entradas dudosas. Las más confiables son animales, plantas, instrumentos, deportes, vehículos y medicamentos; las menos, TV y radio, canciones y bancos.

## Limitaciones conocidas

- `empresas.txt` conserva el ruido del registro: nombres de personas, sociedades de dos socios y marcas muy chicas.
- Las calles incluyen numeradas (por ejemplo, "ALAMEDA 207") y los apellidos vienen sin tildes, como en la fuente.
- Los datos de `nombres.txt` no incluyen años anteriores a 2012 (RENAPER no los publica abiertos).
- `famosos_y_artistas.txt` mezcla personas actuales e históricas, y artistas con deportistas, políticos y empresarios.
- La lista de discos argentinos se descartó por falta de datos confiables.

## Otros archivos

- `alfanum.py`: genera variantes alfanuméricas (palabra + sufijo numérico) a partir de las palabras más comunes del español y nombres/apellidos de Faker.
- `pin.txt`: 100.000.000 de PINs numéricos de 8 dígitos (`00000000`–`99999999`), uno por línea.

## Carpeta `generadores/`

Scripts que combinan líneas de dos o tres de las listas anteriores para armar wordlists de contraseñas (por ejemplo `nombres.txt` + `apellidos.txt` + `fechas_anios_argentina.txt` → `JuanPerez1990`). Cada combinación resultante se filtra para quedarse solo con los largos de 8 a 10 caracteres, sin tildes ni espacios.

Convención de nombres:
- Script: `generar_<categoria1>_<categoria2>[_<categoria3>].py`
- Salida: `wordlist_<categoria1>_<categoria2>[_<categoria3>].txt` (se escribe siempre en la raíz del proyecto, sin importar desde dónde se ejecute el script)

La lógica común (limpieza de texto, armado de combinaciones, resolución de rutas) vive en `nucleo_wordlist.py`; cada `generar_*.py` solo declara sus archivos de entrada y de salida.

### Quick start

```bash
git clone https://github.com/nruizneiman/dictionaries.git
cd dictionaries
python generadores/generar_mascotas_anios.py
```

Salida esperada:

```
naturaleza/mascotas.txt: 570 palabras unicas
cosas/fechas_anios_argentina.txt: 321 palabras unicas
TOTAL: 168,111 lineas en 'wordlist_mascotas_anios.txt' (0.0s)
```

El archivo generado (`wordlist_mascotas_anios.txt`) queda en la raíz del repo y no se versiona (ver `.gitignore`). Funciona igual si lo corrés desde la raíz del repo o desde adentro de `generadores/`.
