"""Genera combinaciones de: lunfardo + anios."""
from nucleo_wordlist import generar

ARCHIVOS = [
    "vocabulario/lunfardo.txt",
    "cosas/fechas_anios_argentina.txt",
]
ARCHIVO_SALIDA = "wordlist_lunfardo_anios.txt"

if __name__ == "__main__":
    generar(ARCHIVOS, ARCHIVO_SALIDA)
