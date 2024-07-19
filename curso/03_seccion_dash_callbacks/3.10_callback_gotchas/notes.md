# Callback Gotchas

```bash
Para aprovechar al máximo esta página, asegúrese de haber leído sobre las callbacks básicas en los Fundamentos de Dash.
```

Hay algunos aspectos de cómo funciona Dash que pueden resultar complicados, especialmente cuando se trata de callbacks. Esta página describe algunos errores comunes que puede encontrar al comenzar a crear aplicaciones Dash más complejas.

## Callbacks require their Inputs, States, and Output to be present in the layout

De forma predeterminada, Dash aplica validación a sus callbacks, lo que realiza comprobaciones como validar los tipos de argumentos de callbacks y verificar si los componentes de entrada y salida especificados realmente tienen las propiedades especificadas. Para una validación completa, todos los componentes dentro de su callbacks deben existir en el diseño cuando se inicia su aplicación y verá un error si no es así.

Sin embargo, en el caso de aplicaciones Dash más complejas que implican una modificación dinámica del diseño (como aplicaciones de varias páginas), no todos los componentes que aparecen en sus callbacks se incluirán en el diseño inicial. Puede eliminar esta restricción deshabilitando la validación de callbacks de esta manera:

```python
app.config.suppress_callback_exceptions = True
```

## Callbacks require all Inputs and States to be rendered on the page

Si ha deshabilitado la validación de callback para admitir diseños dinámicos, no se le alertará automáticamente sobre la situación en la que un componente dentro de un callback no se encuentre dentro de un diseño. En esta situación, donde falta un componente registrado con una devolución de callback, el callback no se activará. Por ejemplo, si define un callback con solo un subconjunto de las entradas especificadas presentes en el diseño de página actual, el callback simplemente no se activará en absoluto.

## All callbacks must be defined before the server starts

Todas sus callbacks deben definirse antes de que el servidor de su aplicación Dash comience a ejecutarse, es decir, antes de llamar a app.run(debug=True). Esto significa que, si bien puede ensamblar dinámicamente fragmentos de diseño modificados durante el manejo de un callback, no puede definir callbacks dinámicas en respuesta a la entrada del usuario durante el manejo de una callback. Si tiene una interfaz dinámica, donde un callback cambia el diseño para incluir un conjunto diferente de controles de entrada, entonces ya debe haber definido los callbacks necesarias para dar servicio a estos nuevos controles con anticipación.

Por ejemplo, un escenario común es un componente desplegable que actualiza el diseño actual para reemplazar un panel con otro panel lógicamente distinto que tiene un conjunto diferente de controles (cuyo número y tipo pueden depender de otras entradas del usuario) y una lógica diferente. para generar los datos subyacentes. Una organización sensata sería que cada uno de estos paneles tuviera callbacks independientes. En este escenario, cada una de estaos callbacks debe definirse antes de que la aplicación comience a ejecutarse.

En términos generales, si una característica de su aplicación Dash es que la cantidad de entradas o estados está determinada por la entrada de un usuario, entonces debe predefinir cada permutación de callback que un usuario pueda activar potencialmente. Para ver un ejemplo de cómo esto se puede hacer mediante programación usando el decorador de callback, consulte esta publicación del foro de la comunidad Dash.

## Callback definitions don't need to be in lists

A partir de Dash 1.15.0, no es necesario que las definiciones de Input, Output y State de callback estén en las listas. Aún debe proporcionar primero los elementos de Salida y el formulario de lista aún es compatible. En particular, si desea devolver un único elemento de salida envuelto en una lista de longitud 1, aún así debe envolver la Salida en una lista. Esto puede resultar útil para callbacks generados por procedimientos.

## All Dash Core Components in a layout should be registered with a callback

Si un componente Dash Core está presente en el diseño pero no está registrado con un callback (ya sea como Input, State o Output), cualquier cambio en su valor por parte del usuario se restablecerá al valor original cuando cualquier callback actualice la página.
