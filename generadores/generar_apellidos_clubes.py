"""Genera combinaciones de: apellidos + clubes de futbol."""
from nucleo_wordlist import generar

ARCHIVOS = [
    "personas/apellidos.txt",
    "organizaciones/clubes_futbol.txt",
]
ARCHIVO_SALIDA = "wordlist_apellidos_clubes.txt"

if __name__ == "__main__":
    generar(ARCHIVOS, ARCHIVO_SALIDA)
