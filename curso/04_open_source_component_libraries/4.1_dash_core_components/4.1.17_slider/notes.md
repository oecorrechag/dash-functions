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




```python

```

