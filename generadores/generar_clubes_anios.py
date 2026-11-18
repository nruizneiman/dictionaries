"""Genera combinaciones de: clubes de futbol + anios."""
from nucleo_wordlist import generar

ARCHIVOS = [
    "organizaciones/clubes_futbol.txt",
    "cosas/fechas_anios_argentina.txt",
]
ARCHIVO_SALIDA = "wordlist_clubes_anios.txt"

if __name__ == "__main__":
    generar(ARCHIVOS, ARCHIVO_SALIDA)
