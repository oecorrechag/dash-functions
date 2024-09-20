# Conditional Formatting

El formato condicional se proporciona a través de la propiedad **style_data_conditional**. La palabra clave **if** proporciona un conjunto de instrucciones de formato condicional y el resto de las palabras clave son propiedades CSS con formato **camelCased**.

La sintaxis if admite varios operadores: row_index, column_id, filter_query, column_type, column_editable y state.

**filter_query** es la opción más flexible cuando se trabaja con datos.

A continuación, se incluye un ejemplo de todos los operadores:

```bash
1.conditional_formatting.py
```
Notas:

- **filter_query** admite distintos operadores según el tipo de datos de la columna:
    - =, >, >=, <, <= y contains son compatibles con todos los tipos de datos (numéricos, de texto, de fecha y hora y cualquier otro).
    - Con contains, el lado derecho debe ser una cadena, por lo que {Date} contains "01" funcionará, pero {Date} contains 1 no.
    - datestartswith es compatible con datetime
    - is nil es compatible con todos los tipos de datos
    - is blank es compatible con todos los tipos de datos
- El tipo de datos predeterminado de una columna es cualquiera
- **column_type** hace referencia al tipo de datos de la columna (numérico, texto, fecha y hora, etc.)
- **column_editable** puede ser igual a Verdadero o Falso (novedad en Dash 1.12.0)
- **state** puede ser igual a 'active' o 'selected' (novedad en Dash 1.12.0). Úselo para cambiar los colores de fondo y borde rosados ​​predeterminados para las celdas seleccionadas y activas.
- row_index es absoluto: si filtra u ordena su tabla, la quinta fila permanecerá resaltada. Intente ordenar las columnas y observe cómo "San Francisco" permanece resaltado, pero "Londres" no.
- column_id, row_index y header_index pueden ser iguales a un escalar (como se indica arriba) o a una lista de valores. Por ejemplo, 'column_id': ['Region', 'Pressure'] es válido (novedad en Dash 1.12.0). El filtrado de DataTable y el formato condicional funcionan más rápido cuando se especifica una lista de valores en lugar de una lista de bloques if separados.
- **id** es una columna oculta especial que se puede utilizar como alternativa a row_index para resaltar datos por índice. Dado que cada fila tiene un id único, el formato condicional asociado con este id permanecerá asociado con esos datos después de ordenarlos y filtrarlos.
- **RebeccaPurple**, **hotpink**, **DodgerBlue**... Estos son colores CSS con nombre. Recomendamos evitar los nombres de colores comunes como rojo, azul, verde, ya que parecen muy anticuados. Para ver otras sugerencias de colores, consulte http://clrs.cc/.
- Dado que estamos utilizando .format, escapamos { con \{{ y } con \}}.
- Para resaltar una fila, omita column_id. Para resaltar una celda en particular, incluya column_id.
- **style_cell_conditional** (todas las celdas, incluidos los encabezados), style_header_conditional (celdas de encabezado), style_filter_conditional (filtrar cuadros de entrada) son palabras clave alternativas que se pueden usar para filtrar otras partes de la tabla.
- **Limitación**: si la tabla es editable, el valor máximo podría cambiar si el usuario edita la tabla. Dado que este ejemplo codifica de forma rígida el valor máximo en la expresión de filtro, el valor resaltado ya no se resaltaría. Como solución alternativa, puede actualizar style_data_conditional a través de una devolución de llamada siempre que cambie derived_virtual_data. Esta limitación se aplica a cualquier formato condicional con números codificados de forma rígida calculados a partir de una expresión en Python (¡incluidos muchos de los ejemplos a continuación!). Consulte plotly/dash-table#755 para obtener actualizaciones.

## Alternative Highlighting Styles

En lugar de resaltar la celda de fondo, puede cambiar el color del texto, ponerlo en negrita, agregar subrayados o darle estilo usando cualquier otra propiedad CSS.

```bash
2.alternative_highlighting_styles.py
```

## Special Characters like Emojis, Stars, Checkmarks, Circles

Puede copiar y pegar caracteres Unicode de emoji directamente en su código. Recomendamos copiar valores de emojipedia, p. ej., https://emojipedia.org/star/.

Todos los años se lanzan nuevos caracteres Unicode de emoji y es posible que no estén disponibles en los conjuntos de caracteres de las máquinas de su audiencia. La apariencia de estos íconos difiere en la mayoría de los sistemas operativos.

```bash
3.special_characters_like_emojis,_stars,_checkmarks,_circles.py
```

## Filtering and Conditional Formatting Recipes

### Highlighting the Max Value in a Column

```bash
4.highlighting_the_max_value_in_a_column.py
```

### Highlighting a Row with the Min Value

```bash
5.highlighting_a_row_with_the_min_value.py
```

### Highlighting the Top Three or Bottom Three Values in a Column

```bash
6.highlighting_the_top.py
```

### Highlighting the Max Value in Every Row

```bash
7.highlighting_the_max_value.py
```

### Highlighting the Top Two Values in a Row

```bash
8.top_two_values_in_a_row.py
```

## Highlighting the Maximum Value in the Table

```bash
9.maximum_value_in_the_table.py
```

## Highlighting a Range of Values

```bash
10.highlighting_a_range_of_values.py
```

```bash
11.highlighting_a_range_of_values.py
```

Vamos a descomponer \{{\{col}}}. Queremos que la expresión final se parezca a algo como {2017} > 5 & {2017} < 10 donde 2017 es el nombre de la columna. Como estamos usando .format(), necesitamos escapar los corchetes, por lo que {2017} sería {{2017}}. Luego, necesitamos reemplazar 2017 con {col} para buscar y reemplazar, por lo que se convierte en \{{\{col}}}.format(col=col)

## Highlighting Top 10% or Bottom 10% of Values by Column

```bash
12.values_by_column.py
```

```bash
13.values_by_column.py
```

## Highlighting Values above Average and Below Average

Aquí, el resaltado se realiza por columna.

```bash
14.values_above_average_and_below_average.py
```

Aquí el resaltado se realiza por tabla.

```bash
15.values_above_average_and_below_average.py
```

## Highlighting None, NaN, or Empty String Values

Tres consultas de filtro ayudan con valores vacíos o en blanco:

{my_column} es nulo y coincidirá con valores Ninguno
{my_column} es blanco y coincidirá con valores Ninguno y cadenas vacías
{my_column} = "" coincidirá con cadenas vacías

```bash
16.highlighting_none,_nan,_or_empty_string_values.py
```

## Displaying Special Values for NaN or None Values

```bash
17.special_values_for_nan_or_none_values.py
```

**Limitaciones:**

- Format(nully=) aún no coincide con cadenas vacías, solo con valores None. Consulte plotly/- dash-table#763 para obtener actualizaciones.
- 'type': 'numeric' debe configurarse, consulte plotly/dash-table#762 para obtener actualizaciones.

Un método alternativo sería completar, por ejemplo, "N/A" en los datos antes de renderizar:

```bash
18.special_values_for_nan_or_none_values.py
```

**Limitación**: si su tabla es editable, si un usuario elimina el contenido de una celda, ya no se mostrará "N/D". Esto es diferente del ejemplo con Formato, donde DataTable mostrará automáticamente N/D para todas las celdas vacías, incluso después de la edición.

## Highlighting Text that Contains a Value

```bash
19.highlighting_text_that_contains_a_value.py
```

## Highlighting Text that Equals a Value

```bash
20.highlighting_text_that_equals_a_value.py
```

## Highlighting Cells by Value with a Colorscale Like a Heatmap

Esta receta sombrea celdas con style_data_conditional y crea una leyenda con componentes HTML. Necesitará instalar pip **colorlover** para obtener las escalas de colores.

```bash
21.colorscale_like_a_heatmap.py
```

## Highlighting with a Colorscale on a Single Column

```bash
22.colorscale_on_a_single_column.py
```

## Displaying Data Bars

Estas recetas muestran un uso creativo de los colores de fondo con degradados lineales para mostrar gráficos de barras horizontales dentro de la tabla. ¡Los resultados pueden variar! Siéntete libre de modificar estas recetas para tu propio uso.

```bash
23.displaying_data_bars.py
```

## Data Bars without Text

Muestra las barras de datos sin texto creando una nueva columna y haciendo que el texto sea transparente.

```bash
24.data_bars_without_text.py
```

## Diverging Data Bars

La función **data_bars_diverging** divide los datos en dos cuadrantes por el punto medio. Las representaciones alternativas de las barras de datos pueden dividir los datos por números positivos y negativos o por los valores promedio. ¡Tus resultados pueden variar! Siéntete libre de modificar la función **data_bars_diverging** según tus propias necesidades de visualización. 

```bash
25.diverging_data_bars.py
```

## Highlighting Dates


