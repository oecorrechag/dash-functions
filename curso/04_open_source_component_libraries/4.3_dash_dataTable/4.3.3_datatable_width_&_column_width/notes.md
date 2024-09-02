# DataTable Width & Column Width

## Default Width

De forma predeterminada, la tabla se expandirá hasta el ancho de su contenedor. El ancho de las columnas se determina automáticamente para acomodar el contenido de las celdas.

```bash
1.default_width.py
```

Los estilos predeterminados funcionan bien para una pequeña cantidad de columnas y texto breve. Sin embargo, si está procesando una gran cantidad de columnas o celdas con contenido extenso, deberá emplear una de las siguientes estrategias de desbordamiento para mantener la tabla dentro de su contenedor.

## Wrapping onto Multiple Lines

Si sus celdas contienen texto con espacios, puede desbordar su contenido en varias líneas. <br>
**style_cell** actualiza el estilo de las celdas de datos y de encabezado. Para especificar estilos de encabezado, utilice **style_header**. Para especificar estilos de celdas de datos, utilice **style_data**. <br>
Este ejemplo mantiene el encabezado en una sola línea mientras envuelve las celdas de datos.

```bash
2.wrapping_onto_multiple_lines.py
```

## Denser Multi-Line Cells with Line-Height

Si muestra mucho texto en las celdas, puede que desee hacer que el texto parezca un poco más denso acortando la altura de línea. De manera predeterminada (como se muestra arriba), es de alrededor de 22 px. Aquí, es de 15 px.

```bash
3.denser_multi-line_cells_with_line-height.py
```

## Wrapping onto Multiple Lines while Constraining the Height of Cells

Si su texto es muy largo, puede restringir la altura de las celdas y mostrar una información sobre herramientas al pasar el cursor sobre la celda.

```bash
4.wrapping_onto_multiple_lines_while_constraining_the_height_of_cells.py
```

Pase el cursor sobre las celdas para ver la información sobre herramientas.

¿Por qué el CSS? Las celdas de altura fija son complicadas porque, según las reglas CSS 2.1, la altura de una celda de tabla es "la altura mínima requerida por el contenido". Por lo tanto, aquí estamos configurando la altura de la celda indirectamente al configurar el div dentro de la celda.

En este ejemplo, mostramos dos líneas de datos configurando la altura de línea en 15 px y la altura de cada celda en 30 px. La segunda oración está cortada.

Este método tiene algunas limitaciones:

1. No es posible mostrar elipses con este método.
2. No es posible configurar una altura máxima. Todas las celdas deben tener la misma altura.

Suscríbete a plotly/dash-table#737 para recibir actualizaciones u otras soluciones alternativas a este problema.

## Overflowing Into Ellipses

Como alternativa, puede mantener el contenido en una sola línea pero mostrar un conjunto de puntos suspensivos si el contenido es demasiado largo para caber en la celda.

Aquí, max-width se establece en 0. Puede ser cualquier número, lo único importante es que se proporcione. El comportamiento será el mismo ya sea 0 o 50.

Si solo desea ocultar el contenido en lugar de mostrar puntos suspensivos, configure textOverflow en 'clip' en lugar de 'ellipsis'.

```bash
5.overflowing_into_ellipses.py
```

## Ellipses & Tooltips

Si muestra datos de texto cortados por puntos suspensivos, puede incluir información sobre herramientas para que el texto completo aparezca al pasar el mouse sobre la celda.

Al configurar **tooltip_duration** en **None**, la información sobre herramientas persistirá mientras el puntero del mouse se encuentre sobre la celda y desaparecerá cuando el puntero se aleje. Puede anular esto al pasar un número en milisegundos (por ejemplo, 2000 si desea que desaparezca después de dos segundos).

```bash
6.ellipses_&_tooltips.py
```

## Horizontal Scroll

En lugar de intentar que todo el contenido entre en el contenedor, puedes convertirlo en un contenedor desplazable.

```bash
7.horizontal_scroll.py
```

Observe que aún no hemos establecido explícitamente el ancho de las columnas individuales. El ancho de las columnas se ha calculado de forma dinámica en función del ancho de la tabla y del ancho del contenido de la celda. En el ejemplo anterior, al proporcionar una barra de desplazamiento, estamos otorgando a la tabla el ancho que necesita para que quepa todo el ancho del contenido de la celda en una sola línea.

## Horizontal Scroll with Fixed-Width Columns & Cell Wrapping

Como alternativa, puede fijar el ancho de cada columna agregando width. En este caso, el ancho de la columna será constante, incluso si su contenido es más corto o más ancho.

```bash
8.fixed-width_columns_&_cell_wrapping.py
```

## Horizontal Scroll with Fixed-Width & Ellipses

```bash
9.scroll_with_fixed-width_&_ellipses.py
```

## Horizontal Scrolling via Fixed Columns

También puede agregar una barra de desplazamiento horizontal a su tabla fijando las columnas más a la izquierda con **fixed_columns**.

```bash
10.horizontal_scrolling_via_fixed_columns.py
```

Aquí está el mismo ejemplo pero con celdas y elipses de ancho fijo.

```bash
11.horizontal_scrolling_via_fixed_columns.py
```

## Setting Column Widths