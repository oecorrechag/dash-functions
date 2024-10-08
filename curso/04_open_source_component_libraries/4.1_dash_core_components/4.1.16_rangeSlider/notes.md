# dcc.RangeSlider

**dcc.RangeSlider** es un componente para representar un control deslizante de rango. Los usuarios interactúan con un **dcc.RangeSlider** seleccionando áreas en el riel o arrastrando controladores.

Los puntos que se muestran en un **dcc.RangeSlider** se denominan marcas. En Dash 2.1 y versiones posteriores, se generan automáticamente si no se proporcionan explícitamente o se desactivan.

## Simple RangeSlider Example

Un ejemplo de un dcc.RangeSlider simple vinculado a una devolución de llamada. El callback toma el rango seleccionado actualmente de dcc.RangeSlider y lo envía a un html.Div.

```bash
1.simple_rangeSlider.py
```

## Min, Max, and Step

En el ejemplo anterior, los tres primeros argumentos proporcionados (0, 20 y 1) son min, max y step respectivamente.

min establece un valor mínimo disponible para la selección en dcc.RangeSlider, max establece un máximo y step define los puntos para dcc.RangeSlider entre el min y el max.

dcc.RangeSlider acepta estos tres argumentos como argumentos posicionales, pero también puede proporcionarlos como argumentos de palabras clave. Si se utilizan argumentos de palabras clave, el mismo código del componente dcc.RangeSlider se ve así:

```python
dcc.RangeSlider(min=0, max=20, step=1, value=[5, 15], id='my-range-slider'),
```

## Auto Generated Marks

De forma predeterminada, el componente dcc.RangeSlider agrega marcas si no se especifican, como en el ejemplo anterior. Utiliza el mínimo y el máximo y las marcas corresponden al paso si se utiliza uno.

Si no se proporciona el paso, RangeSlider calcula automáticamente un paso y agrega alrededor de cinco marcas. Las etiquetas para las marcas generadas automáticamente tienen formato de unidad SI.

```python
from dash import dcc

dcc.RangeSlider(0, 20, value=[5, 15])
```

## Turn Off Marks

Puedes desactivar las marcas configurando marks=None:

```python
from dash import dcc

dcc.RangeSlider(0, 20, marks=None, value=[5, 15])
```

## Custom Marks

También puede definir marcas personalizadas. Si se definen las marcas y el paso se establece en Ninguno, entonces **dcc.RangeSlider** solo podrá seleccionar valores que hayan sido predefinidos por las marcas. Tenga en cuenta que el valor predeterminado es paso=1, por lo que debe especificar explícitamente Ninguno para obtener este comportamiento. Las marcas son un diccionario donde las claves representan los valores numéricos y los valores representan sus etiquetas.

```python
from dash import dcc

dcc.RangeSlider(
    min=0,
    max=10,
    step=None,
    marks={
        0: '0°F',
        3: '3°F',
        5: '5°F',
        7.65: '7.65°F',
        10: '10°F'
    },
    value=[3, 7.65]
)
```

## Included and Styling Marks

De forma predeterminada, included=True, lo que significa que se resaltará el riel que se encuentra detrás del controlador. Para que el controlador actúe como un valor discreto, configure included=False. Para aplicar estilo a las marcas, incluya un atributo CSS de estilo junto con el valor clave.

```python
from dash import dcc

# RangeSlider has included=True by default
dcc.RangeSlider(0, 100, value=[10, 65], marks={
        0: {'label': '0°C', 'style': {'color': '#77b0b1'}},
        26: {'label': '26°C'},
        37: {'label': '37°C'},
        100: {'label': '100°C', 'style': {'color': '#f50'}}
    }
)
```

## Multiple Handles

Para crear varios identificadores, defina más valores para el valor.

```python
from dash import dcc

dcc.RangeSlider(0, 30, value=[1, 3, 4, 5, 12, 17])
```

## Pushable Handles

La propiedad **pushable** es un valor booleano o numérico. El valor numérico determina la distancia mínima entre los controladores. 

```python
from dash import dcc

dcc.RangeSlider(0, 30, value=[8, 10, 15, 17, 20], pushable=2)
```

## Non-Crossing Handles

Para evitar que los controladores se crucen entre sí, configure allowCross=False.

```python
from dash import dcc

dcc.RangeSlider(0, 30, value=[10, 15], allowCross=False)
```

## Non-Linear Slider and Updatemode

Cree un control deslizante logarítmico configurando las marcas para que sean logarítmicas y ajustando el valor de salida del control deslizante en los callbacks. La propiedad updatemode nos permite determinar cuándo queremos que se active un callback. El siguiente ejemplo tiene updatemode='drag', lo que significa que se activa un callback cada vez que se mueve el controlador. Compare la salida del callback con el primer ejemplo de esta página para ver la diferencia.

```bash
2.slider_and_updatemode.py
```

## Tooltips

La propiedad **tooltips** se puede utilizar para mostrar el valor actual. El parámetro **placement** controla la posición de la información sobre herramientas, es decir, 'left', 'right', 'top', 'bottom' y se utiliza always_visible=True. En ese caso, la información sobre herramientas se mostrará siempre; de ​​lo contrario, solo se mostrará cuando se pase el cursor sobre ella.

```python
from dash import dcc

dcc.RangeSlider(0, 30, value=[10, 15],
                tooltip={"placement": "bottom", "always_visible": True})
```

## Styling Tooltips

Puede personalizar el estilo de las descripciones emergentes con el parámetro tooltip.style. Este acepta un diccionario de estilos para aplicar. En este ejemplo, configuramos el color del texto y el tamaño de la fuente.

```python
from dash import dcc

dcc.RangeSlider(0, 30,
    value=[5, 15],
    marks=None,
    tooltip={
        "placement": "bottom",
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

```python
from dash import dcc

dcc.RangeSlider(
    0,
    10,
    value=[3, 7.65],
    marks={0: "0°F", 3: "3°F", 5: "5°F", 7.65: "7.65°F", 10: "10°F"},
    tooltip={"always_visible": True, "transform": "temperatureInCelsius"},
)
```

## Formatting Tooltips

Puede personalizar el texto que se muestra en las descripciones emergentes mediante el parámetro tooltip.template. Este acepta una cadena, que debe contener {value}. El {value} se reemplazará con la representación en cadena del valor de la descripción emergente, o con el valor devuelto por una función de transformación si se especificó una mediante tooltip.transform (consulte la sección anterior).

```python
from dash import dcc

dcc.RangeSlider(0, 30,
    value=[5, 15],
    marks=None,
    tooltip={
        "always_visible": True,
        "template": "$ {value}"
    },
),
```
