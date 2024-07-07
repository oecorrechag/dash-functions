# Pattern-Matching Callbacks

Los selectores de callback de coincidencia de patrones MATCH, ALL y ALLSMALLER le permiten escribir callback que responden o actualizan una cantidad arbitraria o dinámica de componentes.

## Simple Example with ALL

Este ejemplo representa un número arbitrario de elementos dcc.Dropdown y los callbacks se activa cada vez que cambia alguno de los elementos dcc.Dropdown. Intente agregar algunos menús desplegables y seleccionar sus valores para ver cómo se actualiza la aplicación.

```bash
1.all.py
```

Algunas notas sobre este ejemplo:

- Observe cómo la identificación en dcc.Dropdown es un diccionario en lugar de una cadena. Esta es una nueva característica que habilitamos para los callbacks que coinciden con patrones (anteriormente, los ID tenían que ser cadenas).
- En el segundo callback, tenemos Input({'type': 'city-filter-dropdown', 'index': ALL}, 'value'). Esto significa "hacer coincidir cualquier entrada que tenga un diccionario de ID donde 'tipo' es 'menú desplegable de filtro de ciudad' e 'índice' es cualquier cosa. Siempre que la propiedad de valor de cualquiera de los menús desplegables cambie, envíe todos sus valores del callback. "
- Las claves y valores del diccionario de ID (type, index, city-filter-dropdown) son arbitrarios. Esto podría haberse llamado {'foo': 'bar', 'baz': n_clicks}.
- Sin embargo, para facilitar la lectura, recomendamos utilizar claves como tipo, índice o identificación. El tipo se puede usar para hacer referencia a la clase o establecer componentes dinámicos y el índice o la identificación se pueden usar para hacer referencia a qué componente coincide dentro de ese conjunto. En este ejemplo, solo tenemos un único conjunto de componentes dinámicos, pero es posible que usted tenga varios conjuntos de componentes dinámicos en aplicaciones más complejas o si está utilizando MATCH.
- No se necesitaba 'type': 'city-filter-dropdown'. La misma devolución de llamada habría funcionado con Input({'index': ALL}, 'value'). Incluimos 'type': 'city-filter-dropdown' como un especificador adicional en caso de que cree varios conjuntos de componentes dinámicos.
- Las propiedades de los componentes en sí (por ejemplo, el valor) no pueden coincidir con un patrón, solo los ID son dinámicos.
- Este ejemplo utiliza Patch para realizar una actualización parcial de la propiedad 'children' de 'dropdown-container-div'. Agregamos un menú desplegable cada vez que se ejecuta la primera devolución de llamada.

### Simple ALL Example Without Partial Updates

Este ejemplo es similar al ejemplo simple con ALL, pero usa State para acceder a la lista de menús desplegables que se muestran actualmente. En el primer callback, luego agregamos a esta lista de menús desplegables y la devolvemos como resultado.

```bash
2.all.py
```

## Simple Example with MATCH

Al igual que ALL, MATCH activará el callback cuando cambie cualquiera de las propiedades del componente. Sin embargo, en lugar de pasar todos los valores del callback, MATCH pasará solo un valor al callbac. En lugar de actualizar una única salida, actualizará la salida dinámica con la que "coincide".

```bash
3.match.py
```

Algunas notas sobre este ejemplo:

- El callback **display_dropdowns** devuelve dos elementos con el mismo índice: un menú desplegable y un div.
- El segundo callback utiliza el selector MATCH. Con este selector, le pedimos a Dash que:
    - Active el callback cada vez que cambie la propiedad de valor de cualquier componente con el id 'tipo': 'desplegable dinámico': Entrada ({'tipo': 'desplegable dinámico', 'índice': MATCH}, 'valor')
    - Actualice el componente con el id 'type': 'dynamic-output' y el índice que coincida con el mismo índice de la entrada: Output({'type': 'dynamic-output', 'index': MATCH}, 'children' )
    - Pase la identificación del menú desplegable a el callback: State({'type': 'dynamic-dropdown', 'index': MATCH}, 'id')
- Con el selector MATCH, solo se pasa un valor al callback para cada entrada o estado. Esto es diferente al ejemplo anterior con el selector TODO donde Dash pasó todos los valores al callback.
- Observe lo importante que es diseñar diccionarios de ID que "alineen" las entradas con las salidas. El contrato MATCH es que Dash actualizará cualquier salida que tenga la misma ID dinámica que la ID. En este caso, el "ID dinámico" es el valor del índice y hemos diseñado nuestro diseño para devolver menús desplegables y divs con valores de índice idénticos.
- En algunos casos, puede ser importante saber qué componente dinámico cambió. Como se indicó anteriormente, puede acceder a esto configurando la identificación como Estado en el callback.
- También puede usar **dash.callback_context** para acceder a las entradas y al estado y saber qué entrada cambió. **outputs_list** es particularmente útil con MATCH porque puede indicarle qué componente dinámico es responsable de actualizar esta invocación particular de la devolución de llamada. Así es como se verían esos datos con dos menús desplegables representados en la página después de cambiar el primer menú desplegable.
    
    - **dash.callback_context.triggered_prop_ids** devuelve un diccionario de entradas que activaron el callback. Cada clave es un <component_id>.<component_property> y el valor correspondiente es el <component_id>. En este ejemplo, podemos ver que el id del componente que activó al callback fue {'index': 0, 'type': 'dynamic-dropdown'} y la propiedad fue value:

        ```python
        {
            '{"index":0,"type":"dynamic-dropdown"}.value': {
                "index": 0,
                "type": "dynamic-dropdown",
            }
        }
        ```
    
    - dash.callback_context.triggered. Tenga en cuenta que prop_id es un diccionario encadenado sin espacios en blanco.

        ```python
        [
            {
                'prop_id': '{"index":0,"type":"dynamic-dropdown"}.value',
                'value': 'NYC'
            }
        ]
        ```

    - guión.callback_context.inputs. Tenga en cuenta que la clave es un diccionario encadenado sin espacios en blanco.

        ```python
        {
        '{"index":0,"type":"dynamic-dropdown"}.value': 'NYC'
        }
        ```

    - dash.callback_context.inputs_list. Cada elemento de la lista corresponde a una de las declaraciones de entrada. Si una de las declaraciones de entrada coincide con un patrón, contendrá una lista de valores.

        ```python
        [
            [
                {
                'id': {
                    'index': 0,
                    'type': 'dynamic-dropdown'
                },
                'property': 'value',
                'value': 'NYC'
                }
            ]
        ]
        ```

    - dash.callback_context.outputs_list

        ```python
        {
            'id': {
                'index': 0,
                'type': dynamic-output'
            },
            'property': 'children'
        }
        ```
    
```bash
4.match.py
```

## Simple Example with ALLSMALLER

En el siguiente ejemplo, **ALLSMALLER** se utiliza para pasar los valores de todos los menús desplegables de la página que tienen un índice menor que el índice correspondiente al div.

La interfaz de usuario en el siguiente ejemplo muestra resultados de filtro que son cada vez más específicos en cada uno a medida que aplicamos cada menú desplegable adicional.

**ALLSMALLER** solo se puede usar en elementos de Input y State, y debe usarse en una clave que tenga MATCH en los elementos de Salida.

**ALLSMALLER** no siempre es necesario (generalmente puedes usar **ALL** y filtrar los índices en tu devolución de llamada) pero simplificará tu lógica.

```bash
5.all_smaller.py
```

En el ejemplo anterior, intente agregar algunos filtros y luego cambie el primer menú desplegable. Observe cómo cambiar este menú desplegable actualizará el texto de cada html.Div que tenga un índice que dependa de ese menú desplegable.

Es decir, cada html.Div se actualizará cada vez que cambie alguno de los menús desplegables con un índice menor que el mismo.

Entonces, si se agregaron 10 filtros y el primer menú desplegable cambió, Dash activará su devolución de llamada 10 veces, una vez para actualizar cada html.Div que depende del dcc.Dropdown que cambió.

Como se indicó anteriormente, también puede usar dash.callback_context para acceder a las entradas y al estado y saber qué entrada cambió. Así es como se verían esos datos al actualizar el segundo div con dos menús desplegables representados en la página después de cambiar el primer menú desplegable.

dash.callback_context.triggered_prop_ids devuelve un diccionario de entradas que activaron la devolución de llamada. Cada clave es un <component_id>.<component_property> y el valor correspondiente es el <component_id>. En este ejemplo, podemos ver que el id del componente que activó la devolución de llamada fue {'index': 0, 'type': 'filter-dropdown-ex3'} y la propiedad fue value:

```python
{
  '{"index":0,"type":"filter-dropdown-ex3"}.value': {
      "index": 0,
      "type": "filter-dropdown-ex3",
  }
}
```

dash.callback_context.triggered. Tenga en cuenta que prop_id es un diccionario encadenado sin espacios en blanco.

```python
[
  {
    'prop_id': '{"index":0,"type":"filter-dropdown-ex3"}.value',
    'value': 'Canada'
  }
]
```

dash.callback_context.inputs. Note that the key is a stringified dictionary with no whitespace.

```python
{
'{"index":1,"type":"filter-dropdown-ex3"}.value': 'Albania',
'{"index":0,"type":"filter-dropdown-ex3"}.value': 'Canada'
}
```

dash.callback_context.inputs_list. Cada elemento de la lista corresponde a una de las declaraciones de entrada. Si una de las declaraciones de entrada coincide con un patrón, contendrá una lista de valores.

```python
[
  {
    'id': {
      'index': 1,
      'type': 'filter-dropdown-ex3'
    },
    'property': 'value',
    'value': 'Albania'
  },
  [
    {
      'id': {
        'index': 0,
        'type': 'filter-dropdown-ex3'
      },
      'property': 'value',
      'value': 'Canada'
    }
  ]
]
```

dash.callback_context.outputs_list

```python
{
  'id': {
      'index': 1,
      'type': output-ex3'
  },
  'property': 'children'
}
```

```bash
6.all_smaller.py
```

## Todo App

Crear una aplicación Todo es un ejercicio de interfaz de usuario clásico que demuestra muchas funciones en aplicaciones comunes de "crear, leer, actualizar y eliminar" (CRUD).

```bash
7.all.py
```

```bash
8.all.py
```
