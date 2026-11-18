"""Genera combinaciones de: verbos + sustantivos."""
from nucleo_wordlist import generar

ARCHIVOS = [
    "vocabulario/verbos_argentinos.txt",
    "vocabulario/sustantivos.txt",
]
ARCHIVO_SALIDA = "wordlist_verbos_sustantivos.txt"

if __name__ == "__main__":
    generar(ARCHIVOS, ARCHIVO_SALIDA)
