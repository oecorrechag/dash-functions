# dcc.Dropdown

**dcc.Dropdown** es un componente que crea un menú desplegable personalizable para seleccionar uno o varios elementos de una lista de opciones.

## Basic Dropdown

Para crear un menú desplegable básico, proporcione opciones y un valor a **dcc.Dropdown** en ese orden.

```bash
1.basic_dropdown.py
```

## Options and Value

Las propiedades de opciones y valor son los dos primeros argumentos de **dcc.Dropdown**. Existen múltiples formas de configurar opciones. Los siguientes ejemplos definen el mismo menú desplegable:

```python
dcc.Dropdown(['New York City', 'Montreal', 'San Francisco'], 'Montreal')
```

```python
dcc.Dropdown(
   options=['New York City', 'Montreal', 'San Francisco'],
   value='Montreal'
)
```

```python
dcc.Dropdown(
   options=[
       {'label': 'New York City', 'value': 'New York City'},
       {'label': 'Montreal', 'value': 'Montreal'},
       {'label': 'San Francisco', 'value': 'San Francisco'},
   ],
   value='Montreal'
)
```

```python
dcc.Dropdown(
   options={
        'New York City': 'New York City',
        'Montreal': 'Montreal',
        'San Francisco': 'San Francisco'
   },
   value='Montreal'
)
```

En estos ejemplos, la etiqueta de la opción (lo que ve el usuario) y el valor (lo que se pasa a el callback) son equivalentes. A menudo resulta útil que estén separados para poder cambiar fácilmente la etiqueta sin cambiar la lógica de la devolución de llamada que utiliza el valor:

```python
dcc.Dropdown(
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
dcc.Dropdown(
   options=[
       {'label': 'New York City', 'value': 'NYC'},
       {'label': 'Montreal', 'value': 'MTL'},
       {'label': 'San Francisco', 'value': 'SF'},
   ],
   value='MTL'
)
```

## Multi-Value Dropdown

Un componente desplegable con la propiedad **multi** establecida en **True** permitirá al usuario seleccionar más de un valor a la vez.

```python
from dash import dcc

dcc.Dropdown(
    ['New York City', 'Montreal', 'San Francisco'],
    ['Montreal', 'San Francisco'],
    multi=True
)
```

## Disable Search

La propiedad de **searchable** está configurada en **True** de manera predeterminada en todos los componentes dcc.Dropdown. Para evitar buscar el valor del menú desplegable, simplemente configure la propiedad de búsqueda en Falso. Intente buscar "Nueva York" en este menú desplegable a continuación y compárelo con los otros menús desplegables de la página para ver la diferencia.

```python
from dash import dcc

dcc.Dropdown(
    ['New York City', 'Montreal', 'San Francisco'],
    searchable=False
)
```

## Dropdown Clear

La propiedad **clearable** está configurada en True de forma predeterminada en todos los componentes dcc.Dropdown. Para evitar que se borre el valor del menú desplegable seleccionado, simplemente configure la propiedad clearable en False

```python
from dash import dcc

dcc.Dropdown(
    ['New York City', 'Montreal', 'San Francisco'],
    'Montreal',
    clearable=False
)
```

## Placeholder Text

La propiedad de **placeholder** le permite definir el texto predeterminado que se muestra cuando no se selecciona ningún valor.

```python
from dash import dcc

dcc.Dropdown(
    ['New York City', 'Montreal', 'San Francisco'],
    placeholder="Select a city",
)
```

## Disable Dropdown

Para deshabilitar el menú desplegable, simplemente configure **disabled** en Verdadero.

```python
from dash import dcc

dcc.Dropdown(
    ['New York City', 'Montreal', 'San Francisco'],
    disabled=True
)
```

## Disable Options

Para deshabilitar una opción particular dentro del menú desplegable, configure la propiedad deshabilitada en las opciones.

```python
from dash import dcc

dcc.Dropdown([
        {'label': 'New York City', 'value': 'NYC', 'disabled': True},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF', 'disabled': True}])

```

## Dynamic Options

Este es un ejemplo de cómo actualizar las opciones en el servidor según los términos de búsqueda que escriba el usuario. Por ejemplo, las opciones están vacías en la primera carga, tan pronto como comience a escribir, se cargarán con los valores correspondientes.


```bash
2.dynamic_options.py
```

## Flexible Data Types

Hemos visto cómo se pueden configurar las opciones mediante una lista, un diccionario o una lista de diccionarios. options también acepta estructuras de datos de Pandas y NumPy.

En este ejemplo, usamos las columnas de DataFrame (df.columns) como opciones del menú desplegable.

```bash
3.flexible_data_types.py
```

Aquí, configuramos las opciones con df.nation.unique(). Este método de Pandas devuelve valores únicos en la columna "nation". Al pasarlo a las opciones, nuestro menú desplegable muestra todos los valores únicos en esa columna.

```bash
4.flexible_data_types.py
```

## Components as Option Labels

En los ejemplos anteriores, hemos establecido las etiquetas de opciones como cadenas. También puedes usar componentes Dash como etiquetas de opciones. En este ejemplo, cada etiqueta es un componente html.Span con un componente html.Img y algo de texto dentro.

```bash
5.components_as_option_labels.py
```

## Styling Components as Option Labels

También puedes diseñar etiquetas utilizando un componente **html.Span** para cada etiqueta y luego configurando estilos utilizando la propiedad de estilo:

```python
from dash import dcc, html

dcc.Dropdown(
    [
        {
            "label": html.Span(['Montreal'], style={'color': 'Gold', 'font-size': 20}),
            "value": "Montreal",
        },
        {
            "label": html.Span(['NYC'], style={'color': 'MediumTurqoise', 'font-size': 20}),
            "value": "NYC",
        },
        {
            "label": html.Span(['London'], style={'color': 'LightGreen', 'font-size': 20}),
            "value": "London",
        },
    ], value='Montreal'
)
```

## Custom Search Values

Cuando se utilizan componentes como etiquetas de opciones, la búsqueda del menú desplegable utiliza los valores de las opciones de forma predeterminada. Puede agregar una cadena adicional para la búsqueda configurando la propiedad de búsqueda de una opción. Aquí configuramos un valor de búsqueda para cada opción para que coincida con el texto de la etiqueta de esa opción.

El valor proporcionado para la búsqueda se suma al valor de la opción. Por ejemplo, la opción 2 se muestra cuando un usuario busca "NYC" o "New York City".

```python
from dash import dcc, html

dcc.Dropdown(
    [
        {
            "label": html.Span(['Montreal'], style={'color': 'Gold', 'font-size': 20}),
            "value": "MTL",
            "search": "Montreal"
        },
        {
            "label": html.Span(['New York City'], style={'color': 'MediumTurqoise', 'font-size': 20}),
            "value": "NYC",
            "search": "New York City"
        },
        {
            "label": html.Span(['London'], style={'color': 'LightGreen', 'font-size': 20}),
            "value": "LON",
            "search": "London"
        },
    ], value='Montreal',
)
```

## Dropdown Height

La altura de un menú desplegable expandido es de 200 px de manera predeterminada. Las opciones que se ajustan a esta altura son visibles en la pantalla, mientras que se puede acceder a las opciones restantes mediante la barra de desplazamiento vertical del menú desplegable. Puede cambiar la altura con maxHeight si desea que se vean más o menos opciones cuando se expande el menú desplegable. En este ejemplo, la configuramos en 300 px.

```python
from dash import dcc

dcc.Dropdown(
    ['New York City', 'Montreal', 'Paris', 'London', 'Amsterdam', 'Berlin', 'Rome'],
    'Paris', id='height-example-dropdown', maxHeight=300
)
```

## Option Height

Puedes cambiar la altura de las opciones en el menú desplegable configurando optionHeight. En este ejemplo, la configuramos en 50 px. El valor predeterminado es 35 px.

```python
from dash import dcc

dcc.Dropdown(
    ['New York City', 'Montreal', 'Paris', 'London', 'Amsterdam', 'Berlin', 'Rome'],
    'Paris', id='option-height-example-dropdown', optionHeight=50
)
```
