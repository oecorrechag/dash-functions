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

Observe cómo en el ejemplo anterior no hay ninguna indicación visual de que se esté ejecutando el long callback. Un usuario puede hacer clic en "Run Job!" varias veces antes de que se pueda completar el trabajo original. Podemos solucionar estas deficiencias deshabilitando el botón mientras se ejecuta el callback y volviéndolo a habilitar cuando se completa el callback.

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



el callback

los callbacks

un callback

callback

de callback

del callback