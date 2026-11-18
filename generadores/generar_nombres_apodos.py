"""Genera combinaciones de: nombres + apodos."""
from nucleo_wordlist import generar

ARCHIVOS = [
    "personas/nombres.txt",
    "personas/apodos.txt",
]
ARCHIVO_SALIDA = "wordlist_nombres_apodos.txt"

if __name__ == "__main__":
    generar(ARCHIVOS, ARCHIVO_SALIDA)
