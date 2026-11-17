"""Genera la evolución mensual de hurtos con Altair."""

from pathlib import Path

import altair as alt
import pandas as pd


RUTA_PROYECTO = Path(__file__).resolve().parents[1]
RUTA_DATOS = (
    RUTA_PROYECTO / "datos" / "limpio" / "hurto_personas_limpio.csv"
)
RUTA_GRAFICO = (
    RUTA_PROYECTO / "docs" / "graficos" / "evolucion_mensual.html"
)


def cargar_y_agrupar_datos() -> pd.DataFrame:
    """Carga los datos limpios y suma la cantidad por año y mes."""
    datos = pd.read_csv(
        RUTA_DATOS,
        usecols=["año", "mes", "CANTIDAD"],
    )
    evolucion_mensual = (
        datos.groupby(["año", "mes"], as_index=False, sort=True)["CANTIDAD"]
        .sum()
        .rename(columns={"CANTIDAD": "cantidad_hurtos"})
    )
    evolucion_mensual["fecha_mes"] = pd.to_datetime(
        {
            "year": evolucion_mensual["año"],
            "month": evolucion_mensual["mes"],
            "day": 1,
        }
    )
    return evolucion_mensual


def crear_grafico(datos: pd.DataFrame) -> alt.Chart:
    """Crea la serie temporal mensual."""
    return (
        alt.Chart(datos)
        .mark_line(point=True)
        .encode(
            x=alt.X(
                "fecha_mes:T",
                title="Mes",
                axis=alt.Axis(format="%b %Y", labelAngle=-45),
            ),
            y=alt.Y(
                "cantidad_hurtos:Q",
                title="Cantidad de hurtos",
            ),
            tooltip=[
                alt.Tooltip("fecha_mes:T", title="Mes", format="%B %Y"),
                alt.Tooltip(
                    "cantidad_hurtos:Q",
                    title="Cantidad de hurtos",
                    format=",",
                ),
            ],
        )
        .properties(
            title=alt.TitleParams(
                text="Evolución mensual de hurtos",
                subtitle=(
                    "Fuente: datos/limpio/hurto_personas_limpio.csv"
                ),
            ),
            width=800,
            height=400,
        )
    )


def main() -> None:
    """Genera y guarda el gráfico mensual."""
    datos = cargar_y_agrupar_datos()
    grafico = crear_grafico(datos)
    RUTA_GRAFICO.parent.mkdir(parents=True, exist_ok=True)
    grafico.save(RUTA_GRAFICO)
    print(f"Gráfico guardado en: {RUTA_GRAFICO}")


if __name__ == "__main__":
    main()
