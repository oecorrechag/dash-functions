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





