# Background Callbacks

La mayoría de los servidores web tienen un tiempo de espera de 30 segundos de forma predeterminada, lo que supone un problema para los callbacks que tardan más en completarse. Si bien puede aumentar el tiempo de espera en el servidor web, corre el riesgo de permitir que los callbacks de larga duración utilicen todos los trabajadores de su aplicación, lo que impide que se realicen otras solicitudes. Los callbacks en segundo plano ofrecen una solución escalable para utilizar callback de larga duración ejecutándolas en una cola en segundo plano separada. En la cola en segundo plano, los callbacks se ejecutan una por una en el orden en que las recibieron los trabajadores de la cola dedicados.

Puede configurar un callback para que se ejecute en segundo plano configurando background=True en el callback. Los callbacks con background=True utilizan un backend configurado por usted para ejecutar la lógica de callback. Actualmente hay dos opciones:

- Un backend de **DiskCache** que ejecuta la lógica de callback en un proceso separado y almacena los resultados en el disco utilizando la biblioteca **DiskCache**. Este es el backend más fácil de usar para el desarrollo local, pero no se recomienda para producción.

- Un backend de **Celery** que ejecuta la lógica de callback en un trabajador de Celery y devuelve resultados a la aplicación Dash a través de un corredor de Celery como Redis. Esto se recomienda para producción ya que, a diferencia de Disk Cache, pone en cola los callbacks en segundo plano y las ejecuta una por una en el orden en que fueron recibidas por los trabajadores dedicados de Celery. **Celery** es una biblioteca de colas de trabajos lista para producción y ampliamente adoptada. Para obtener más información sobre los beneficios de las colas de trabajos, consulte ¿Por qué las colas de trabajos? sección siguiente.

## Getting Started

Los siguientes ejemplos utilizan el administrador de caché de disco cuando se ejecutan localmente. Instalar con:

```bash
pip install dash[diskcache]
```

Cuando estos ejemplos se implementan en Dash Enterprise, utilizan **Celery**.

```bash
pip install dash[celery]
```

## Basic Steps

Para utilizar un callback en segundo plano, primero debe configurar un administrador utilizando el backend elegido. El decorador @dash.callback requiere esta instancia de administrador. Puede proporcionar la instancia del administrador al constructor de la aplicación dash.Dash como argumento de la palabra clave background_callback_manager o como argumento del administrador para el decorador @dash.callback.

En los siguientes cinco ejemplos, analizaremos con más detalle cómo implementar los callbacks en segundo plano.

### Simple Example

A continuación se muestra un ejemplo simple de un callback en segundo plano que actualiza un elemento html.P con la cantidad de veces que se ha hecho clic en un botón. La devolución de llamada utiliza time.sleep para simular una operación de larga duración.

```bash
1.simple.py
```

## Disable Button While Callback Is Running

Observe cómo en el ejemplo anterior no hay ninguna indicación visual de que el callback en segundo plano se esté ejecutando. Un usuario puede hacer clic en "Run Job!" varias veces antes de que se pueda completar el trabajo original. También puede desactivar el botón mientras se ejecuta el callback y volver a activarlo cuando se complete el callback.

Para hacer esto, use el argumento en ejecución para @dash.callback. Este argumento acepta una lista de tuplas de 3 elementos. El primer elemento de cada tupla debe ser un objeto de dependencia de Output que haga referencia a una propiedad de un componente en el diseño de la aplicación. El segundo elemento es el valor que se debe establecer la propiedad mientras se ejecuta el callback, y el tercer elemento es el valor que se debe establecer la propiedad cuando se completa el callback.

Este ejemplo utiliza la ejecución para establecer la propiedad deshabilitada del botón en True mientras se ejecuta el callback y en False cuando se completa.

Nota: En este ejemplo, background_callback_manager se proporciona al constructor de la aplicación dash.Dash en lugar del decorador @dash.callback.

```bash
2.disable.py
```

Note: Existe un problema conocido por el cual el uso de la ejecución con una aplicación de varias páginas no funciona como se esperaba cuando un usuario cambia de página mientras se ejecuta la devolución de llamada.

## Cancelable Callback

Este ejemplo se basa en el ejemplo anterior y agrega soporte para cancelar un callback de larga duración usando el argumento cancelar al decorador @dash.callback. Establecemos el argumento cancelar en una lista de objetos de dependencia de entrada que hacen referencia a una propiedad de un componente en el diseño de la aplicación. Cuando el valor de esta propiedad cambia mientras se ejecuta un callback, el callback se cancela. Tenga en cuenta que el valor de la propiedad no es significativo: cualquier cambio en el valor cancela el trabajo en ejecución (si corresponde).

```bash
3.cancelable.py
```

## Progress Bar

Este ejemplo utiliza el argumento de progreso para el decorador @dash.callback para actualizar una barra de progreso mientras se ejecuta el callback. Establecemos el argumento de progreso en una agrupación de dependencia de Output que hace referencia a las propiedades de los componentes en el diseño de la aplicación.

Cuando se asigna una agrupación de dependencia al argumento de progreso de @dash.callback, la función decorada se llama con un nuevo argumento especial como primer argumento de la función. Este argumento especial, denominado **set_progress** en el siguiente ejemplo, es un identificador de función que la función decorada llama para proporcionar actualizaciones a la aplicación sobre su progreso actual. La función **set_progress** acepta un único argumento, que corresponde a la agrupación de propiedades especificadas en la agrupación de dependencia de salida pasada al argumento de progreso de @dash.callback.

```bash
4.progress.py
```

## Progress Bar Chart Graph

El argumento de progreso del decorador @dash.callback se puede utilizar para actualizar propiedades de componentes arbitrarios. Este ejemplo crea y actualiza un gráfico de barras Plotly para mostrar el estado de cálculo actual.

Este ejemplo también utiliza el argumento **Progress_default** para especificar una agrupación de valores que deben asignarse a los componentes especificados por el argumento Progress cuando el callback no está en curso. Si no se proporciona **Progress_default**, todas las propiedades de dependencia especificadas en progreso se establecen en None cuando el callback no se está ejecutando. En este caso, **Progress_default** se establece en una figura con una barra de ancho cero.

```bash
5.progress2.py
```

## Using set_props Within a Callback

Al usar **set_props** dentro de un callback, puede actualizar una propiedad de componente que no está incluida como resultado del callback. Las actualizaciones que utilizan **set_props** dentro de un callback en segundo plano se realizan de inmediato. En el siguiente ejemplo, actualizamos los datos de fila de Dash AG Grid usando **set_props** cada dos segundos, agregando gradualmente más datos.

```bash
6.set_props.py
```







el callback

los callbacks

un callback

callback
