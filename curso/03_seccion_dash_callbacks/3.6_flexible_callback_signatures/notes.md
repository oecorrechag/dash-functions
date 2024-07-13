# Flexible Callback Signatures

Al utilizar firmas de callback flexibles, introducidas en Dash 2.0, puede escribir código de aplicación que sea más fácil de administrar mediante el uso de argumentos de palabras clave, agrupación de argumentos mediante dicts o tuplas y mezclando objetos de dependencias de entrada y estado.

En el guión 1, los objetos de dependencia de entrada, estado y salida siempre se proporcionan a @app.callback como argumentos posicionales (ya sea argumentos posicionales directamente a @app.callback o como listas de los argumentos de palabras clave de entrada, estado y salida). El orden en el que se proporcionan los objetos de dependencia dicta el orden de los argumentos posicionales que se pasan a la función de callback decorada. Esto significa que los nombres de los argumentos de la función de callback no importan, sólo el orden en el que están definidos.

## Positional Arguments

```python
@callback(
    Output(...), Output(...),
    Input(...), Input(...),
    State(...)
)
def callback(a, b, c):
    return [a + b, b + c]
```

```python
@callback(
    [Output(...), Output(...)],
    [Input(...), Input(...)],
    [State(...)]
)
def callback(a, b, c):
    return [a + b, b + c]
```

```python
@callback(
    output=[Output(...), Output(...)],
    inputs=[Input(...), Input(...)],
    state=[State(...)]
)
def callback(a, b, c):
    return [a + b, b + c]
```

## Keyword Arguments

Las funciones de callback se pueden registrar para ser llamadas con argumentos de palabras clave con nombre. Puede hacer esto pasando diccionarios a las entradas y argumentos de estado de @callback. En este caso, el orden de los argumentos de la función de callback no importa. Lo único que importa es que las claves del diccionario de dependencia coincidan con los nombres de los argumentos de la función.

A continuación se muestra un ejemplo del uso de entradas de palabras clave y argumentos de estado:

```python
@callback(
    output=[Output(...), Output(...)],
    inputs=dict(a=Input(...), b=Input(...)),
    state=dict(c=State(...))
)
def callback(b, c, a):
    return [a + b, b + c]
```

También puede especificar la salida de una función de callback utilizando argumentos con nombre. En este caso, se espera que la función devuelva un diccionario con claves que coincidan con las claves del diccionario pasadas al argumento de salida de @callback. Por ejemplo:

```python
@callback(
    output=dict(x=Output(...), y=Output(...)),
    inputs=dict(a=Input(...), b=Input(...)),
    state=dict(c=State(...))
)
def callback(b, c, a):
    return dict(x=a + b, y=b + c)
```

## Interchangeable Input and State

Las firmas de callback flexibles significan que puede mezclar libremente objetos de dependencias de entrada y estado. Esto significa que las dependencias de estado se pueden incluir en el argumento de entradas y las dependencias de entrada se pueden incluir en el argumento de estado. Le recomendamos que coloque las dependencias de Input y State en las entradas en lugar de utilizar el argumento de palabra clave de estado. Por ejemplo:

```python
@callback(
    output=dict(x=Output(...), y=Output(...)),
    inputs=dict(a=Input(...), b=Input(...), c=State(...)),
)
def callback(b, c, a):
    return dict(x=a + b, y=b + c)
```

## Tuple and Dictionary Argument Grouping

También puede combinar varios valores de dependencia de Input y State en un único argumento de función.

### Tuple Grouping

Puede agrupar valores de dependencia en una tupla. Aquí, el argumento de la función de palabra clave **ab** es una tupla que consta de los valores de dos valores de dependencia de Input.

```python
@callback(
    output=[Output(...), Output(...)],
    inputs=dict(
        ab=(Input(...), Input(...)),
        c=Input(...)
    )
)
def callback(ab, c):
    a, b = ab
    return [a + b, b + c]
```

O con indexación posicional

```python
@callback(
    output=[Output(...), Output(...)],
    inputs=[(Input(...), Input(...)), Input(...)]
)
def callback(ab, c):
    a, b = ab
    return [a + b, b + c]
```

### Dictionary Grouping

De manera similar, puede agrupar varios valores de Input y State en un diccionario de valores cuando se pasan a la función. Aquí, el argumento ab se pasa a la función como un dict que contiene las claves "a" y "b" con valores correspondientes a los valores de dependencia de entrada en la especificación @callback.

```python
@callback(
    output=[Output(...), Output(...)],
    inputs=dict(
        ab=dict(a=Input(...), b=Input(...)),
        c=Input(...)
    )
)
def callback(ab, c):
    a, b = ab["a"], ab["b"]
    return [a + b, b + c]
```

También puedes anidar estos grupos a una profundidad arbitraria.

```python
@callback(
    output=[Output(...), Output(...)],
    inputs=dict(
        ab=dict(a=Input(...), b=Input(...)),
        c=Input(...)
    )
)
def callback(ab, c):
    a, b = ab["a"], ab["b"]
    return [a + b, b + c]
```

### Output Grouping

También puede utilizar las mismas agrupaciones de tuplas y dict para los valores de salida de la función.

### Output Tuple Grouping

```python
@callback(
    output=[Output(...), (Output(...), Output(...))],
    inputs=dict(
        a=Input(...),
        b=Input(...),
        c=Input(...),
    )
)
def callback(a, b, c):
    return [a, (a + b, b + c)]
```

### Output Dict Grouping

```python
@callback(
    output=[Output(...), dict(x=Output(...), y=Output(...))],
    inputs=dict(
        a=Input(...),
        b=Input(...),
        c=Input(...),
    )
)
def callback(a, b, c):
    return [a, dict(x=a+b, y=b+c)]
```

## Callback Context with Flexible Callback Signatures

```bash
dash.callback_context.args_grouping is new in Dash 2.4
```

**dash.callback_context.args_grouping** (o dash.ctx.args_grouping) es un dictado de las entradas utilizadas con firmas de callback flexibles y ayuda a simplificar los callbacks complejas que tienen muchas entradas.

Cuando se activa un callback, podemos usar **args_grouping** para obtener la siguiente información sobre nuestras entradas:

- "id": el ID del componente. Si se trata de una identificación que coincide con un patrón, será un dictado.
- "id_str": para ID de coincidencia de patrones, es el ID de dictado en cadena sin espacios en blanco.
- "propiedad": la propiedad del componente utilizada en el callback.
- "valor": el valor de la propiedad del componente en el momento en que se disparó el callback.
- "triggered": un booleano que indica si esta entrada activó el callback.

En el siguiente ejemplo, en el callback, capturamos el diccionario de entradas con c = ctx.args_grouping.all_inputs. Luego verificamos si btn1 activó el callback (verificando si c.btn1.triggered es True) y, si lo hizo, devolvemos el valor de btn1: c.btn1.value. Hacemos lo mismo para btn2 y btn3. Tenga en cuenta que solo necesitamos pasar un argumento a la función de visualización.

```bash
app.py
```
No funciono el ejemplo, desconozco el motivo

## Limitations

- Ya no se admite proporcionar el argumento de la palabra clave de State a @callback a menos que también se proporcione el argumento de la palabra clave de entrada.

- No se admiten callbacks del lado del cliente.
