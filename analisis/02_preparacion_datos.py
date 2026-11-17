"""Prepara el archivo crudo para los análisis exploratorios."""

from pathlib import Path

import pandas as pd


RUTA_PROYECTO = Path(__file__).resolve().parents[1]
RUTA_DATOS_CRUDOS = (
    RUTA_PROYECTO / "datos" / "crudo" / "HURTO_PERSONAS_20261117.csv"
)
RUTA_DATOS_LIMPIOS = (
    RUTA_PROYECTO / "datos" / "limpio" / "hurto_personas_limpio.csv"
)

NOMBRES_MESES = {
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    12: "diciembre",
}

NOMBRES_DIAS_SEMANA = {
    0: "lunes",
    1: "martes",
    2: "miércoles",
    3: "jueves",
    4: "viernes",
    5: "sábado",
    6: "domingo",
}


def cargar_datos_crudos() -> pd.DataFrame:
    """Lee el archivo crudo sin modificarlo."""
    return pd.read_csv(
        RUTA_DATOS_CRUDOS,
        dtype={
            "FECHA HECHO": "string",
            "COD_DEPTO": "string",
            "DEPARTAMENTO": "string",
            "COD_MUNI": "string",
            "MUNICIPIO": "string",
            "CANTIDAD": "string",
        },
    )


def preparar_datos(datos: pd.DataFrame) -> pd.DataFrame:
    """Convierte la fecha y crea las variables temporales derivadas."""
    datos_preparados = datos.copy()
    fecha = pd.to_datetime(
        datos_preparados["FECHA HECHO"],
        format="%d/%m/%Y",
        errors="coerce",
    )

    fechas_invalidas = fecha.isna()
    if fechas_invalidas.any():
        cantidad_invalidas = int(fechas_invalidas.sum())
        raise ValueError(
            f"Se encontraron {cantidad_invalidas:,} fechas inválidas. "
            "No se generó el archivo limpio."
        )

    datos_preparados["FECHA HECHO"] = fecha
    datos_preparados["CANTIDAD"] = pd.to_numeric(
        datos_preparados["CANTIDAD"], errors="raise"
    )
    datos_preparados["año"] = fecha.dt.year
    datos_preparados["mes"] = fecha.dt.month
    datos_preparados["nombre_mes"] = fecha.dt.month.map(NOMBRES_MESES)
    datos_preparados["dia_semana"] = fecha.dt.day_of_week
    datos_preparados["nombre_dia_semana"] = fecha.dt.day_of_week.map(
        NOMBRES_DIAS_SEMANA
    )

    return datos_preparados


def main() -> None:
    """Lee, prepara y guarda los datos limpios."""
    datos_crudos = cargar_datos_crudos()
    datos_limpios = preparar_datos(datos_crudos)
    datos_limpios.to_csv(RUTA_DATOS_LIMPIOS, index=False, encoding="utf-8")

    print(f"Archivo limpio guardado en: {RUTA_DATOS_LIMPIOS}")
    print(f"Filas guardadas: {len(datos_limpios):,}")
    print(f"Columnas guardadas: {len(datos_limpios.columns):,}")


if __name__ == "__main__":
    main()
