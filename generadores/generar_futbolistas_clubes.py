"""Genera combinaciones de: futbolistas/tecnicos + clubes de futbol."""
from nucleo_wordlist import generar

ARCHIVOS = [
    "personas/futbolistas_tecnicos.txt",
    "organizaciones/clubes_futbol.txt",
]
ARCHIVO_SALIDA = "wordlist_futbolistas_clubes.txt"

if __name__ == "__main__":
    generar(ARCHIVOS, ARCHIVO_SALIDA)
