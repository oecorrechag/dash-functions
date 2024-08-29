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




