# dcc.Slider

**dcc.Slider** es un componente para renderizar un control deslizante. Los usuarios interactúan con un **dcc.Slider** seleccionando áreas en el riel o arrastrando el controlador.

Los puntos que se muestran en un control deslizante se denominan marcas. Se generan automáticamente si no se proporcionan explícitamente o se desactivan.

## Simple Slider Example

Un ejemplo de un control deslizante simple vinculado a un callback. El callback toma el valor seleccionado actualmente del control deslizante y lo envía a un html.Div.

```bash
1.slider_example.py
```

## Min, Max, and Step

min, max y step son los tres primeros argumentos posicionales en el ejemplo anterior. min establece un valor mínimo disponible para la selección en el control deslizante, max establece un máximo y step define los puntos del control deslizante entre el mínimo y el máximo. También se pueden utilizar argumentos de palabras clave. Estos ejemplos de definición de un dcc.Slider son equivalentes:

```python
dcc.Slider(0, 20, 5, value=10, id='my-slider')
```

```python
dcc.Slider(min=0, max=20, step=5, value=10, id='my-slider')
```

```python
dcc.Slider(id='my-slider', value=10, min=0, max=20, step=5)
```

```python
dcc.Slider(min=0, max=20, step=5, value=10, id='my-slider')
```

## Auto Generated Marks

De forma predeterminada, el componente dcc.Slider agrega marcas si no se especifican, como en el ejemplo anterior. Utiliza el mínimo y el máximo y las marcas corresponden al paso si se utiliza uno.

Si no se proporciona el paso, Slider calcula automáticamente un paso y agrega alrededor de cinco marcas. Las etiquetas para las marcas generadas automáticamente tienen el formato de unidad SI.

```python
from dash import dcc

dcc.Slider(0, 20)
```

## Custom Marks

También puedes definir marcas. Si se definen las marcas del control deslizante y el paso se establece en Ninguno, el control deslizante solo podrá seleccionar valores que hayan sido predefinidos por las marcas. Ten en cuenta que el valor predeterminado es paso=1, por lo que debes especificar explícitamente Ninguno para obtener este comportamiento. Las marcas son un diccionario donde las claves representan los valores numéricos y los valores representan sus etiquetas.

```python
from dash import dcc

dcc.Slider(0, 10,
    step=None,
    marks={
        0: '0°F',
        3: '3°F',
        5: '5°F',
        7.65: '7.65°F',
        10: '10°F'
    },
    value=5
)
```

## Turn Off Marks

Puede desactivar las marcas del control deslizante configurando marks=None:

```python
from dash import dcc

dcc.Slider(0, 20, marks=None, value=10)
```

## Included and Styling Marks

De forma predeterminada, included=True, lo que significa que se resaltará el riel que se encuentra detrás del controlador. Para que el controlador actúe como un valor discreto, configure included=False. Para aplicar estilo a las marcas, incluya un atributo CSS de estilo junto con el valor clave.

```python
from dash import dcc

# Slider has included=True by default
dcc.Slider(0, 100, value=65,
    marks={
        0: {'label': '0°C', 'style': {'color': '#77b0b1'}},
        26: {'label': '26°C'},
        37: {'label': '37°C'},
        100: {'label': '100°C', 'style': {'color': '#f50'}}
    }
)
```

```python
from dash import dcc

dcc.Slider(0, 100, value=65,
    marks={
        0: {'label': '0°C', 'style': {'color': '#77b0b1'}},
        26: {'label': '26°C'},
        37: {'label': '37°C'},
        100: {'label': '100°C', 'style': {'color': '#f50'}}
    },
    included=False
)
```

## Non-Linear Slider and Updatemode

```bash
2.slider_and_updatemode.py
```

## Slider Tooltips

La propiedad tooltips se puede utilizar para mostrar el valor actual. El parámetro placement controla la posición de la información sobre herramientas, es decir, 'izquierda', 'derecha', 'arriba', 'abajo'. Si se utiliza always_visible=True, la información sobre herramientas se mostrará siempre; de ​​lo contrario, solo se mostrará cuando se pase el cursor sobre ella.

```python
from dash import dcc

dcc.Slider(0, 10, 1, value=5, marks=None,
    tooltip={"placement": "bottom", "always_visible": True})
```

## Styling Tooltips

Puede personalizar el estilo de las descripciones emergentes con el parámetro tooltip.style. Este acepta un diccionario de estilos para aplicar. En este ejemplo, configuramos el color del texto y el tamaño de la fuente.

```python
from dash import dcc

dcc.Slider(0, 10,
    1,
    value=5,
    marks=None,
    tooltip={
        "always_visible": True,
        "style": {"color": "LightSteelBlue", "fontSize": "20px"},
    },
),
```

## Transforming Tooltip Values

Puede transformar el valor que se muestra en una información sobre herramientas mediante una función de JavaScript especificando el nombre de la función con el parámetro tooltip.transform.

Para que una función personalizada esté disponible en su aplicación, agréguela a un archivo en la carpeta de recursos de su aplicación. La función debe estar disponible en el espacio de nombres window.dccFunctions.

En este ejemplo, tenemos una función que convierte las temperaturas en grados Fahrenheit a grados Celsius. Esta función se guarda en assets/tooltip.js:

```javascript
window.dccFunctions = window.dccFunctions || {};
window.dccFunctions.temperatureInCelsius = function(value) {
     return ((value - 32) * 5/9).toFixed(2);
}
```

Luego pasamos este nombre de función al parámetro tooltip.transform:

```python
from dash import dcc

dcc.Slider(
    0,
    10,
    step=None,
    marks={0: "0°F", 3: "3°F", 5: "5°F", 7.65: "7.65°F", 10: "10°F"},
    value=5,
    tooltip={"always_visible": True, "transform": "temperatureInCelsius"},
)
```

## Formatting Tooltips





```python

```

