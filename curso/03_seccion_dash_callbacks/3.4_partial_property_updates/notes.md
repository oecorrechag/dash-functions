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
















de callback

callback

del callback

el callback

en un callback


