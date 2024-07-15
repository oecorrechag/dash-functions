# Determining Which Callback Input Changed

A veces tendrás varias entradas de callback y querrás actualizar una salida de manera diferente dependiendo de qué entrada activó el callback.

Puede usar las propiedades de dash.callback_context (o dash.ctx para abreviar en Dash 2.4 y versiones posteriores) para determinar qué entrada activó un callback.

## Capturing the Component ID that Triggered the Callback

En este ejemplo, obtenemos la identificación del botón que activó el callback y la mostramos cada vez que se hace clic en un botón. En la primera carga, cuando ninguna acción del usuario ha activado el callback, el valor de triggered_id es Ninguno. Lo comprobamos y lo utilizamos para mostrar el mensaje: "You haven't clicked any button yet".

```bash
Nota: triggered_id está disponible en Dash 2.4 y versiones posteriores. En versiones anteriores de Dash, puedes obtener la identificación activada con dash.callback_context.triggered[0]['prop_id'].split('.')[0]
```

```bash
1.capturing.py
```

Con ID del callback que coinciden con patrones

En el ejemplo anterior, triggered_id es una cadena ya que la identificación de la entrada es una cadena. En los casos en que la identificación de un componente sea un diccionario, por ejemplo, con callbacks de coincidencia de patrones, triggered_id también será un diccionario.

Por ejemplo, con este componente:

```python
dcc.Dropdown(
        ['NYC', 'MTL', 'LA', 'TOKYO'],
        id={
            'type': 'filter-dropdown',
            'index': 0
        })
```

Esto se utiliza como entrada para un callback:

```python
Input({'type': 'filter-dropdown', 'index': ALL}, 'value')
```

triggered_id devuelve:

```python
{'index': 0, 'type': 'filter-dropdown'}
```

Aquí puede capturar el índice con: triggered_id.index, o el tipo con triggered_id.type.

## Determining Multiple Input Triggers and Properties

En los casos en los que varias entradas activan un callback, puede utilizar triggered_prop_ids. También es útil si diferentes propiedades del mismo componente pueden activar el callback y desea capturar la propiedad.

triggered_prop_ids devuelve un diccionario de entradas que activaron el callback. Cada clave es un <component_id>.<component_property> y el valor correspondiente es el <component_id>.

En nuestro primer ejemplo anterior, si usáramos triggered_prop_ids, cuando se haga clic en el Botón 2, devolverá:

```python
{'btn-2-ctx-example.n_clicks': 'btn-2-ctx-example'}
```

Con callbacks que coinciden con patrones

Para el ejemplo anterior de 'filter-dropdown' de callback de coincidencia de patrones, triggered_prop_ids devuelve:

```python
{'{"index":0,"type":"filter-dropdown"}.value': {'index': 0, 'type': 'filter-dropdown'}}
```

Con callbacks que coinciden con patrones con múltiples activadores

Si tenemos una serie de menús desplegables con diferentes índices (0-2) y todos activaron el callback, triggered_prop_ids devuelve:

```python
{'{"index":0,"type":"filter-dropdown"}.value': {'index': 0, 'type': 'filter-dropdown'}, '{"index":1,"type":"filter-dropdown"}.value': {'index': 1, 'type': 'filter-dropdown'}, '{"index":2,"type":"filter-dropdown"}.value': {'index': 2, 'type': 'filter-dropdown'}}
```

En todos estos ejemplos, las claves del diccionario tienen el formato `<component_id>.<component_property>, mientras que los valores del diccionario son los identificadores de los componentes.
