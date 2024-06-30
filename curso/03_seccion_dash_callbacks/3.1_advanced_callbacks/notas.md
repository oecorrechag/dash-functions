
# Catching Errors with PreventUpdate

En determinadas situaciones, no desea actualizar el resultado de la devolución de llamada. Puede lograr esto generando una excepción PreventUpdate en la función de devolución de llamada.

```bash
1.prevent.py
```

# Displaying Errors with dash.no_update

Este ejemplo ilustra cómo puede mostrar un error manteniendo la entrada anterior, usando dash.no_update para actualizar solo algunas de las salidas de devolución de llamada.

```bash
2.no_update.py
```

# Updating Component Properties when a Callback is Running

Puede utilizar el argumento en ejecución en una devolución de llamada para actualizar pares de propiedad-componente específicos cuando la devolución de llamada se está ejecutando. Por ejemplo, puede desactivar el botón que activó la devolución de llamada mientras la devolución de llamada aún se está ejecutando.

running acepta una lista de tuplas de tres elementos, donde:

- El primer elemento de cada tupla debe ser un objeto de dependencia de Salida que haga referencia a una propiedad de un componente en el diseño de la aplicación.
- El segundo elemento es el valor al que se debe establecer la propiedad mientras se ejecuta la devolución de llamada.
- El tercer elemento es el valor al que se debe establecer la propiedad cuando se completa la devolución de llamada.

En el siguiente ejemplo, el argumento en ejecución establece la propiedad deshabilitada en el botón de envío en Verdadero mientras se ejecuta la devolución de llamada y la vuelve a establecer en Falso una vez que se completa la devolución de llamada.

```bash
3.updating.py
```

## Determining which Input Has Fired with dash.callback_context

Además de las propiedades de eventos como n_clicks que cambian cada vez que ocurre un evento (en este caso un clic), existe una variable global dash.callback_context, disponible solo dentro de una devolución de llamada. Con dash.callback_context, puede determinar qué pares de componente/propiedad activaron una devolución de llamada.

A continuación se muestra un resumen de las propiedades de dash.callback_context que describe los conceptos básicos sobre cuándo usarlos. Para obtener más detalles y ejemplos, consulte Determinar qué entrada de devolución de llamada cambió.

## Properties for callback_context

- **triggered_id:** La identificación del componente que desencadenó la devolución de llamada.

- **triggered_prop_ids:** Un diccionario de los identificadores de componentes y accesorios que activaron la devolución de llamada. Es útil cuando varias entradas pueden desencadenar la devolución de llamada al mismo tiempo, o varias propiedades del mismo componente pueden desencadenar la devolución de llamada.

- **args_grouping:** Un diccionario de las entradas utilizadas con firmas de devolución de llamada flexibles. Las claves son los nombres de las variables y los valores son diccionarios que contienen:

    - **"id":** el ID del componente. Si se trata de una identificación que coincide con un patrón, será un dictado.
    - **"id_str":** para ID de coincidencia de patrones, es el ID de dictado en cadena sin espacios en blanco.
    - **"property":** la propiedad del componente utilizada en la devolución de llamada.
    - **"triggered":** un booleano que indica si esta entrada activó la devolución de llamada.

    Dash 2.4 y versiones anteriores de Dash tienen las siguientes propiedades

    - **triggered:** lista de todos los accesorios de entrada que cambiaron y provocaron que se ejecutara la devolución de llamada. Está vacío cuando se llama a la devolución de llamada en la carga inicial, a menos que un accesorio de entrada obtenga su valor de otra devolución de llamada inicial. Las devoluciones de llamada activadas por acciones del usuario generalmente tienen un elemento activado, a menos que la misma acción cambie dos accesorios a la vez o la devolución de llamada tenga varios accesorios de entrada que sean modificados por otra devolución de llamada basada en una única acción del usuario.

    - **inputs and states:** le permiten acceder a los parámetros de devolución de llamada por ID y propiedad en lugar de a través de la función args. Estos tienen la forma de diccionarios { 'component_id.prop_name': value }

    - **outputs_list, inputs_list, and states_list:** listas de entradas, salidas y elementos de estado organizados como los encontrará en los argumentos de devolución de llamada y el valor de retorno.

    - **response:** el objeto de respuesta HTTP que se está construyendo, útil para cambiar las cookies.

```bash
4.properties.py
```

# Improving Performance with Memoization

La memorización le permite evitar cálculos largos almacenando los resultados de las llamadas a funciones.

Para comprender mejor cómo funciona la memorización, comencemos con un ejemplo sencillo.

```bash
5.memoization.py
```

Llamar a slow_function('test') la primera vez tardará 10 segundos. Llamarlo por segunda vez con el mismo argumento casi no llevará tiempo ya que el resultado calculado previamente se guardó en la memoria y se reutilizó.

La sección Rendimiento de los documentos de Dash profundiza un poco más en cómo aprovechar múltiples procesos e hilos junto con la memorización para mejorar aún más el rendimiento.

# When Are Callbacks Executed?

Esta sección describe las circunstancias bajo las cuales el cliente front-end del renderizador de tablero puede realizar una solicitud al servidor back-end de Dash (o al código de devolución de llamada del lado del cliente) para ejecutar una función de devolución de llamada.

## When a Dash App First Loads

- **Llamada inicial de los callbacks:** Cuando una aplicación Dash se carga por primera vez, todos sus callbacks se ejecutan utilizando el valor inicial de sus entradas. Esto se conoce como la "initial call" del callback.
- **Evitar la llamada inicial:** El atributo **prevent_initial_call** de los callbacks de Dash permite suprimir la llamada inicial si es necesario.
- **Cadena de callbacks:** Al cargar la aplicación, Dash analiza recursivamente toda la cadena de callbacks para determinar el orden de ejecución.
- **Dependencias entre callbacks:** Los callbacks se bloquean si sus entradas dependen de la salida de otros callbacks que aún no se han ejecutado.
- **Optimización del renderizado:** Dash prioriza la ejecución de callbacks cuyos valores de entrada están disponibles inmediatamente. De esta forma, minimiza el tiempo y esfuerzo de renderizado, evitando redibujar la página innecesariamente.

```bash
6.loads.py
```

Tenga en cuenta que cuando un navegador web termina de cargar esta aplicación y está lista para la interacción del usuario, los componentes **html.Div** no dicen **"devolución de llamada no ejecutada"** como se declara en el diseño de la aplicación, sino **"n_clicks es Ninguno"** como resultado de callback change_text() se está ejecutando. Esto se debe a que la "llamada inicial" del callback se produjo cuando **n_clicks** tenía el valor Ninguno.

## As a Direct Result of User Interaction

Con mayor frecuencia, los callbacks se ejecutan como resultado directo de la interacción del usuario, como hacer clic en un botón o seleccionar un elemento en un menú desplegable. Cuando ocurren tales interacciones, los componentes de Dash comunican sus nuevos valores al cliente front-end del renderizador de tablero, que luego solicita que el servidor Dash ejecute cualquier función de devolución de llamada que tenga el valor recién cambiado como entrada.

Si una aplicación Dash tiene varias devoluciones de llamada, el renderizador de guión solicita que se ejecuten devoluciones de callback en función de si se pueden ejecutar inmediatamente o no con las entradas recién modificadas. Si varias entradas cambian simultáneamente, se realizan solicitudes para ejecutarlas todas.

El hecho de que estas solicitudes se ejecuten o no de forma sincrónica o asincrónica depende de la configuración específica del servidor back-end de Dash. Si se ejecuta en un entorno de subprocesos múltiples, todas los callback se pueden ejecutar simultáneamente y devolverán valores según su velocidad de ejecución. Sin embargo, en un entorno de subproceso único, los callback se ejecutarán una a la vez en el orden en que las reciba el servidor.

En la aplicación de ejemplo anterior, al hacer clic en el botón se ejecuta el callback.

## As an Indirect Result of User Interaction

Cuando un usuario interactúa con un componente, el callback resultante puede tener salidas que son a su vez la entrada de otros callbacks. El renderizador de guión bloqueará la ejecución de dicha devolución de callback hasta que se haya ejecutado la devolución de callback cuya salida es su entrada.

```bash
7.interaction.py
```

La aplicación Dash anterior demuestra cómo se encadenan los callback. Tenga en cuenta que si primero hace clic en **"execute slow callback"** y luego hace clic en **"execute fast callback"**, el tercer callback no se ejecuta hasta que execute slow callback termine de ejecutarse. Esto se debe a que el tercer callback tiene la salida de la segunda callback como entrada, lo que le permite al renderizador de guión saber que debe retrasar su ejecución hasta que finalice el segundo callback.

## When Dash Components Are Added to the Layout

Es posible que un callback inserte nuevos componentes de Dash en el diseño de una aplicación Dash. Si estos nuevos componentes son en sí mismos las entradas para otras funciones de callback, entonces su aparición en el diseño de la aplicación Dash activará la ejecución de esas funciones de callback.

En esta circunstancia, es posible que se realicen varias solicitudes para ejecutar la misma función de callback. Esto ocurriría si el callback en cuestión ya se solicitó y su salida se devolvió antes de que se agreguen al diseño los nuevos componentes que también son sus entradas.

# Prevent Callback Execution Upon Initial Component Render

Puede usar el atributo **prevent_initial_call** para evitar que se activen callback cuando sus entradas aparecen inicialmente en el diseño de su aplicación Dash.

Este atributo se aplica cuando el diseño de su aplicación Dash se carga inicialmente y también cuando se introducen nuevos componentes en el diseño cuando se activa un callback.

```bash
8.prevent.py
```

Sin embargo, el comportamiento anterior solo se aplica si tanto la salida como la entrada del callback están presentes en el diseño de la aplicación durante la carga inicial de la aplicación.

Es importante tener en cuenta que **prevent_initial_call** no evitará que se active un callback en el caso de que la entrada de callback se inserte en el diseño como resultado de otro callback después de que la aplicación se cargue inicialmente, a menos que la salida se inserte junto con esa entrada.

```bash
9.prevent.py
```

En este caso, **prevent_initial_call** evitará que se active el callback **update_output()** cuando su entrada se inserta por primera vez en el diseño de la aplicación como resultado del callback **display_page()**. Esto se debe a que tanto la entrada como la salida del callback ya están contenidas en el diseño de la aplicación cuando se ejecuta el callback.

Sin embargo, debido a que el diseño de la aplicación contiene solo la salida del callback, y no su entrada, **prevent_initial_call** no evitará que se active el callback **update_layout_div**(). Dado que aquí se especifica **suprimir_callback_exceptions=True**, Dash debe asumir que la entrada está presente en el diseño de la aplicación cuando se inicializa la aplicación. Desde la perspectiva del elemento de salida en este ejemplo, el nuevo componente de entrada se maneja como si a una entrada existente se le hubiera proporcionado un nuevo valor, en lugar de tratarlo como se representó inicialmente.

# Callbacks with No Outputs

Todos los ejemplos anteriores tienen entradas que activan callbacks, así como salidas que se actualizan. Los callbacks también admiten no tener salidas. Esto puede resultar útil en los casos en los que desea que se ejecute algún código cuando una acción desencadena un callback, pero no desea actualizar ninguna propiedad del componente. Por ejemplo, es posible que desees recuperar algunos datos y guardarlos, enviar correos electrónicos o interactuar con otros servicios externos fuera del ecosistema Dash.

En el siguiente ejemplo, utilizando el componente dcc.Upload, permitimos al usuario cargar un archivo en el servidor.

Nuestro ejemplo no tiene declaraciones de devolución. Los callback sin salidas no deberían devolver un valor porque no hay salidas para actualizar. Si devuelves un valor de callback cuando no hay resultados para actualizar, verás un error en Dash Dev Tools.

```bash
10.no_outputs.py
```

## Setting Properties Directly

Puede actualizar los pares componente-propiedad directamente desde un callback sin que sean salidas de callback utilizando **set_props**. Con este enfoque, actualizar condicionalmente diferentes pares componente-propiedad es más sencillo porque no es necesario agregarlos todos como salidas y usar **dash.no_update**.

**set_props** toma el ID del componente a actualizar como primer argumento, seguido de un dictado de propiedades a actualizar. Cada clave dict debe ser un nombre de propiedad, siendo el valor de la clave el valor para actualizar la propiedad del componente.

Aquí, tenemos un callback que usa **set_props** para establecer la propiedad **is_open** del modal en False cuando el callback es activada por un usuario que selecciona el botón modal_close. De lo contrario, se establece en True y se muestra el contenido modal. No tenemos resultados en este callback, pero **set_props** también se puede combinar con resultados.

Este ejemplo se basa en el ejemplo de selección de fila emergente en la página Dash AG Grid, que en su lugar utiliza salidas y **dash.no_update**.

```bash
11.setting.py
```

En el ejemplo anterior, usamos **set_props** para simplificar el código. En otros casos, sin embargo, el uso de Salidas puede generar un código más simple porque las Salidas se definen en la firma del callback, lo que facilita saber qué propiedades de componente actualiza un callback.

**Limitations**

- Las propiedades de los componentes actualizadas con **set_props** no aparecerán en el gráfico del callback para la depuración.
- Las propiedades de los componentes actualizadas usando **set_props** no aparecerán como cargadas cuando estén empaquetadas con un componente `dcc.Loading`.
- **set_props** no valida la identificación o los nombres de propiedad proporcionados, por lo que no se mostrará ningún error si contienen errores tipográficos. Esto puede hacer que las aplicaciones que usan **set_props** sean más difíciles de depurar.
- El uso de **set_props** con callback encadenadas puede generar resultados inesperados.

# Circular Callbacks

No se admiten cadenas de callback circulares que impliquen varios callback. <br>
Se pueden utilizar callback circulares para mantener varias entradas sincronizadas entre sí.

## Synchronizing a Slider with a Text Input Example

```bash
12.sync.py
```

## Displaying Two Inputs with Different Units Example

```bash
13.sync.py
```

## Synchronizing Two Checklists

```bash
14.sync.py
```



# parametros adicionales

prevent_initial_call=True               # 8.prevent.py
no ouputs de callback                   # 10.no_outputs.py
set_props                               # 11.setting.py          para modales

# Notes inputs 

Input('show-secret', 'n_clicks')        # entrada boton
Input('num', 'value')                   # entrada dcc input texto u otro
Input("first_output_3", "children"),    # entrada un callback

# Notes states
State('input-on-submit-text', 'value'), # esperando un dcc input texto

# Notes Outputs 

Output('body-div', 'children'),         # salida div texto
Output('container', 'children'),        # salida un container  