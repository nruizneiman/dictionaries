"""Genera combinaciones de: vehiculos/modelos + anios."""
from nucleo_wordlist import generar

ARCHIVOS = [
    "cosas/vehiculos_modelos.txt",
    "cosas/fechas_anios_argentina.txt",
]
ARCHIVO_SALIDA = "wordlist_vehiculos_anios.txt"

if __name__ == "__main__":
    generar(ARCHIVOS, ARCHIVO_SALIDA)
