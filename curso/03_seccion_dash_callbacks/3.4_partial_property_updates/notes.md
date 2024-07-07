# Multi-Page Apps and URL Support


Dash presenta aplicaciones web como una "aplicación de una sola página". Al utilizar dcc.Link, la aplicación no se recarga completamente al navegar, lo que hace que la navegación sea muy rápida. Con Dash, puede crear aplicaciones de varias páginas utilizando componentes y callbacks dcc.Location y dcc.Link.

Dash Pages utiliza estos componentes y abstrae la lógica de callback necesaria para el enrutamiento de URL, lo que facilita la puesta en marcha de una aplicación de varias páginas. 

## The Dash Patch Class

Las actualizaciones de propiedades parciales utilizan la clase **Patch**, con la que puede importar desde Dash Import Patch. Cree una instancia de un objeto Patch en una callback para realizar actualizaciones parciales en la salida de una devolución de llamada. Este objeto Patch define los cambios que se deben realizar en la propiedad. Los posibles cambios incluyen asignar un nuevo valor, fusionar un diccionario y agregar un elemento a una lista. Las operaciones están definidas por el objeto Patch dentro de su devolución de llamada, pero se ejecutan en el cliente del navegador en la interfaz de Dash.

### Updating Title Color with a Partial Update

```bash
1.updating_color.py
```

Pasos:

- Primero, importamos la clase **Patch**.
- Definimos nuestras entradas y salidas de callback de la misma manera que con un callback estándar.
- En nuestro callback, creamos un objeto **Patch**. Aquí lo llamamos **patched_figure**, pero el nombre es arbitrario. Esta figura_parcheada definirá los cambios que Dash debe realizar en la figura.
- Luego, definimos un cambio de asignación, diciéndole a Dash que queremos que esta parte de la figura sea el valor en **new_color**.
- Devolvemos nuestra figura_parcheada.
- Una vez que el callback devuelve el objeto **Patch**, en la interfaz, Dash asigna el valor en **new_color** a ['layout']['title']['font']['color'] en la figura.





callback


