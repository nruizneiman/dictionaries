"""Genera combinaciones de: mascotas + anios."""
from nucleo_wordlist import generar

ARCHIVOS = [
    "naturaleza/mascotas.txt",
    "cosas/fechas_anios_argentina.txt",
]
ARCHIVO_SALIDA = "wordlist_mascotas_anios.txt"

if __name__ == "__main__":
    generar(ARCHIVOS, ARCHIVO_SALIDA)
