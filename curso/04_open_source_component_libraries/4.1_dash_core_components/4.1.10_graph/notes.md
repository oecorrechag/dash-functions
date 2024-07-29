# dcc.Graph

El componente **dcc.Graph** se puede utilizar para representar cualquier visualización de datos impulsada por gráficos, pasada como argumento de **figure**.

## Primer on Plotly Graphing Library

- La biblioteca de gráficos Plotly, conocida como el paquete plotly, genera "figures". Estas se utilizan en **dcc.Graph**, por ejemplo, **dcc.Graph(figure=fig)** con **fig** una figura plotly.

- Para comenzar a utilizar plotly, aprenda cómo está organizada su documentación:

    1. Aprenda la arquitectura de la figura: https://plotly.com/python/creating-and-updating-figures/
    2. Cada tipo de gráfico tiene un conjunto de ejemplos en una URL única. Familiarícese con la estructura de estas páginas. Google es su amigo. Por ejemplo, "Histogramas en Python" está documentado en https://plotly.com/python/histograms
    3. Plotly Express es la interfaz de alto nivel recomendada. Comprenda dónde encaja leyendo el punto 1. Una vez que comprenda su estructura, puede ver todos los argumentos en la página "Referencia de API" documentada aquí: https://plotly.com/python-api-reference/plotly.express.html
    4. Cada aspecto de un gráfico es configurable. Lea el punto 1 para comprender la interfaz de la figura de bajo nivel y cómo modificar las propiedades de una figura generada. Una vez que la comprenda, vea todas las propiedades visitando la página "Referencia de la figura" en https://plotly.com/python/reference.
    5. Si no puede generar el gráfico fácilmente con px, aprenda la estructura graph_objects leyendo 1 y comprendiendo la estructura de la figura a través de https://plotly.com/python/reference

- Plotly admite entre 40 y 50 tipos de gráficos diferentes. Obtenga más información en https://plotly.com/python/.
- Durante el desarrollo, puede crear figuras ejecutando aplicaciones de Dash o en otros entornos como Jupyter, su consola y más. Si está utilizando la interfaz fuera de Dash, al llamar a **fig.show()** siempre se mostrará el gráfico (ya sea en su navegador o directamente en línea en su entorno).
- Para ver todos estos entornos de renderizado, consulte https://plotly.com/python/renderers/.

## Plotly Express in Dash

El objeto fig se pasa directamente a la propiedad **figure** de dcc.Graph:

```python
from dash import dcc
import plotly.express as px

df = px.data.iris()  # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")

dcc.Graph(figure=fig)

```

## Using the Low-Level Interface with go.Figure

Uso de la interfaz de bajo nivel con go.Figure

Lea el punto (1) anterior para obtener más información sobre la diferencia entre px y go.Figure.

```python
from dash import dcc
import plotly.graph_objs as go

fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])

dcc.Graph(figure=fig)

```











```python

```
