"""Genera el ranking departamental de hurtos con Altair."""

from pathlib import Path

import altair as alt
import pandas as pd


RUTA_PROYECTO = Path(__file__).resolve().parents[1]
RUTA_DATOS = (
    RUTA_PROYECTO / "datos" / "limpio" / "hurto_personas_limpio.csv"
)
RUTA_GRAFICO = RUTA_PROYECTO / "docs" / "graficos" / "departamentos.html"


def cargar_y_agrupar_datos() -> pd.DataFrame:
    """Carga los datos y suma la cantidad de hurtos por departamento."""
    datos = pd.read_csv(
        RUTA_DATOS,
        usecols=["DEPARTAMENTO", "CANTIDAD"],
    )
    return (
        datos.groupby("DEPARTAMENTO", as_index=False)["CANTIDAD"]
        .sum()
        .rename(columns={"CANTIDAD": "cantidad_hurtos"})
        .sort_values("cantidad_hurtos", ascending=False)
    )


def crear_grafico(datos: pd.DataFrame) -> alt.Chart:
    """Crea el gráfico de barras horizontales por departamento."""
    return (
        alt.Chart(datos)
        .mark_bar()
        .encode(
            x=alt.X(
                "cantidad_hurtos:Q",
                title="Cantidad de hurtos",
            ),
            y=alt.Y(
                "DEPARTAMENTO:N",
                title="Departamento",
                sort="-x",
            ),
            tooltip=[
                alt.Tooltip("DEPARTAMENTO:N", title="Departamento"),
                alt.Tooltip(
                    "cantidad_hurtos:Q",
                    title="Cantidad de hurtos",
                    format=",",
                ),
            ],
        )
        .properties(
            title=alt.TitleParams(
                text="Cantidad de hurtos por departamento",
                subtitle=(
                    "Fuente: datos/limpio/hurto_personas_limpio.csv"
                ),
            ),
            width=700,
            height=500,
        )
    )


def main() -> None:
    """Genera y guarda el gráfico departamental."""
    datos = cargar_y_agrupar_datos()
    grafico = crear_grafico(datos)
    RUTA_GRAFICO.parent.mkdir(parents=True, exist_ok=True)
    grafico.save(RUTA_GRAFICO)
    print(f"Gráfico guardado en: {RUTA_GRAFICO}")


if __name__ == "__main__":
    main()
