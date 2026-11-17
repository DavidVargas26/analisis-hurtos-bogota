"""Carga y revisión inicial del archivo crudo de hurtos."""

from pathlib import Path

import pandas as pd


RUTA_PROYECTO = Path(__file__).resolve().parents[1]
RUTA_DATOS = RUTA_PROYECTO / "datos" / "crudo" / "HURTO_PERSONAS_20261117.csv"


def cargar_datos() -> pd.DataFrame:
    """Carga el archivo crudo sin modificarlo."""
    return pd.read_csv(
        RUTA_DATOS,
        dtype={
            "FECHA HECHO": "string",
            "COD_DEPTO": "string",
            "DEPARTAMENTO": "string",
            "COD_MUNI": "string",
            "MUNICIPIO": "string",
            "CANTIDAD": "string",
        },
    )


def reportar_calidad(datos: pd.DataFrame) -> None:
    """Reporta validaciones básicas y posibles problemas de calidad."""
    problemas: list[str] = []

    fecha = pd.to_datetime(datos["FECHA HECHO"], format="%d/%m/%Y", errors="coerce")
    cantidad = pd.to_numeric(datos["CANTIDAD"], errors="coerce")

    fechas_invalidas = fecha.isna() & datos["FECHA HECHO"].notna()
    cantidades_invalidas = cantidad.isna() & datos["CANTIDAD"].notna()
    cantidades_no_enteras = cantidad.notna() & (cantidad % 1 != 0)
    cantidades_no_positivas = cantidad.notna() & (cantidad <= 0)

    if datos.duplicated().sum():
        problemas.append(f"Hay {datos.duplicated().sum():,} filas duplicadas.")
    if fechas_invalidas.sum():
        problemas.append(
            f"Hay {fechas_invalidas.sum():,} fechas con formato inválido."
        )
    if cantidades_invalidas.sum():
        problemas.append(
            f"Hay {cantidades_invalidas.sum():,} cantidades no numéricas."
        )
    if cantidades_no_enteras.sum():
        problemas.append(
            f"Hay {cantidades_no_enteras.sum():,} cantidades no enteras."
        )
    if cantidades_no_positivas.sum():
        problemas.append(
            f"Hay {cantidades_no_positivas.sum():,} cantidades menores o iguales a cero."
        )

    for columna in datos.select_dtypes(include=["string", "object"]).columns:
        valores_con_espacios = datos[columna].dropna().str.strip().ne(
            datos[columna].dropna()
        )
        if valores_con_espacios.any():
            problemas.append(
                f"La columna '{columna}' contiene valores con espacios "
                "al inicio o al final."
            )

    print("\nPosibles problemas de calidad de datos:")
    if problemas:
        for problema in problemas:
            print(f"- {problema}")
    else:
        print("- No se encontraron problemas en las validaciones realizadas.")


def main() -> None:
    """Ejecuta el diagnóstico exploratorio inicial."""
    datos_crudos = cargar_datos()
    datos = datos_crudos.copy()
    datos["FECHA HECHO"] = pd.to_datetime(
        datos["FECHA HECHO"], format="%d/%m/%Y", errors="coerce"
    )
    datos["CANTIDAD"] = pd.to_numeric(
        datos["CANTIDAD"], errors="coerce"
    ).convert_dtypes()

    print(f"Archivo: {RUTA_DATOS}")
    print(f"\nNúmero de filas: {datos.shape[0]:,}")
    print(f"Número de columnas: {datos.shape[1]:,}")

    print("\nNombres exactos de las columnas:")
    for columna in datos.columns:
        print(f"- {columna!r}")

    print("\nTipos de datos:")
    print(datos.dtypes.to_string())

    print("\nPrimeras 5 filas:")
    print(datos.head(5).to_string(index=False))

    print("\nPorcentaje de valores nulos por columna:")
    porcentaje_nulos = datos_crudos.isna().mean().mul(100)
    print(porcentaje_nulos.map(lambda porcentaje: f"{porcentaje:.2f}%").to_string())

    reportar_calidad(datos_crudos)


if __name__ == "__main__":
    main()
