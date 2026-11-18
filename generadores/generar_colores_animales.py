"""Genera combinaciones de: colores + animales."""
from nucleo_wordlist import generar

ARCHIVOS = [
    "cosas/colores.txt",
    "naturaleza/animales.txt",
]
ARCHIVO_SALIDA = "wordlist_colores_animales.txt"

if __name__ == "__main__":
    generar(ARCHIVOS, ARCHIVO_SALIDA)
