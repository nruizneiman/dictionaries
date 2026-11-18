"""Genera combinaciones de: apodos + anios."""
from nucleo_wordlist import generar

ARCHIVOS = [
    "personas/apodos.txt",
    "cosas/fechas_anios_argentina.txt",
]
ARCHIVO_SALIDA = "wordlist_apodos_anios.txt"

if __name__ == "__main__":
    generar(ARCHIVOS, ARCHIVO_SALIDA)
