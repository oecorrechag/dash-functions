# Long Callbacks

Recomendamos utilizar callbacks en segundo plano con @dash.callback(..., background=True) en lugar de long_callback. El argumento background=True se introdujo en Dash 2.6.0 y soluciona varias limitaciones con long_callback, incluida su incompatibilidad con componentes agregados dinámicamente y con callbacks de coincidencia de patrones. long_callback sigue siendo seguro de usar, pero ya **no se recomienda para versiones de Dash posteriores a la 2.6.0**.

La mayoría de los servidores web tienen un tiempo de espera de 30 segundos de forma predeterminada, lo que supone un problema para las callbacks que tardan más en completarse. Si bien puede aumentar el tiempo de espera en el servidor web, corre el riesgo de permitir que las callbacks de larga duración utilicen todos los trabajadores de su aplicación, lo que impide que se realicen otras solicitudes. Los long callbacks ofrecen una solución escalable para utilizar callbacks de larga duración.

Se pueden agregar long callbacks a sus aplicaciones con el decorador @app.long_callback. Los callbacks con este decorador utilizan un backend configurado por usted para ejecutar la lógica de callback. Actualmente hay dos opciones:

- Un backend de **DiskCache** que ejecuta la lógica de callback en un proceso separado y almacena los resultados en el disco utilizando la biblioteca diskcache. Este es el backend más fácil de usar para el desarrollo local, pero no se recomienda para producción.

- Un backend de **Celery** que ejecuta la lógica de callback en un trabajador de Celery y devuelve resultados a la aplicación Dash a través de un corredor de **Celery** como RabbitMQ o Redis. Esto se recomienda para producción ya que, a diferencia de Disk Cache, utiliza una cola de trabajos y no consumirá accidentalmente todos los recursos de su servidor. Para obtener más información sobre los beneficios de las colas de trabajos, consulte ¿Por qué las colas de trabajos? sección siguiente.

## Getting Started

Los siguientes ejemplos utilizan el administrador de diskcache, que requiere bibliotecas diskcache, multiproceso y psutil:

```bash
$ pip install diskcache multiprocess psutil
```

## Basic Steps

El primer paso para utilizar long callbacks es configurar una instancia de administrador de long callbacks utilizando el backend elegido.

El decorador @app.long_callback requiere esta instancia de administrador de long callbacks. Puede proporcionar la instancia del administrador al constructor de la aplicación dash.Dash como el argumento de la palabra clave **long_callback_manager** o como el argumento del administrador para el propio decorador @app.long_callback.

El decorador @app.long_callback admite los mismos argumentos que el decorador @app.callback normal, pero también incluye soporte para varios argumentos opcionales adicionales que se explican más adelante: administrador, ejecución, cancelación, progreso y progreso_default.

En los siguientes cinco ejemplos, analizaremos con más detalle cómo implementar devoluciones de long callbacks.

### Example 1: Simple Example

A continuación se muestra un ejemplo sencillo del uso del decorador @app.long_callback para registrar una función de callback que actualiza un elemento html.P con la cantidad de veces que se ha hecho clic en un botón. La callback utiliza time.sleep para simular una operación de larga duración.

```bash
1.simple.py
```

### Example 2: Disable Button While Callback Is Running

    rve cómo en el ejemplo anterior no hay ninguna indicación visual de que se esté ejecutando el long callback. Un usuario puede hacer clic en "Run Job!" varias veces antes de que se pueda completar el trabajo original. Podemos solucionar estas deficiencias deshabilitando el botón mientras se ejecuta el callback y volviéndolo a habilitar cuando se completa el callback.

Esto se logra usando el argumento en ejecución para @app.long_callback. Este argumento acepta una lista de tuplas de 3 elementos. El primer elemento de cada tupla debe ser un objeto de dependencia de Salida que haga referencia a una propiedad de un componente en el diseño de la aplicación. El segundo elemento es el valor que se debe establecer la propiedad mientras se ejecuta el callback, y el tercer elemento es el valor que se debe establecer la propiedad cuando se completa el callback.

Este ejemplo utiliza la ejecución para establecer la propiedad deshabilitada del botón en True mientras se ejecuta el callback y en False cuando se completa.

En este ejemplo, el administrador de long callback se proporciona al constructor de la aplicación dash.Dash en lugar del decorador @app.long_callback.

```bash
2.disable.py
```

### Example 3: Cancelable Callback

Este ejemplo se basa en el ejemplo anterior y agrega soporte para cancelar un long callback duración usando el argumento cancelar al decorador @app.long_callback. Establecemos el argumento cancelar en una lista de objetos de dependencia de entrada que hacen referencia a una propiedad de un componente en el diseño de la aplicación. Cuando el valor de esta propiedad cambia mientras se ejecuta un callback, el callback se cancela. Tenga en cuenta que el valor de la propiedad no es significativo: cualquier cambio en el valor cancela el trabajo en ejecución (si corresponde).

```bash
3.cancelable.py
```

### Example 4: Progress Bar

Este ejemplo utiliza el argumento de progreso para el decorador @app.long_callback para actualizar una barra de progreso mientras se ejecuta el callback. Establecemos el argumento de progreso en una agrupación de dependencia de Salida que hace referencia a las propiedades de los componentes en el diseño de la aplicación.

Cuando se asigna una agrupación de dependencia al argumento de progreso de @app.long_callback, la función decorada se llama con un nuevo argumento especial como primer argumento de la función. Este argumento especial, denominado set_progress en el siguiente ejemplo, es un identificador de función que la función decorada llama para proporcionar actualizaciones a la aplicación sobre su progreso actual. La función set_progress acepta un único argumento, que corresponde a la agrupación de propiedades especificadas en la agrupación de dependencia de salida pasada al argumento de progreso de @app.long_callback.

```bash
4.progress.py
```

### Example 5: Progress Bar Chart Graph

El argumento de progreso del decorador @app.long_callback se puede utilizar para actualizar propiedades de componentes arbitrarios. Este ejemplo crea y actualiza un gráfico de barras Plotly para mostrar el estado de cálculo actual.

Este ejemplo también utiliza el argumento Progress_default para long_callback para especificar una agrupación de valores que deben asignarse a los componentes especificados por el argumento de progreso cuando el callback no está en curso. Si no se proporciona Progress_default, todas las propiedades de dependencia especificadas en progreso se establecen en Ninguna cuando el callback no se está ejecutando. En este caso, Progress_default se establece en una figura con una barra de ancho cero.


```bash
5.progress2.py
```

### Example with Celery/Redis

Recomendamos utilizar un backend de Celery/Redis para entornos de producción.

Con Celery y Redis, el ejemplo 3 se ve así:

```bash
6.celery.py
```

En lugar de DiskcacheLongCallbackManager, usamos CeleryLongCallbackManager e importamos Celery usando la línea:

```python
from celery import Celery
```

Configuramos una celery_app y la pasamos al CeleryLongCallbackManager. Esto se almacena en la variable long_callback_manager y luego se pasa a la aplicación:

```python
aplicación = guión.Dash(__nombre__, long_callback_manager=long_callback_manager)
```

## Caching Results

El decorador @app.long_callback puede opcionalmente memorizar los resultados de la función de callback mediante el almacenamiento en caché y proporciona una API flexible para configurar cuándo se pueden reutilizar los resultados almacenados en caché.

```bash
El almacenamiento en caché con long callback puede ayudar a mejorar el tiempo de respuesta de su aplicación, pero si desea que los usuarios puedan guardar y acceder a vistas de la aplicación en un momento determinado y generar informes en PDF a partir de estas vistas, use Dash Enterprise Snapshot Engine. Como Dash Enterprise Snapshot Engine almacena un registro completo de resultados, puede realizar un seguimiento de cómo cambia el resultado de un conjunto específico de parámetros con el tiempo. Para long callback duración en las que no necesita tener acceso a resultados anteriores, utilice long callback.
```

## How It Works

Aquí hay una descripción de alto nivel de cómo funciona el almacenamiento en caché en long_callback. Conceptualmente, puedes imaginar que hay un diccionario asociado con cada función de long callback decorada. Cada vez que se llama a la función decorada, los argumentos de entrada de la función (y potencialmente otra información sobre el entorno) se procesan para generar una clave. El decorador long_callback luego verifica el diccionario para ver si ya hay un valor almacenado usando esta clave. Si es así, no se llama a la función decorada y se devuelve el resultado almacenado en caché. De lo contrario, se llama a la función y el resultado se almacena en el diccionario usando la clave asociada.

El decorador integrado functools.lru_cache utiliza un dictado de Python como este. La situación es un poco más complicada con Dash por dos razones:

- Es posible que deseemos que el caché persista después de que se reinicie el servidor.

- Cuando una aplicación se entrega mediante múltiples procesos (por ejemplo, múltiples trabajadores gunicorn en un solo servidor o múltiples servidores detrás de un equilibrador de carga), es posible que deseemos compartir valores almacenados en caché en todos estos procesos.

Por estas razones, un simple dict de Python no es un contenedor de almacenamiento adecuado para almacenar en caché las long callback de Dash. En cambio, long_callback usa el administrador de callbacks actual DiskCache o Celery para almacenar los resultados almacenados en caché.

## Caching Flexibility Requirements

Para admitir el almacenamiento en caché en una variedad de casos de uso de desarrollo y producción, long_callback se puede configurar mediante una o más funciones de argumento cero, donde los valores de retorno de estas funciones se combinan con los argumentos de entrada de la función al generar la clave de caché. A continuación se describen varios casos de uso comunes.

## Enabling Caching

El almacenamiento en caché se habilita proporcionando una o más funciones sin argumentos al argumento cache_by de long_callback. Estas funciones se llaman cada vez que se verifica el estado de una función long_callback y sus valores de retorno se codifican como parte de la clave de caché.

A continuación se muestra un ejemplo que utiliza el administrador de callbacks DiskCache. En este ejemplo, el argumento cache_by se establece en una función lambda que devuelve un UUID fijo que se genera aleatoriamente durante la inicialización de la aplicación. La implicación de esta función cache_by es que la caché se comparte entre todas las invocaciones de callbacks en todas las sesiones de usuario manejadas por una única instancia de servidor. Cada vez que se reinicia un proceso del servidor, se borra el caché y se genera un nuevo UUID.

```bash
7.enabling.py
```

Aquí puede ver que se necesitan unos segundos para ejecutar la función de callback, pero los resultados almacenados en caché se usan después de que n_clicks vuelve a 0. Al interactuar con la aplicación en una pestaña separada, puede ver que los resultados almacenados en caché se comparten entre sesiones de usuario.

## Omitting Properties from Cache Key Calculation

El decorador @app.long_callback tiene un argumento cache_args_to_skip que se puede usar para omitir las propiedades que especifique en el cálculo de la clave de caché. Por ejemplo, probablemente no querrás incluir la propiedad n_clicks de un botón en una clave de caché porque tendrá un nuevo valor cada vez que se haga clic en él y, en este caso, podrías usar cache_args_to_skip.

Si el callback está configurada con argumentos de palabras clave (Input/State proporcionado en un dict), cache_args_to_skip debe ser una lista de nombres de argumentos como cadenas. De lo contrario, debería ser una lista de índices de argumentos como números enteros. Consulte el capítulo Firmas de callbackflexibles para obtener más información sobre argumentos de palabras clave.

## Cache_by Function Workflows

Puede utilizar las funciones cache_by para implementar una variedad de políticas de almacenamiento en caché. Aquí están algunos ejemplos:

- La función cache_by podría devolver la hora de modificación del archivo de un conjunto de datos para invalidar automáticamente el caché cuando cambia un conjunto de datos de entrada.
- En una configuración de implementación de Heroku o Dash Enterprise, la función cache_by podría devolver el hash git de la aplicación, lo que hace posible conservar el caché durante las reimplementaciones, pero invalidarlo cuando cambia la fuente de la aplicación.
- En una configuración de Dash Enterprise, la función cache_by podría devolver metadatos del usuario para evitar que los valores almacenados en caché se compartan entre usuarios autenticados.

## Setting an Expiration Time for Cache Entries

Tanto con **CeleryLongCallbackManager** como con **DiskcacheLongCallbackManager**, puede usar el argumento de caducidad para limitar cuánto tiempo se conserva una entrada de caché en la base de datos. Esta es la cantidad de segundos que se deben conservar una entrada de caché después de su último uso. Cuando se accede a una entrada, el cronómetro se reinicia.

```python
celery_app = Celery(
    __name__, broker="redis://localhost:6379/0", backend="redis://localhost:6379/1"
)
long_callback_manager = CeleryLongCallbackManager(celery_app, expire=100)
```

## Limitations

- Las long callbaks admiten el multiprocesamiento/caché de disco como backend, lo cual es ideal para entornos de desarrollo y puede ser más fácil de configurar si se trabaja en Windows. Sin embargo, para entornos de producción, recomendamos Celery/Redis.
- No puede acceder a los resultados anteriores devueltos por una long callbak. Esta funcionalidad está disponible en Snapshot Engine de Dash Enterprise.
- Las dependencias de coincidencia de patrones no se admiten con long callbaks. Se genera un error si un ID de callback contiene ALL, MATCH o ALL_SMALLER.
- dash.callback_context no es compatible.
- Si las dependencias de Input/State/Output no existen cuando se inicia la aplicación (si hacen referencia a componentes generados por otro callback), suprimir_callback_exceptions=True no evita que Dash genere errores de validación de callback. Recomendamos el siguiente enfoque:
    - La aplicación debe proporcionar un diseño_validación que contenga todos los componentes a los que hacen referencia los callbacks en la aplicación.
    - El argumento prevent_initial_call de app.long_callback debe establecerse en True.
