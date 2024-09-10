# Styling the DataTable

## Default Styles

De manera predeterminada, la DataTable tiene encabezados y bordes grises alrededor de cada celda. Se parece a una hoja de cálculo y los encabezados están claramente definidos.

```bash
1.default_styles.py
```

## Column Alignment

Al mostrar datos numéricos, es una buena práctica utilizar fuentes monoespaciadas, alinear los datos a la derecha y proporcionar la misma cantidad de decimales en toda la columna.

En el caso de los datos textuales, suele ser más fácil leerlos alineando el texto a la izquierda.

En ambos casos, los encabezados de las columnas deben tener la misma alineación que el contenido de la celda.

```bash
2.column_alignment.py
```

## Styling the Table as a List

La vista en cuadrícula es una buena vista predeterminada para una tabla editable, ya que se ve y se siente como una hoja de cálculo. Si su tabla no es editable, en muchos casos puede verse más ordenada sin las líneas de cuadrícula verticales.

```bash
3.styling_the_table_as_a_list.py
```

## List Style with Minimal Headers

En algunos contextos, el fondo gris puede resultar un poco pesado. Puedes aligerarlo con un fondo blanco y un texto en negrita.

```bash
4.list_style_with_minimal_headers.py
```

## Striped Rows

Cuando visualiza conjuntos de datos en los que necesita comparar valores dentro de filas individuales, a veces puede resultar útil asignarles a las filas colores de fondo alternos. Recomendamos utilizar colores descoloridos para no atraer demasiado la atención a las rayas.

Tenga en cuenta los tres grupos diferentes a los que puede aplicar estilos: "celda" es toda la tabla, "encabezado" son solo las filas de encabezado y "datos" son solo las filas de datos. Para usar estilos pares/impares u otros basados ​​en row_index, debe usar **style_data_conditional**.

```bash
5.striped_rows.py
```

## Multi-Headers

Los encabezados múltiples son compatibles de forma nativa en DataTable. Solo tienes que configurar el nombre dentro de las columnas como una lista de cadenas en lugar de una sola cadena y activar **merge_duplicate_headers**=**True**. DataTable comprobará los vecinos de cada fila de encabezado y, si coinciden, los fusionará en una sola celda automáticamente.

```bash
6.multi-headers.py
```

## Dark Theme with Cells

Tienes control total sobre todos los elementos de la tabla. Si estás viendo tu tabla en una aplicación con un fondo oscuro, puedes proporcionar colores de fuente y fondo invertidos.

```bash
7.dark_theme_with_cells.py
```

## Styles Priority

Existe un orden específico de prioridad para las propiedades style_*. Si hay varias propiedades style_*, la que tenga mayor prioridad tendrá precedencia. Dentro de cada propiedad, las reglas para índices más altos tendrán prioridad sobre las de índices más bajos. Los estilos aplicados previamente con la misma prioridad prevalecen sobre los posteriores (aplicados de arriba hacia abajo, de izquierda a derecha).

Estas son las prioridades de las propiedades style_*, en orden decreciente:

1. style_data_conditional
2. style_data
3. style_filter_conditional
4. style_filter
5. style_header_conditional
6. style_header
7. style_cell_conditional
8. style_cell

```bash
8.dark_theme_with_cells.py
```

## Adding Borders

Personaliza los bordes de la tabla agregando borde a los accesorios de **style***.

```bash
9.adding_borders.py
```

## Styling Editable Columns

Las columnas editables se pueden diseñar utilizando column_editable en las propiedades **style_header_conditional**, **style_filter_conditional** y **style_data_conditional**.

```bash
10.styling_editable_columns.py
```
