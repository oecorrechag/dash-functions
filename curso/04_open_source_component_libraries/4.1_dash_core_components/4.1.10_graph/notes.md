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

## Using the Low-Level Interface with Dicts & Lists

Lea (1) más arriba para obtener más información sobre la diferencia entre px, go.Figure y diccionarios y listas.

```python
from dash import dcc

dcc.Graph(
    figure={
        'data': [
            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
        ],
        'layout': {
            'title': 'Dash Data Visualization'
        }
    }
)
```

## Interactive Graphing with Callbacks

Visualizaciones interactivas en los conceptos básicos de Dash explica cómo capturar eventos de interacción del usuario con un **dcc.Graph** y cómo actualizar la propiedad de la figura en los callbacks.

Algunas funciones avanzadas están documentadas en las publicaciones del foro de la comunidad:

    - Cómo conservar el estado de la interfaz de usuario (nivel de zoom, etc.) de un gráfico al actualizar el gráfico en un callback https://community.plot.ly/t/preserving-ui-state-like-zoom-in-dcc-graph-with-uirevision/15793
    - Transiciones de gráficos para transiciones suaves o animaciones en las actualizaciones de gráficos https://community.plot.ly/t/exploring-a-transitions-api-for-dcc-graph/15468

## Controlling the Plotly.js Version Used by dcc.Graph

- El componente dcc.Graph aprovecha la biblioteca Plotly.js para generar visualizaciones.
- En Dash 2.13 y versiones posteriores, el componente dcc.Graph utiliza la versión de la biblioteca Plotly.js en la versión de Plotly.py que haya instalado. Cada versión de Dash anterior a la 2.13 incluía su propia versión de Plotly.js.
- Si desea utilizar una versión diferente de Plotly.js en Dash 2.13 o versiones posteriores, puede utilizar una versión diferente de Plotly.py. Consulte la página de versiones de Plotly.py para obtener más detalles sobre qué versión de Plotly.js se incluyó con cada versión.
- En todas las versiones de Dash, también puede anular la versión de Plotly.js colocando un paquete de Plotly.js en el directorio de activos.
- Esta técnica se puede utilizar para:


    - Aprovecha las nuevas características de una versión de Plotly.js que sea más reciente que la que está
    incluida en la versión instalada actualmente de Dash, Plotly.py o Dash Design Kit.
    - Aprovecha el comportamiento más deseable de una versión de Plotly.js que sea menos reciente que la que está incluida en la versión instalada actualmente de Dash, Plotly.py o Dash Design Kit. Nos esforzamos por hacer que las versiones de Plotly.js sean completamente compatibles con versiones anteriores, por lo que no deberías tener que hacer esto muy a menudo.
    - Utiliza un paquete parcial de Plotly.js distribuido por Plotly o un paquete de Plotly.js personalizado que solo incluya el subconjunto de características de Plotly.js que usa tu aplicación Dash. Los paquetes parciales son más pequeños que los paquetes completos de Plotly.js que vienen con el componente Graph y Plotly.py y, por lo tanto, pueden mejorar el tiempo de carga de tu aplicación.

## LaTeX

**dcc.Graph** admite la representación de LaTeX en títulos, etiquetas y anotaciones. Utiliza la versión 3.2 de MathJax y se puede habilitar configurando mathjax=True en el componente. Coloque el contenido que se representará con MathJax entre los delimitadores $. Si necesita un $ literal, utilice la entidad HTML &#36;. Para incluir texto dentro de los delimitadores de MathJax, utilice \text{<your_text_goes_here>}. En el siguiente ejemplo (radio solar) se incluye como texto en el eje y_título.

```bash
1.laTeX.py
```

## Graph Resizing and Responsiveness

Hay varias opciones que puedes aprovechar si quieres que el tamaño de tu gráfico sea reactivo.

El comportamiento predeterminado de plotly.js dicta que el gráfico debe cambiar de tamaño al cambiar el tamaño de la ventana. Sin embargo, en algunos casos, es posible que quieras cambiar el tamaño del gráfico en función del tamaño de su contenedor principal. (Puedes establecer el tamaño del contenedor principal con las propiedades style.height y style.width).

La propiedad responsive del componente dcc.Graph te permite definir el comportamiento deseado. En resumen, acepta como valor True, False o 'auto':

    - **True** fuerza al gráfico a responder al cambio de tamaño de la ventana y del elemento primario, independientemente de cualquier otra especificación en figure.layout o config
    - **False** fuerza al gráfico a no responder al cambio de tamaño de la ventana y del elemento primario, independientemente de cualquier otra especificación en figure.layout o config
    - **'auto'** conserva el comportamiento heredado (el tamaño y la capacidad de cambio de tamaño se determinan mediante los valores especificados en figure.layout y config.responsive)

## How Resizing Works - Advanced

Las propiedades de dcc.Graph que pueden controlar el tamaño del gráfico (además de ser responsivo) son:

- figure.layout.height: establece explícitamente la altura
- figure.layout.width: establece explícitamente el ancho
- figure.layout.autosize: si es Verdadero, establece la altura y el ancho del gráfico al de su contenedor principal
- config.responsive: si es Verdadero, cambia la altura y el ancho del gráfico al cambiar el tamaño de la ventana.

La propiedad responsive funciona junto con las propiedades anteriores de la siguiente manera:

- **True**: config.responsive y figure.layout.autosize se reemplazan con valores Verdaderos, y figure.layout.height y figure.layout.width no están configurados
- **False**: config.responsive y figure.layout.autosize se reemplazan con valores Falso
- **'auto'**: la redimensionabilidad del gráfico se determina de la misma manera que antes (es decir, con las cuatro propiedades anteriores)








```python

```
