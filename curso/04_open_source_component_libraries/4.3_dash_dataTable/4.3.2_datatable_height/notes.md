# DataTable Height

De forma predeterminada, la altura de la tabla se ampliará para mostrar hasta 250 filas. Después de 250 filas, la tabla mostrará una interfaz de paginación que permite ver hasta 250 filas a la vez.

## Setting Table Height with Pagination

Si utiliza paginación, puede controlar la altura mostrando menos filas a la vez. En lugar de 250 filas, podría mostrar 10 filas a la vez. De forma predeterminada y sin ajuste, cada fila ocupa 30 px. Por lo tanto, 10 filas con un encabezado establecerían la tabla en 330 px de alto. La interfaz de paginación en sí tiene alrededor de 60 px de alto.

```bash
1.setting_table_height_with_pagination.py
```

## Setting Table Height with Vertical Scroll

Si la tabla contiene menos de aproximadamente 1000 filas, una opción es eliminar la paginación, restringir la altura y mostrar una barra de desplazamiento vertical.

```bash
2.setting_table_height_with_vertical_scroll.py
```

Si tiene más de 1000 filas, el navegador se ralentizará al intentar representar la tabla. Con más de 1000 filas, recomendamos cambiar a paginación de navegador o servidor (como se indica más arriba) o virtualización (como se indica más abajo).

## Vertical Scroll With Pagination

Si tiene más de ~1000 filas, puede mantener la paginación en la parte inferior de la tabla, restringir la altura y mostrar una barra de desplazamiento vertical.

```bash
3.vertical_scroll_with_pagination.py
```

## Vertical Scroll With Fixed Headers

También puedes fijar los encabezados para que el contenido de la tabla se desplace pero los encabezados permanezcan visibles.

```bash
4.vertical_scroll_with_fixed_headers.py
```

## Limitations

1. Los anchos de columna basados ​​en porcentajes no están disponibles con filas fijas y diseño de tabla: fijo. Ver https://github.com/plotly/dash-table/issues/748

2. Anchos basados ​​en porcentajes con fixed_rows y sin table-layout: fixed tiene algunos problemas al cambiar el tamaño de la ventana. Ver https://github.com/plotly/dash-table/issues/747

3. Si el filtrado está habilitado, el desplazamiento horizontal no funciona con tablas anchas. https://github.com/plotly/dash-table/issues/746

4. Si el encabezado de una columna es más ancho que los datos dentro de esa columna y el contenedor de la tabla no es lo suficientemente ancho para mostrar los encabezados, entonces la columna será tan ancha como los datos y el texto del encabezado se truncará (la mayoría de los navegadores) o se desbordará hacia la siguiente columna (Firefox). Esto es un error ([plotly/dash-table#432](https://github.com/plotly/dash-table/issues/432)). La solución actual es ocultar el desbordamiento o fijar el ancho de las columnas en píxeles. Al usar esta solución alternativa, puede encontrarse con algunos de estos problemas:

    4.1. En aquellos casos en los que el encabezado está cortado, no es posible colocar puntos suspensivos dentro del encabezado. Para obtener actualizaciones, consulte https://github.com/plotly/dash-table/issues/735

    4.2. Cuando el texto se trunca, resulta útil mostrar información sobre herramientas que muestre el texto completo. Aún no es posible agregar información sobre herramientas a los encabezados. Para obtener actualizaciones, consulte https://github.com/plotly/dash-table/issues/295

    4.3. Si el texto del encabezado se trunca, el desbordamiento del encabezado es visible. La solución actual consiste en ocultar el desbordamiento con overflow: 'hidden'.

## Vertical Scroll with Virtualization

Como se mencionó anteriormente, el navegador tiene dificultades para representar miles de filas en una tabla. Al representar las filas sobre la marcha mientras se desplaza, la virtualización soluciona los problemas de rendimiento de representación inherentes al navegador web.

Todos los datos de su tabla se seguirán enviando a través de la red al navegador, por lo que si está mostrando más de 10 000 a 100 000 filas, puede considerar el uso de paginación de back-end para reducir el volumen de datos que se transfieren a través de la red y el uso de memoria asociado.

```bash
5.vertical_scroll_with_virtualization.py
```

## Limitations

1. Con la virtualización, el navegador no conoce el ancho de las columnas de antemano; solo puede determinar el ancho de las columnas cuando se renderizan. Por lo tanto, las columnas pueden cambiar de tamaño a medida que se desplaza, a menos que fije el ancho de las columnas.

2. Dado que, con la virtualización, estamos renderizando filas sobre la marcha mientras nos desplazamos, el rendimiento de renderización será más lento que el desplazamiento vertical nativo optimizado para el navegador. Si se desplaza rápidamente, puede notar que la tabla aparece momentáneamente en blanco hasta que se completa la renderización.

3. Existen las mismas limitaciones de fixed_rows que se mencionaron anteriormente.
