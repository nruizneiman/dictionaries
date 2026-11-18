"""Genera combinaciones de: nombres + apellidos + anios."""
from nucleo_wordlist import generar

ARCHIVOS = [
    "personas/nombres.txt",
    "personas/apellidos.txt",
    "cosas/fechas_anios_argentina.txt",
]
ARCHIVO_SALIDA = "wordlist_nombres_apellidos_anios.txt"

if __name__ == "__main__":
    generar(ARCHIVOS, ARCHIVO_SALIDA)
