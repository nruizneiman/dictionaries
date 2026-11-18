"""Genera combinaciones de: profesiones/oficios + anios."""
from nucleo_wordlist import generar

ARCHIVOS = [
    "personas/profesiones_oficios.txt",
    "cosas/fechas_anios_argentina.txt",
]
ARCHIVO_SALIDA = "wordlist_profesiones_anios.txt"

if __name__ == "__main__":
    generar(ARCHIVOS, ARCHIVO_SALIDA)
