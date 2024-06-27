# Sharing Data Between Callbacks

## Why Share State?

- **Evitar tareas repetitivas:** En aplicaciones con callbacks que dependen de tareas costosas (consultas a bases de datos, simulaciones, descargas), se busca optimizar para no repetir esas tareas en cada callback.
- **Callback con salidas múltiples:** Una opción es tener un callback con salidas múltiples. Se ejecuta la tarea costosa una vez y se usa el resultado en todas las salidas. Sirve cuando el mismo dato se necesita para mostrar en diferentes elementos (ej: gráfica y tabla).
- **Cuándo no usar salidas múltiples:** No conviene si hay entradas independientes que no siempre requieren la tarea costosa. Ejemplo: un app que muestra temperatura según fecha y unidad (Celsius o Fahrenheit). Si se usaran salidas múltiples, al cambiar de unidad se volvería a descargar el clima, siendo innecesario.
- **Compartir variables de estado:** En estos casos, es mejor tener callbacks separados. Uno descarga el clima y otro muestra la temperatura según el dato descargado y la unidad seleccionada. Así, al cambiar solo la unidad, no se repite la descarga.

## Dash is Stateless

**Escalabilidad:** Dash es diseñado para ser sin estado, lo que lo hace más escalable que frameworks con estado.

**Razones de escalabilidad:**    
    - **Añadir poder de cómputo es sencillo:** se pueden ejecutar "copias" de la aplicación en procesos separados.
    - **Ejemplos de escalado:**
        - Servidores múltiples con balanceo de carga.
        - Contenedores Docker.

**Robustez:**
- La falla de un proceso no afecta a otros: si un proceso falla, los demás siguen funcionando.
- Dash Enterprise Kubernetes: Los contenedores pueden correr en servidores o regiones separadas, aumentando la resistencia a fallos.

**Sesiones de usuario:** No hay una relación 1-a-1 entre sesiones de usuario y procesos del servidor.
- Cualquier proceso disponible puede ejecutar la solicitud de un callback.
- Gunicorn distribuye las solicitudes de usuarios entre procesos no ocupados.

```bash
gunicorn app:server --workers 8
```

## Why Global Variables Will Break Your App

- **Multi-usuario y sesiones independientes:** Dash permite que múltiples usuarios accedan a la aplicación simultáneamente, cada uno con su propia sesión.
- **Problema con variables globales:** Modificar una variable global en un callback puede afectar a las sesiones de otros usuarios, ya que no hay control sobre quién la modifica primero.
- **Múltiples workers:** Dash puede ejecutarse con varios workers para procesar callbacks en paralelo, lo cual se logra usando herramientas como gunicorn.
- **Memoria no compartida:** Al usar múltiples workers, la memoria de cada uno es independiente, por lo que las modificaciones a variables globales en un worker no se reflejan en los demás.
- **Ejemplo problemático:** Se muestra un ejemplo de código que no funcionará de manera fiable porque un callback modifica una variable global.

## Storing Shared Data

Para compartir datos de forma segura entre múltiples procesos o servidores, necesitamos almacenar los datos en algún lugar que sea accesible para cada uno de los procesos. Hay tres lugares donde puede almacenar estos datos:

- En la sesión del navegador del usuario, usando dcc.Store
- En el disco (por ejemplo, en un archivo o base de datos)
- En la memoria del lado del servidor (RAM) compartida entre procesos y servidores, como una base de datos de Redis. Dash Enterprise incluye bases de datos Redis integradas con un solo clic para este propósito.

Los siguientes ejemplos ilustran algunos de estos enfoques.

### Example 1 - Storing Data in the Browser with dcc.Store

Para guardar datos en la sesión del navegador del usuario:

- **Almacenamiento de datos en la sesión del navegador:** Permite guardar información temporal en el navegador del usuario utilizando dcc.Store.
- **Formato de datos:** La información debe convertirse a una cadena de texto (JSON) o datos binarios codificados en base64 antes de guardarla.
- **Alcance de la sesión:** Los datos solo están disponibles durante la sesión actual del usuario. Al abrir una nueva ventana, la aplicación volverá a calcular los datos.
- **Eficiencia:** No aumenta la memoria de la aplicación, pero puede generar tráfico de red.
- **Consideraciones de red:** Si se comparte mucha información (ej: 10MB), se enviará por la red en cada callback.
- **Solución:** Calcular agregaciones de antemano y transportar solo esos datos. Es probable que la aplicación no muestre los 10MB completos.
- **Ejemplo de uso:** Guardar resultados de procesamiento costoso para reutilizarlos en múltiples callbacks, evitando recalcularlos.

```bash
2.store.py
```

Note que:

- **Preparación de datos para almacenamiento:** Antes de guardar información en dcc.Store, se necesita convertirla a un formato legible por el ordenador, como una cadena JSON.
- **Almacenamiento y reutilización:** dcc.Store funciona como un contenedor temporal. Los datos procesados se guardan en dcc.Store como salida de un callback. Luego, otros callbacks pueden acceder a esos mismos datos como entrada, permitiendo su reutilización y evitando recalcularlos varias veces.


### Example 2 - Computing Aggregations Upfront

- **Costos de enviar datos por red:** Transferir grandes cantidades de datos calculados puede ser caro para la red.
- **Serialización JSON:** Convertir datos a JSON (para almacenamiento o transporte) también puede ser costoso.
- **Precomputar agregaciones:** Si la aplicación solo muestra una parte o un resumen de los datos procesados, conviene calcular previamente esas agregaciones y enviarlas a los callbacks restantes en lugar de los datos completos.

**Ejemplo con dcc.Store:** Se muestra un ejemplo donde se utilizan agregaciones precomputadas y dcc.Store para transportarlas a múltiples callbacks, evitando enviar los datos completos y costosos de procesar.


### Example 3 - Caching and Signaling

**Almacenamiento persistente:** Este ejemplo utiliza Redis a través de Flask-Cache para guardar "variables globales" del lado del servidor en una base de datos. Se accede a estos datos mediante una función (global_store()), cuyo resultado se almacena en caché y se identifica por sus argumentos de entrada.
**dcc.Store para señalización:** Se usa dcc.Store para enviar una señal a otros callbacks cuando finaliza el cálculo costoso.
**Alternativa a Redis:** En lugar de Redis, se puede guardar la información en el sistema de archivos (https://flask.palletsprojects.com/en/3.0.x/patterns/caching/).
**Eficiencia:** Esta señalización es eficiente porque permite que el cálculo costoso ocupe un solo proceso y se realice una única vez. Sin esta señal, cada callback podría terminar calculando todo en paralelo, bloqueando cuatro procesos en lugar de uno.
**Reutilización en nuevas sesiones:** Otro beneficio es que las sesiones futuras pueden usar el valor precalculado. Esto funciona bien para aplicaciones con pocas entradas.

```bash
cache.py # aplicacion

gunicorn app:server --workers 8

gunicorn cache:server --workers 8

gunicorn cuatro_cache:server --workers 8

```

Nota: Debe estar instalado redis

```bash

pip install redis

sudo service redis-server start

```

- **Simulación de proceso costoso:** Se usa un retraso de 3 segundos para simular un proceso lento.
- **Rendimiento inicial: La carga inicial de la aplicación tarda 3 segundos en renderizar 4 gráficos debido al cálculo costoso.
- **Eficiencia del cálculo:** El cálculo inicial solo bloquea un proceso.
- **Señalización y renderizado paralelo:** Una vez finalizado el cálculo, se envía una señal y 4 callbacks se ejecutan en paralelo para renderizar los gráficos, estos obtienen los datos de la "memoria global del servidor" (caché de Redis o sistema de archivos).
- **Procesos múltiples:** Se configura processes=6 para ejecutar callbacks en paralelo. En producción, se usa gunicorn con una sintaxis similar. Si no se usan procesos múltiples, los gráficos se actualizarán secuencialmente.
- **Multiproceso vs Multihilo:** Al usar procesos múltiples, se configura threaded=False ya que Flask no soporta ambos simultáneamente.
- **Beneficios del caché:** Seleccionar un valor del desplegable es rápido si ya se ha seleccionado antes, porque se obtiene del caché.
- **Recarga y nuevas sesiones:** Recargar la página o abrir la aplicación en una ventana nueva también es rápido porque el estado inicial y el cálculo costoso ya están pre-calculados.

### Example 4 - User-Based Session Data on the Server

- **Aislamiento de datos por sesión:** El ejemplo anterior guardaba cálculos de forma accesible para todos los usuarios. A veces se quiere mantener la información aislada por sesión, para evitar que los datos de un usuario afecten a los de otro.

**Métodos de aislamiento:**

- Almacenamiento en dcc.Store (ver primer ejemplo).
- Guardar datos en caché con un identificador de sesión y acceder a ellos usando ese identificador. Este método suele ser más rápido que dcc.Store porque los datos se guardan en el servidor.

**Ejemplo:**

- Almacena datos en la caché del sistema de archivos usando flask_caching. También permite caché en memoria o bases de datos como Redis.
- Serializa los datos como JSON.
    - Para DataFrames de Pandas, se recomienda usar Apache Arrow para serializar más rápido o Plasma para tamaños más pequeños.
- Limita el almacenamiento de datos de sesión a la cantidad esperada de usuarios concurrentes para evitar saturar la caché.
- Genera identificadores de sesión únicos y los guarda en dcc.Store en cada carga de página. Esto asegura que cada usuario tenga datos únicos en su sesión.









