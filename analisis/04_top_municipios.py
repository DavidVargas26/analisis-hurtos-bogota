"""Genera el ranking de municipios con mayor cantidad de hurtos."""

from pathlib import Path

import altair as alt
import pandas as pd


RUTA_PROYECTO = Path(__file__).resolve().parents[1]
RUTA_DATOS = (
    RUTA_PROYECTO / "datos" / "limpio" / "hurto_personas_limpio.csv"
)
RUTA_GRAFICO = RUTA_PROYECTO / "docs" / "graficos" / "top_10_municipios.html"


def cargar_y_agrupar_datos() -> pd.DataFrame:
    """Carga los datos y obtiene los 10 municipios con mayor suma."""
    datos = pd.read_csv(
        RUTA_DATOS,
        usecols=["MUNICIPIO", "CANTIDAD"],
    )
    municipios = (
        datos.groupby("MUNICIPIO", as_index=False)["CANTIDAD"]
        .sum()
        .rename(columns={"CANTIDAD": "cantidad_hurtos"})
        .nlargest(10, "cantidad_hurtos")
    )
    return municipios


def crear_grafico(datos: pd.DataFrame) -> alt.Chart:
    """Crea el gráfico de barras horizontales del ranking."""
    return (
        alt.Chart(datos)
        .mark_bar()
        .encode(
            x=alt.X(
                "cantidad_hurtos:Q",
                title="Cantidad de hurtos",
            ),
            y=alt.Y(
                "MUNICIPIO:N",
                title="Municipio",
                sort="-x",
            ),
            tooltip=[
                alt.Tooltip("MUNICIPIO:N", title="Municipio"),
                alt.Tooltip(
                    "cantidad_hurtos:Q",
                    title="Cantidad de hurtos",
                    format=",",
                ),
            ],
        )
        .properties(
            title=alt.TitleParams(
                text="Top 10 municipios con más hurtos",
                subtitle=(
                    "Fuente: datos/limpio/hurto_personas_limpio.csv"
                ),
            ),
            width=700,
            height=400,
        )
    )


def main() -> None:
    """Genera y guarda el ranking de municipios."""
    datos = cargar_y_agrupar_datos()
    grafico = crear_grafico(datos)
    RUTA_GRAFICO.parent.mkdir(parents=True, exist_ok=True)
    grafico.save(RUTA_GRAFICO)
    print(f"Gráfico guardado en: {RUTA_GRAFICO}")


if __name__ == "__main__":
    main()
