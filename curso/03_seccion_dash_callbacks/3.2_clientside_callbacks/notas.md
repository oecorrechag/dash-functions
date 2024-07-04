# Clientside Callbacks

A veces, los callbacks pueden generar una sobrecarga significativa, especialmente cuando:

- recibir y/o devolver cantidades muy grandes de datos (tiempo de transferencia)
- se llaman con mucha frecuencia (latencia de red, colas, protocolo de enlace)
- son parte de una cadena de callback que requiere múltiples viajes de ida y vuelta entre el navegador y Dash

Cuando el costo general de un callback se vuelve demasiado grande y no es posible realizar otra optimización, el callback se puede modificar para que se ejecute directamente en el navegador en lugar de realizar una solicitud a Dash.

La sintaxis del callback es casi exactamente la misma; usa Entrada y Salida como lo haría normalmente al declarar una devolución de llamada, pero también define una función de JavaScript como el primer argumento del decorador @callback.

```python
@callback(
    Output('out-component', 'value'),
    Input('in-component1', 'value'),
    Input('in-component2', 'value')
)
def large_params_function(largeValue1, largeValue2):
    largeValueOutput = someTransform(largeValue1, largeValue2)

    return largeValueOutput
```

Se puede reescribir para usar JavaScript así:

```python
from dash import clientside_callback, Input, Output

clientside_callback(
    """
    function(largeValue1, largeValue2) {
        return someTransform(largeValue1, largeValue2);
    }
    """,
    Output('out-component', 'value'),
    Input('in-component1', 'value'),
    Input('in-component2', 'value')
)
```

También tiene la opción de definir la función en un archivo .js en su carpeta de **assets/**. Para lograr el mismo resultado que el código anterior, el contenido del archivo .js tendría este aspecto:

```javascript
window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        large_params_function: function(largeValue1, largeValue2) {
            return someTransform(largeValue1, largeValue2);
        }
    }
});
```
En Dash, el callback ahora se escribiría como:

```python
from dash import clientside_callback, ClientsideFunction, Input, Output

clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='large_params_function'
    ),
    Output('out-component', 'value'),
    Input('in-component1', 'value'),
    Input('in-component2', 'value')
)
```

## A Simple Example

A continuación se muestran dos ejemplos del uso del callback del lado del cliente para actualizar un gráfico junto con un componente dcc.Store. En estos ejemplos, actualizamos un componente dcc.Store en el backend; Para crear y mostrar el gráfico, tenemos un callback del lado del cliente en la interfaz que agrega información adicional sobre el diseño que especificamos usando los botones de opción en "Escala de gráfico".

```bash
1.ejemplo.py
```

Tenga en cuenta que, en este ejemplo, estamos creando manualmente el diccionario de figuras extrayendo los datos relevantes del marco de datos. Esto es lo que se almacena en nuestro componente dcc.Store; expanda el "Contenido del almacenamiento de figuras" arriba para ver exactamente qué se utiliza para construir el gráfico.

## Using Plotly Express to Generate a Figure

Plotly Express le permite crear declaraciones de cifras de una línea. Cuando crea un gráfico con, por ejemplo, plotly_express.Scatter, obtiene un diccionario como valor de retorno. Este diccionario tiene la misma forma que el argumento de figura de un componente dcc.Graph.

Podemos reelaborar el ejemplo anterior para usar Plotly Express.

```bash
2.express.py
```

Contenido del almacenamiento de figuras.

```bash
{
  "data": [
    {
      "hovertemplate": "year=%{x}<br>pop=%{y}<extra></extra>",
      "legendgroup": "",
      "marker": {
        "color": "var(--colorway-0)",
        "symbol": "circle"
      },
      "mode": "markers",
      "name": "",
      "orientation": "v",
      "showlegend": false,
      "x": [
        1952,
        1957,
        1962,
        1967,
        1972,
        1977,
        1982,
        1987,
        1992,
        1997,
        2002,
        2007
      ],
      "xaxis": "x",
      "y": [
        14785584,
        17010154,
        18985849,
        20819767,
        22284500,
        23796400,
        25201900,
        26549700,
        28523502,
        30305843,
        31902268,
        33390141
      ],
      "yaxis": "y",
      "type": "scatter"
    }
  ],
  "layout": {
    "template": {
      "layout": {
        "colorscale": {
          "sequential": [
            [
              0,
              "var(--colorscale-0)"
            ],
            [
              0.1111111111111111,
              "var(--colorscale-1)"
            ],
            [
              0.2222222222222222,
              "var(--colorscale-2)"
            ],
            [
              0.3333333333333333,
              "var(--colorscale-3)"
            ],
            [
              0.4444444444444444,
              "var(--colorscale-4)"
            ],
            [
              0.5555555555555556,
              "var(--colorscale-5)"
            ],
            [
              0.6666666666666666,
              "var(--colorscale-6)"
            ],
            [
              0.7777777777777778,
              "var(--colorscale-7)"
            ],
            [
              0.8888888888888888,
              "var(--colorscale-8)"
            ],
            [
              1,
              "var(--colorscale-9)"
            ]
          ]
        },
        "colorway": [
          "var(--colorway-0)",
          "var(--colorway-1)",
          "var(--colorway-2)",
          "var(--colorway-3)",
          "var(--colorway-4)",
          "var(--colorway-5)",
          "var(--colorway-6)",
          "var(--colorway-7)",
          "var(--colorway-8)",
          "var(--colorway-9)"
        ],
        "margin": {
          "t": 0
        }
      }
    },
    "xaxis": {
      "anchor": "y",
      "domain": [
        0,
        1
      ],
      "title": {
        "text": "year"
      }
    },
    "yaxis": {
      "anchor": "x",
      "domain": [
        0,
        1
      ],
      "title": {
        "text": "pop"
      }
    },
    "legend": {
      "tracegroupgap": 0
    }
  }
}
```

Nuevamente, puedes expandir la sección "Contenido del almacenamiento de figuras" arriba para ver qué se genera. Podrás notar que esto es bastante más extenso que el ejemplo anterior; en particular, ya está definido un diseño. Entonces, en lugar de crear un diseño como lo hicimos anteriormente, tenemos que modificar el diseño existente en nuestro código JavaScript.

## Clientside Callbacks with Promises

Dash 2.4 y versiones posteriores admiten devoluciones de callbacks del cliente que devuelven promises.

## Fetching Data Example

En este ejemplo, recuperamos datos (según el valor del menú desplegable) utilizando una función de callbacks asíncrona del lado del cliente que los envía a un componente **dash_table.DataTable**.

```bash
3.fetching.py
```

## Notifications Example

Este ejemplo utiliza promises y envía notificaciones de escritorio al usuario una vez que otorga permiso y selecciona el botón Notificar:

```bash
4.notification.py
```

## Callback Context

Puede usar **dash_clientside.callback_context.triggered_id** dentro de un callback del lado del cliente para acceder al ID del componente que activó el callback.

En este ejemplo, mostramos el **triggered_id** en la aplicación cuando se hace clic en un botón.

```bash
5.context.py
```

## Set Props

**dash_clientside.set_props** le permite actualizar una propiedad del componente Dash directamente en lugar de actualizarla al tenerla como resultado de una devolución del callback. Esto puede ser útil si tiene un componente que no es Dash (por ejemplo, un componente JavaScript personalizado) desde el cual desea actualizar una propiedad del componente Dash, o si desea implementar una funcionalidad personalizada que no está disponible directamente dentro de Dash pero que interactúa con Dash.

El siguiente ejemplo agrega un detector de eventos a la página. Este detector de eventos responde al usuario que presiona **Ctrl+R** actualizando los datos de un componente dcc.Store. Otra devolución de llamada tiene la propiedad de datos del componente dcc.Store como entrada, por lo que se ejecuta cada vez que cambia y envía los datos actualizados a un componente html.Div.

```bash
6.props.py
```

Notas sobre este ejemplo:

- **dash_clientside.set_props** toma dos argumentos. El primero es el ID del componente Dash a actualizar. El segundo es un objeto con el nombre de la propiedad a actualizar como clave y el valor como el nuevo valor al que actualizar esa propiedad. En este ejemplo, **dash_clientside.set_props("store-events", {data: newData})** actualiza la propiedad data del componente Dash con ID store-events, con un nuevo valor de newData, que aquí es una variable que contiene una representación de cadena. de la fecha y hora actuales.

- El callback del lado del cliente devuelve **dash_clientside.no_update**, lo que significa que no actualiza ningún componente Dash especificado como Salida. La única actualización que se realiza en la página desde el callback del lado del cliente es a través de **dash_clientside.set_props**.

- La entrada para el callback que agrega el detector de eventos es el ID del contenedor principal de la aplicación, html.Div. Usamos la propiedad id ya que esto no cambiará después de que se cargue nuestra aplicación, lo que significa que este callback del lado del cliente solo se ejecuta cuando se carga la aplicación.

- En este ejemplo, la Salida es la misma que la Entrada, pero podría ser cualquier cosa porque no actualizamos la Salida.

## Limitations

Hay algunas limitaciones a tener en cuenta:

- Los callbacks del lado del cliente se ejecutan en el hilo principal del navegador y bloquearán la representación y el procesamiento de eventos mientras se ejecutan.

- Los callbacks del lado del cliente no son posibles si necesita hacer referencia a variables globales en el servidor o si se requiere una llamada a la base de datos.
