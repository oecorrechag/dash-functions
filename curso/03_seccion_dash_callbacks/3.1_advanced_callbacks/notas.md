
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

# Determining which Input Has Fired with dash.callback_context

Además de las propiedades de eventos como n_clicks que cambian cada vez que ocurre un evento (en este caso un clic), existe una variable global dash.callback_context, disponible solo dentro de una devolución de llamada. Con dash.callback_context, puede determinar qué pares de componente/propiedad activaron una devolución de llamada.

A continuación se muestra un resumen de las propiedades de dash.callback_context que describe los conceptos básicos sobre cuándo usarlos. Para obtener más detalles y ejemplos, consulte Determinar qué entrada de devolución de llamada cambió.

# Properties for callback_context

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



