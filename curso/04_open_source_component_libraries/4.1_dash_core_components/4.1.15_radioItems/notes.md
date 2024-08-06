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

