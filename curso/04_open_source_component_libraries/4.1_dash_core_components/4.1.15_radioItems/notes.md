# dcc.RadioItems

**dcc.RadioItems** es un componente para representar un conjunto de botones de opción. Los usuarios pueden seleccionar una opción del conjunto. Consulte la Lista de verificación para seleccionar varias opciones a la vez y el Menú desplegable para obtener una vista más compacta.

## Basic RadioItems

Para crear un radioitems básico, proporcione opciones y un valor al componente **dcc.RadioItems** en ese orden.

```bash
1.basic_radioItems.py
```

## Horizontal Options

Las etiquetas del ejemplo anterior en los RadioItems se muestran verticalmente. inline=True para que las etiquetas se muestren horizontalmente:

```bash
2.horizontal_options.py
```

En el ejemplo anterior, al configurar inline=True, configuramos los RadioItems para que se muestren horizontalmente.

Esta propiedad es una forma abreviada de configurarla en la propiedad labelStyle y está disponible desde Dash 2.1. Lo mismo se puede hacer con labelStyle={'display': 'inline-block'} en versiones anteriores de Dash.

## Options and Value

Las propiedades de opciones y valor son los dos primeros argumentos de **dcc.RadioItems**. Existen varias formas de configurar las opciones. Los siguientes ejemplos definen el mismo componente RadioItems:

```python
dcc.RadioItems(['New York City', 'Montreal', 'San Francisco'], 'Montreal')
```

```python
dcc.RadioItems(
   options=['New York City', 'Montreal', 'San Francisco'],
   value='Montreal'
)
```

```python
dcc.RadioItems(
   options=[
       {'label': 'New York City', 'value': 'New York City'},
       {'label': 'Montreal', 'value': 'Montreal'},
       {'label': 'San Francisco', 'value': 'San Francisco'},
   ],
   value='Montreal'
)
```

```python
dcc.RadioItems(
   options={
        'New York City': 'New York City',
        'Montreal': 'Montreal',
        'San Francisco': 'San Francisco'
   },
   value='Montreal'
)
```

En estos ejemplos, la etiqueta de la opción (lo que ve el usuario) y el valor (lo que se pasa al callback) son equivalentes. A menudo resulta útil que estén separados para poder cambiar fácilmente la etiqueta sin cambiar la lógica del callback que utiliza el valor:

```python
dcc.RadioItems(
   options={
        'NYC': 'New York City',
        'MTL': 'Montreal',
        'SF': 'San Francisco'
   },
   value='MTL'
)
```

Las opciones proporcionadas como un único diccionario se muestran sin ningún orden en particular en el navegador. Proporcionar una lista que contenga un diccionario para cada opción garantiza que las opciones se muestren en el orden proporcionado.

```python
dcc.RadioItems(
   options=[
       {'label': 'New York City', 'value': 'NYC'},
       {'label': 'Montreal', 'value': 'MTL'},
       {'label': 'San Francisco', 'value': 'SF'},
   ],
   value='MTL'
)
```

## Disable Options

```bash
3.disable_options.py
```

## Flexible Data Types

Hemos visto cómo se pueden configurar las opciones mediante una lista, un diccionario o una lista de diccionarios. options también acepta estructuras de datos de Pandas y NumPy.

En este ejemplo, usamos las columnas de DataFrame (df.columns) como opciones.

```bash
4.flexible_data_types.py
```

Aquí, configuramos las opciones con df.nation.unique(). Este método de Pandas devuelve valores únicos en la columna de nación. Al pasarlo a opciones, nuestro componente RadioItems muestra todos los valores únicos en esa columna.

```bash
5.flexible_data_types.py
```

## Components as Option Labels

En los ejemplos anteriores, hemos establecido las etiquetas de opciones como cadenas. También puedes usar componentes Dash como etiquetas de opciones. En este ejemplo, cada etiqueta es una lista de componentes que contienen un html.Img y texto en un html.Span.

```python
from dash import dcc, html

dcc.RadioItems(
    [
        {
            "label":
                [
                    html.Img(src="/assets/images/language_icons/python_50px.svg", height=30),
                    html.Span("Python", style={'font-size': 15, 'padding-left': 10}),
                ],
            "value": "Python",
        },
        {
            "label":
                [
                    html.Img(src="/assets/images/language_icons/julia_50px.svg", height=30),
                    html.Span("Julia", style={'font-size': 15, 'padding-left': 10}),
                ], 
            "value": "Julia",
        },
        {
            "label":
                [
                    html.Img(src="/assets/images/language_icons/r-lang_50px.svg", height=30),
                    html.Span("R", style={'font-size': 15, 'padding-left': 10}),
                ],
            "value": "R",
        },
    ], labelStyle={"display": "flex", "align-items": "center"},
)
```

## Styling Components as Option Labels

También puedes diseñar etiquetas utilizando componentes html.Div para cada etiqueta y luego configurando estilos utilizando la propiedad de estilo:

```python
from dash import dcc, html

dcc.RadioItems(
    [
        {
            "label": html.Div(['Montreal'], style={'color': 'Gold', 'font-size': 20}),
            "value": "Montreal",
        },
        {
            "label": html.Div(['NYC'], style={'color': 'MediumTurqoise', 'font-size': 20}),
            "value": "NYC",
        },
        {
            "label": html.Div(['London'], style={'color': 'LightGreen', 'font-size': 20}),
            "value": "London",
        },
    ], value='Montreal'
)

```
