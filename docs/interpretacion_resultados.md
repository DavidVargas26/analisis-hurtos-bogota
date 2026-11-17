# Interpretación de resultados

## Fuente y alcance

Las interpretaciones se basan en los tres gráficos generados a partir de
`datos/limpio/hurto_personas_limpio.csv`:

- `evolucion_mensual.html`
- `top_10_municipios.html`
- `departamentos.html`

La variable analizada es `CANTIDAD`. Los resultados describen los registros
disponibles en el archivo y no deben interpretarse como tasas de ocurrencia,
pues el conjunto no incluye denominadores poblacionales, exposición al riesgo
ni información sobre la cobertura del reporte.

## 1. Evolución mensual de hurtos

### Principales hallazgos

La serie cubre el periodo comprendido entre enero de 2003 y septiembre de
2026. Se observa un crecimiento general del volumen mensual desde los primeros
años hasta niveles considerablemente mayores en los años recientes. El máximo
mensual de la serie se registra en octubre de 2022, con 37.326 hurtos. También
se observan valores elevados en varios meses de 2022 y 2023.

El mínimo mensual corresponde a diciembre de 2004, con 2.019 hurtos. La
diferencia entre ese mínimo y los valores máximos muestra que la magnitud
registrada no es constante a lo largo del periodo.

### Patrones relevantes

- Entre 2003 y 2019 predomina una trayectoria ascendente, aunque con
  fluctuaciones entre meses.
- En 2020 aparece una disminución marcada frente a 2019.
- La serie vuelve a crecer en 2021 y alcanza niveles altos en 2022 y 2023.
- En 2024 y 2025 el total anual disminuye respecto de 2023.
- El año 2026 llega únicamente hasta septiembre en el archivo; por tanto, su
  acumulado no es comparable directamente con los años completos.

### Posibles explicaciones basadas en los datos

El descenso de 2020 y la recuperación posterior son cambios temporales
claramente visibles en los registros, pero este archivo no contiene variables
que permitan atribuirlos a una causa específica. La tendencia ascendente
también puede reflejar cambios en el volumen de reportes, en la cobertura del
registro o en la forma de consolidar la información, además de cambios en el
fenómeno observado. Para distinguir esas posibilidades se requerirían datos
adicionales y una validación de la metodología de recolección.

## 2. Top 10 de municipios

### Principales hallazgos

Bogotá D.C. ocupa el primer lugar con 1.379.012 hurtos, equivalente al 36,28 %
del total registrado. Le siguen Medellín, con 288.620, y Cali, con 261.159.
Barranquilla ocupa el cuarto lugar con 143.107, mientras que Bucaramanga
registra 95.463.

Los diez municipios representados en el gráfico reúnen aproximadamente el
66,05 % de la cantidad total. Esto indica una concentración importante del
registro en un conjunto reducido de municipios.

### Patrones relevantes

- Bogotá D.C. se encuentra claramente por encima del resto del ranking.
- Medellín y Cali forman un segundo grupo, aunque con valores inferiores al de
  Bogotá D.C.
- Después de las cuatro primeras posiciones, las diferencias son menores y el
  descenso entre municipios es más gradual.
- `SIN ESTABLECER` aparece entre los diez primeros. Esta categoría no
  corresponde a un municipio identificable y debe conservarse como una señal
  de clasificación territorial faltante o no determinada.

### Posibles explicaciones basadas en los datos

La concentración puede estar asociada a una mayor cantidad de registros en
municipios con mayor volumen absoluto de población, actividad o reportes, pero
el dataset no contiene esas variables y no permite establecer cuál de esas
explicaciones es determinante. Tampoco es válido concluir que Bogotá D.C.
tenga la mayor tasa de hurtos: el gráfico compara cantidades absolutas.

La presencia de `SIN ESTABLECER` sugiere que parte de los registros no tiene
una asignación municipal identificable. Esto puede afectar la interpretación
del ranking y justifica revisar la calidad de la clasificación geográfica en
análisis posteriores.

## 3. Cantidad de hurtos por departamento

### Principales hallazgos

Bogotá D.C. es la categoría con mayor cantidad acumulada, con 1.379.012
registros, seguida por Antioquia, con 418.269, y Valle del Cauca, con
363.414. Estas tres categorías concentran aproximadamente el 56,84 % del total.

Cundinamarca, Atlántico y Santander ocupan las posiciones siguientes, con
valores entre 173.147 y 189.921. En el extremo inferior del gráfico aparecen
Vaupés, Vichada, Guainía y Guaviare, con cantidades absolutas menores dentro de
este conjunto de datos.

### Patrones relevantes

- La distribución departamental es asimétrica: pocas categorías concentran
  una parte sustancial del total.
- Bogotá D.C. presenta una diferencia amplia frente al segundo lugar.
- Antioquia y Valle del Cauca forman un grupo intermedio alto.
- Existe una cola extensa de departamentos con cantidades progresivamente
  menores.
- `SIN ESTABLECER` también aparece como categoría departamental, por lo que no
  representa un departamento identificable.

### Posibles explicaciones basadas en los datos

Las diferencias pueden reflejar variaciones en el tamaño y la concentración
territorial de la población, en la actividad registrada o en la cobertura de
los reportes. Sin variables de población, exposición, presencia institucional
o completitud del registro, el gráfico solo permite describir cantidades
acumuladas y no comparar riesgos relativos entre departamentos.

La categoría `SIN ESTABLECER` evidencia que existe información sin asignación
territorial completa. Esta situación puede reducir artificialmente las
cantidades de algunas categorías y debe considerarse antes de realizar
comparaciones geográficas más específicas.

## Conclusión

Los gráficos muestran una evolución temporal no estable y una concentración
territorial marcada. El volumen registrado aumenta de forma general hasta
2019, presenta una caída en 2020 y alcanza valores elevados en 2022-2023,
mientras que Bogotá D.C., Antioquia y Valle del Cauca concentran una parte
importante del total. Estos hallazgos son descriptivos: no establecen
causalidad ni permiten estimar tasas sin incorporar información adicional.
