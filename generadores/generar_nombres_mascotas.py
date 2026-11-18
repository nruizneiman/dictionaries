"""Genera combinaciones de: nombres + mascotas."""
from nucleo_wordlist import generar

ARCHIVOS = [
    "personas/nombres.txt",
    "naturaleza/mascotas.txt",
]
ARCHIVO_SALIDA = "wordlist_nombres_mascotas.txt"

if __name__ == "__main__":
    generar(ARCHIVOS, ARCHIVO_SALIDA)
