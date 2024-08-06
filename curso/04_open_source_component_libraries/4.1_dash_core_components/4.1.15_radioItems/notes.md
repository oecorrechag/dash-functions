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





```python

```