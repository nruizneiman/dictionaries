# Contribuir

Gracias por tu interés en mejorar este repositorio. Hay dos tipos de contribución: agregar o corregir entradas en las listas, y agregar o mejorar generadores de wordlists.

## Agregar o corregir entradas en una lista (`.txt`)

- Un valor por línea, codificación UTF-8, sin líneas vacías.
- No dupliques entradas que ya existan ignorando mayúsculas y tildes (por ejemplo, si ya está `Perón`, no agregues `peron`).
- Si agregás una lista nueva, decidí en qué carpeta temática entra (`personas/`, `lugares/`, `organizaciones/`, `cultura/`, `vocabulario/`, `naturaleza/`, `cosas/`) o proponé una carpeta nueva si no encaja en ninguna.
- En el pull request, indicá la fuente de los datos (dataset abierto, Wikidata, memoria propia, etc.) y si tiene algún orden (frecuencia, relevancia, alfabético). Esa información se refleja después en la tabla del `README.md`.
- Evitá cargar datos personales identificables que no vengan de una fuente abierta/pública ya agregada (no subas, por ejemplo, listas de clientes, contactos de tu agenda, etc.).

## Agregar un generador en `generadores/`

Los scripts de esa carpeta combinan líneas de dos o tres listas para armar wordlists de contraseñas, filtrando por largo final. Si agregás una combinación nueva:

- Nombrá el script `generar_<categoria1>_<categoria2>[_<categoria3>].py`, y la salida que produce `wordlist_<categoria1>_<categoria2>[_<categoria3>].txt`.
- Reutilizá `nucleo_wordlist.py` (la función `generar()`) en vez de reimplementar la lógica de combinación o limpieza de texto.
- El script solo debería declarar `ARCHIVOS` (rutas relativas a la raíz del repo) y `ARCHIVO_SALIDA` (solo el nombre de archivo, sin ruta), y llamar a `generar(ARCHIVOS, ARCHIVO_SALIDA)`.
- No hace falta indicar una carpeta de salida: `generar()` escribe siempre en `output/` (la crea si no existe), sin importar desde dónde se ejecute el script.
- No subas los `.txt` generados (pueden pesar varios GB); la carpeta `output/` ya está en `.gitignore`.

## Pull requests

- Un PR por tema (una lista nueva, una corrección, un generador nuevo) para que sea fácil de revisar.
- Si corregís una entrada existente, mencioná por qué (dato erróneo, duplicado, mal categorizado).

## Uso responsable

Este repositorio existe para pruebas de seguridad propias o autorizadas (auditoría de contraseñas, pentesting con permiso). No se aceptan contribuciones pensadas para facilitar ataques contra terceros sin autorización.
