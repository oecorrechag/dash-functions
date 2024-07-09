# Partial Property Updates

La mayoría de los ejemplos de callbacks que hemos visto en capítulos anteriores actualizaron una propiedad completa cuando se ejecutó el callback. En los casos en los que solo queremos actualizar una pequeña parte de una propiedad, por ejemplo, el título de un gráfico, esto es ineficiente. Significa que todos los datos de la propiedad (la figura completa en este caso) se envían de vuelta a través de la red, aunque la mayoría de los datos no hayan cambiado. Mejore el rendimiento de su aplicación realizando actualizaciones parciales de propiedades cuando no se requiera una actualización completa.

## The Dash Patch Class

Las actualizaciones de propiedades parciales utilizan la clase Patch, con la que puede importar desde Dash Import Patch. Cree una instancia de un objeto Patch en un callback para realizar actualizaciones parciales en la salida de un callback. Este objeto Patch define los cambios que se deben realizar en la propiedad. Los posibles cambios incluyen asignar un nuevo valor, fusionar un diccionario y agregar un elemento a una lista. Las operaciones están definidas por el objeto Patch dentro de su callback, pero se ejecutan en el cliente del navegador en la interfaz de Dash.

## Updating Title Color with a Partial Update

A continuación se muestra un ejemplo del uso de un Path para actualizar solo el color de fuente del título del gráfico:

```bash
1.updating_color.py
```

Echemos un vistazo más de cerca a lo que está sucediendo aquí:

1. Primero, importamos la clase Patch:

```python
from dash import Patch
```

2. Definimos nuestras entradas y salidas de callback de la misma manera que con una callback estándar:

```python
@callback(
    Output('my-fig', 'figure'),
    Input('update-color-button-2', 'n_clicks')
)
```

3. En nuestra callback, creamos un objeto Patch. Aquí lo llamamos patched_figure, pero el nombre es arbitrario. Esta figura_parcheada definirá los cambios que Dash debe realizar en la figura.

```python
patched_figure = Patch()
```

4. Luego, definimos un cambio de asignación, diciéndole a Dash que queremos que esta parte de la figura sea el valor en new_color.

```python
patched_figure['layout']['title']['font']['color'] = new_color
```

5. Devolvemos nuestra figura_parcheada:

```python
return patched_figure
```

Una vez que el callback devuelve el objeto Patch, en la interfaz, Dash asigna el valor en new_color a ['layout']['title']['font']['color'] en la figura.

En este ejemplo, actualizamos el color de fuente del título indicándole a Dash que actualice ['layout']['título']['fuente']['color'] en la figura. Para obtener más detalles sobre cómo explorar los atributos de propiedad de una figura de objetos gráficos, consulte la sección "Exploración de la estructura de propiedades" a continuación.

```bash
2.updating_color.py
```

## Performance

Veamos la diferencia al realizar una actualización parcial en lugar de una actualización completa. El gráfico de nuestro ejemplo anterior utiliza un pequeño conjunto de datos de 150 filas. Aquí la diferencia de tamaño es relativamente pequeña: 9,5 kB para la actualización completa frente a 380 B para la actualización parcial.

## Partial Update Methods

Hay varias formas de utilizar objetos Patch para realizar actualizaciones parciales.

Aunque todos los métodos descritos a continuación siempre están disponibles cuando se utiliza un objeto Patch, no funcionarán con todas las propiedades o tipos de atributos. Por ejemplo, anteponer, ampliar y anexar funcionan con listas, mientras que la actualización funciona con diccionarios. Consulte la sección Exploración de la estructura de las propiedades a continuación para obtener más detalles sobre cómo comprender la propiedad que está actualizando.

### Assign

En el ejemplo anterior, también se puede utilizar la notación de puntos. Entonces podrías asignar new_color de esta manera:

```python
patched_figure.layout.title.font.color = new_color
```

#### Examples of Assigning New Data

En este ejemplo, actualizamos los valores en el eje y según la selección desplegable

```bash
3.assign.py
```

Aquí hay otro ejemplo. Aquí actualizamos el color del marcador según los valores seleccionados en un menú desplegable. En este ejemplo, verificamos qué valores ha seleccionado el usuario y luego devolvemos una lista con el color de esos puntos de datos en rojo y cualquier otro punto de datos en azul.

```bash
4.assign.py
```

### Append

Patch tiene un método de Append que puede usar para agregar atributos de propiedad que son listas. Funciona como agregar a una lista en Python, agregando el elemento al final. Es útil para agregar elementos secundarios a un componente y para agregar datos a los ejes de una figura.

### Example with X and Y Axes of a Graph

Al agregar a las matrices de datos X e Y de un gráfico, podemos agregar puntos de datos adicionales. En este ejemplo, comenzamos con un gráfico sin datos y lo agregamos a los ejes X e Y cada vez que se selecciona el botón.

```bash
5.append.py
```

### Example of Append with Pattern-Matching Callbacks

Con los callbacks de coincidencia de patrones, podemos agregar contenido dinámicamente a nuestro diseño. A menudo, querremos agregar elementos secundarios a un componente. En este ejemplo, los elementos secundarios de 'dropdown-container-2' comienzan como una lista vacía. Cada vez que se ejecuta la devolución de llamada display_dropdowns, se agrega un nuevo menú desplegable a los elementos secundarios de 'dropdown-container-2' usando un objeto Patch.

```bash
6.append.py
```

## Prepend

El método Prepend agrega el valor proporcionado al inicio de la lista. Aquí anteponemos los ejes X e Y.

```bash
7.prepend.py
```

## Extend

El método Extend funciona como extender una lista en Python. Úselo proporcionando un iterable cuyos valores se agregarán al final de la lista.

```bash
8.extend.py
```

- Maximum Number of Values

Cada vez que amplía una lista, se agrega a los datos existentes. Actualmente no es posible limitar el número máximo de valores en la lista. Esto es algo que esperamos apoyar en el futuro. Para hacer esto actualmente, deberá usar la asignación y reemplazar la lista completa por una nueva con la cantidad exacta de valores que desee.

### Example with a Dataframe

Aquí hay otro ejemplo del uso de Extend. En este ejemplo, agregamos filas de un marco de datos a los datos de una tabla de datos con cada clic (después de 10 clics dejamos de actualizar la tabla).

```bash
9.extend.py
```

## Insert

Utilice Insert para agregar a una lista en un índice específico. El método de inserción toma dos argumentos: el índice para insertar y los datos para agregar. En este ejemplo, agregamos "Producto B" después de "Producto A" insertando sus datos X e Y en el índice 1.

```bash
10.insert.py
```

## Reverse

Usando Reverse puedes invertir el orden de los elementos en una lista. Aquí, invertimos los datos en los ejes X e Y de la figura.

```bash
11.reverse.py
```

## Clear

Utilice Clear para eliminar todos los elementos de una lista. anotaciones es una lista de diccionarios en el diseño del gráfico. En este ejemplo, borramos la lista cuando se selecciona el botón. La próxima vez que se seleccione el botón volvemos a agregar las anotaciones.

```bash
12.clear.py
```

## Update

Para un atributo de propiedad que es un diccionario, puede utilizar el método de Update para fusionar otro diccionario en él. En este ejemplo, las opciones del componente RadioItems se crean como un diccionario. El diccionario inicial tiene tres pares clave-valor y, cuando se selecciona el botón, se fusionan en él tres pares clave-valor adicionales.

Nota: la actualización realiza una combinación de un solo nivel, no una combinación profunda.

```bash
13.update.py
```

## Delete

También puede realizar actualizaciones parciales que eliminen partes de los datos de una propiedad. En este ejemplo, eliminamos la primera fila de la tabla eliminando el elemento de datos en el índice 0:

```bash
14.delete.py
```

## Remove

También puede realizar actualizaciones parciales que eliminen partes de los datos de una propiedad que coincidan con un valor determinado. En este ejemplo, cuando se selecciona el botón, eliminamos todos los elementos de la Lista de verificación que están en la lista canandian_cities.

```bash
15.remove.py
```

## Math Operations

Patch también admite operaciones matemáticas, por ejemplo, para incrementar, disminuir, multiplicar y dividir valores. En este ejemplo, incrementamos el valor en el eje y cuando se selecciona una barra.

```bash
16.operations.py
```

## Method Summary

- Hay varias formas de utilizar objetos Patch para realizar actualizaciones parciales:

    - Listas: anteponer, extender, agregar, invertir, insertar, borrar, eliminar y asignar usando =
    - Diccionarios: actualización y asignación usando =
    - Cadenas: asignación usando =
    - Números: asignación usando =

- La ubicación de la actualización se puede especificar con corchetes o notación de puntos: por ejemplo, ambas son válidas:

```python
patched_figure = Patch()
patched_figure['layout']['title'] = 'New Title'
```

```python
patched_figure = Patch()
patched_figure.layout.title = 'New Title'
```

- Pero la notación de puntos no funciona para índices de listas, ya que sólo se puede utilizar con identificadores válidos de Python.

```python
patched_figure = Patch()
patched_figure['data'][0]['y'] = [1, 2, 3]
```

Reemplazar patched_figure['data'][0]['y'] = [1, 2, 3] con patched_figure.data.0.y = [1, 2, 3] en el ejemplo anterior no funcionaría.

## Combining Patch Methods


Puede combinar los diferentes Patch métodos mencionados anteriormente. En este ejemplo, usamos anteponer y agregar con el mismo objeto para actualizar el mismo atributo. Las operaciones se aplican en el orden en que se definen en el callback.

```bash
17.combining.py
```

## Using Patches on Multiple Outputs

Puede utilizar varios objetos Patch dentro de un callback. En este ejemplo, creamos un objeto Patch, patched_figure para agregarlo a los datos de la figura, y creamos otro objeto Patch, patched_table, para actualizar la propiedad de datos de DataTable.

```bash
18.multiple.py
```

## Allowing Duplicate Callback Outputs

A veces querrás actualizar el mismo par componente-propiedad desde múltiples salidas del callback. Por ejemplo, podría tener una salida de callback para actualizar el color de un gráfico y otra salida de callback para actualizar los datos. Puede hacer esto configurando enable_duplicate=True en cualquier salida que se use más de una vez.

También puedes usar enable_duplicate para realizar actualizaciones completas en una salida de callback y una actualización parcial en otra. En este ejemplo, al hacer clic en un botón se elimina la primera fila de datos. El segundo botón envía los datos completos al componente.

Cuando se utilizan salidas de callback duplicadas (con enable_duplicate=True), no se garantiza el orden en el que se actualizan las devoluciones de llamada que se ejecutan al mismo tiempo. Consulte Salidas de callback duplicadas.

```bash
19.duplicate.py
```

nota: falla

## Exploring the Structure of Properties

Para realizar actualizaciones parciales de una propiedad, es necesario conocer la estructura de la propiedad que desea actualizar. Para comprender la estructura de cualquier propiedad de componente, consulte los documentos de referencia correspondientes. Por ejemplo, encontrará los documentos de referencia para cada componente Dash Core al final de la página del componente. Por ejemplo, las propiedades desplegables.

## Graph Objects

Como hemos visto en los ejemplos anteriores, un gran uso para las actualizaciones parciales es actualizar partes individuales de los objetos Figura de objetos gráficos Plotly.py, que puede pasar al parámetro de figura de un componente dcc.Graph. A menudo, solo querrás actualizar un pequeño detalle de un gráfico, como un color, y evitar enviar todos los datos del gráfico al navegador.

Para hacer esto con éxito, necesitará comprender la estructura de una figura.

A continuación se muestra un ejemplo de la estructura de un objeto Figura simple.

```python
Figure({
    'data': [{'hovertemplate': 'x=%{x}<br>y=%{y}<extra></extra>',
              'legendgroup': '',
              'line': {'color': '#636efa', 'dash': 'solid'},
              'marker': {'symbol': 'circle'},
              'mode': 'lines',
              'name': '',
              'orientation': 'v',
              'showlegend': False,
              'type': 'scatter',
              'x': array(['a', 'b', 'c'], dtype=object),
              'xaxis': 'x',
              'y': array([1, 3, 2]),
              'yaxis': 'y'}],
    'layout': {'legend': {'tracegroupgap': 0},
               'template': '...',
               'title': {'font': {'color': 'red'}, 'text': 'sample figure'},
               'xaxis': {'anchor': 'y', 'domain': [0.0, 1.0], 'title': {'text': 'x'}},
               'yaxis': {'anchor': 'x', 'domain': [0.0, 1.0], 'title': {'text': 'y'}}}
})
```

En nuestro primer ejemplo de Patch anterior, asignamos un color al título.

```python
patched_figure['layout']['title']['font']['color'] = new_color
```

De manera similar, podríamos actualizar el texto del título, que actualmente está configurado en una figura de muestra:

```python
patched_figure['layout']['title']['text'] = "my new title text"
```

Al trabajar con una Figura, puedes ver su estructura imprimiéndola.

```python
fig = px.line(x=["a","b","c"], y=[1,3,2], title="sample figure")

fig.update_layout(
    title_font_color="red"
)
print(fig)
```

Consulte la página La estructura de datos de la figura en Python en los documentos de la Biblioteca gráfica para obtener más detalles.
https://plotly.com/python/figure-structure/?_gl=1*7ciodj*_gcl_au*NDI0OTg5ODAyLjE3MTkxODkyNjc.*_ga*MTY1OTIzMjc3NS4xNzE5MTg5MjY3*_ga_6G7EE0JNSC*MTcyMDQ4NTM0Ni40NC4xLjE3MjA0ODU4ODAuNjAuMC4w

## Limitations

- Un objeto Patch es una representación de la operación que se aplicará a parte de una propiedad de salida. No le da acceso a los valores de una propiedad. Por ejemplo, lo siguiente no funcionará:

```python
patch_output = Patch()
formatted_property = f"My prop: {patch_output["my_prop"]}"
```

Si necesita acceder al valor de la propiedad, utilice Estado en su callback.

- El parche no está disponible en los callbacks del lado del cliente.

- Cada vez que amplías una lista, se agrega a los datos existentes. Actualmente no es posible limitar el número máximo de valores en la lista.
