# dcc.Checklist

**dcc.Checklist** es un componente para representar un conjunto de casillas de verificación. Consulte también RadioItems para seleccionar una sola opción a la vez o Menú desplegable para una vista más compacta.

## Basic Checklist

```python
from dash import dcc

dcc.Checklist(
    ['New York City', 'Montréal', 'San Francisco'],
    ['New York City', 'Montréal']
)
```

## Horizontal Options

```python
from dash import dcc

dcc.Checklist(
    ['New York City', 'Montréal', 'San Francisco'],
    ['New York City', 'Montréal'],
    inline=True
)
```

**inline=True**, configuramos las opciones de la lista de verificación para que se muestren horizontalmente. Esta propiedad es una abreviatura para configurarla en la propiedad labelStyle y está disponible desde Dash 2.1. Se puede hacer lo mismo con labelStyle={'display': 'inline-block'} en versiones anteriores de Dash.

## Options and Value

Las opciones y las propiedades de valor son los dos primeros argumentos de **dcc.Checklist**. Hay varias formas de configurar **Opciones**. Los siguientes ejemplos definen la misma lista de verificación:

```python
dcc.Checklist(['New York City', 'Montreal', 'San Francisco'], ['Montreal'])
```

```python
dcc.Checklist(
   options=['New York City', 'Montreal', 'San Francisco'],
   value=['Montreal']
)
```

```python
dcc.Checklist(
   options=[
       {'label': 'New York City', 'value': 'New York City'},
       {'label': 'Montreal', 'value': 'Montreal'},
       {'label': 'San Francisco', 'value': 'San Francisco'},
   ],
   value=['Montreal']
)
```

```python
dcc.Checklist(
   options={
        'New York City': 'New York City',
        'Montreal': 'Montreal',
        'San Francisco': 'San Francisco'
   },
   value=['Montreal']
)
```

En estos ejemplos, la etiqueta de la opción (lo que ve el usuario) y el valor (lo que se pasa a el callback) son equivalentes. A menudo es útil que estén separados para que puedas cambiar fácilmente la etiqueta sin cambiar la lógica de callback que usa el valor:

```python
dcc.Checklist(
   options=[
       {'label': 'New York City', 'value': 'NYC'},
       {'label': 'Montreal', 'value': 'MTL'},
       {'label': 'San Francisco', 'value': 'SF'},
   ],
   value=['MTL']
)
```

```python
dcc.Checklist(
   options={
        'NYC': 'New York City',
        'MTL': 'Montreal',
        'SF': 'San Francisco'
   },
   value=['MTL']
)
```

Nota: Las versiones de Dash anteriores a la 2.1 solo admiten argumentos de palabras clave para opciones y valores, y también las opciones deben proporcionarse como una lista de diccionarios.

## Flexible Data Types

Hemos visto cómo se pueden configurar las **Options** de una lista de verificación usando una lista, un diccionario o una lista de diccionarios. **Options** también acepta estructuras de datos Pandas y NumPy.

En este ejemplo, utilizamos las columnas del DataFrame (df.columns) como **Options** de la lista de verificación.

```python
from dash import dcc
from plotly.express import data

df = data.medals_long()

dcc.Checklist(df.columns, df.columns[0:2].values)
```

Aquí configuramos **Options** con df.nation.unique(). Este método de Pandas devuelve valores únicos en la columna 'nación'. Al pasarlo a **Options**, nuestra lista de verificación muestra todos los valores únicos en esa columna.

```python
from dash import dcc
from plotly.express import data

df = data.medals_long()

dcc.Checklist(df.nation.unique(), df.nation.unique()[0:2])
```

## Components as Option Labels

Esta función está disponible en Dash 2.5 y versiones posteriores.

En ejemplos anteriores, configuramos etiquetas de opciones como cadenas. También puedes usar componentes Dash como etiquetas de opciones. En este ejemplo, cada etiqueta es una lista de componentes que contienen un **html.Img** y texto en un **html.Span**.

```python
from dash import dcc, html

dcc.Checklist(
    [
        {
            "label": [
                html.Img(src="/assets/images/language_icons/python_50px.svg"),
                html.Span("Python", style={"font-size": 15, "padding-left": 10}),
            ],
            "value": "Python",
        },
        {
            "label": [
                html.Img(src="/assets/images/language_icons/julia_50px.svg"),
                html.Span("Julia", style={"font-size": 15, "padding-left": 10}),
            ],
            "value": "Julia",
        },
        {
            "label": [
                html.Img(src="/assets/images/language_icons/r-lang_50px.svg"),
                html.Span("R", style={"font-size": 15, "padding-left": 10}),
            ],
            "value": "R",
        },
    ],
    labelStyle={"display": "flex", "align-items": "center"},
)

```

## Styling Components as Option Labels

Esta función está disponible en Dash 2.5 y versiones posteriores.

También puede diseñar etiquetas usando un componente **html.Div** para cada etiqueta y luego configurando estilos usando la propiedad **style**:

```python
from dash import dcc, html

dcc.Checklist(
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
    ], value=['Montreal'],
    labelStyle={"display": "flex", "align-items": "center"},
)

```

https://dash.plotly.com/dash-core-components/checklist
