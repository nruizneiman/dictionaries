"""Genera combinaciones de: famosos y artistas + anios."""
from nucleo_wordlist import generar

ARCHIVOS = [
    "personas/famosos_y_artistas.txt",
    "cosas/fechas_anios_argentina.txt",
]
ARCHIVO_SALIDA = "wordlist_famosos_anios.txt"

if __name__ == "__main__":
    generar(ARCHIVOS, ARCHIVO_SALIDA)
