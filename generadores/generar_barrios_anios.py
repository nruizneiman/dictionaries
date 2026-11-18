"""Genera combinaciones de: barrios + anios."""
from nucleo_wordlist import generar

ARCHIVOS = [
    "lugares/barrios.txt",
    "cosas/fechas_anios_argentina.txt",
]
ARCHIVO_SALIDA = "wordlist_barrios_anios.txt"

if __name__ == "__main__":
    generar(ARCHIVOS, ARCHIVO_SALIDA)
