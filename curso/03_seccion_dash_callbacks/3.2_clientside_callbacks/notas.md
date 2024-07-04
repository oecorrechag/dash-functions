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