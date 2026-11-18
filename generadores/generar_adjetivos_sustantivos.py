"""Genera combinaciones de: adjetivos + sustantivos."""
from nucleo_wordlist import generar

ARCHIVOS = [
    "vocabulario/adjetivos_argentinos.txt",
    "vocabulario/sustantivos.txt",
]
ARCHIVO_SALIDA = "wordlist_adjetivos_sustantivos.txt"

if __name__ == "__main__":
    generar(ARCHIVOS, ARCHIVO_SALIDA)
