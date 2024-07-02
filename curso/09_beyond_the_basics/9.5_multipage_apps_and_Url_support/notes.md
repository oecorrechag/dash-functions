# Multi-Page Apps and URL Support


Dash presenta aplicaciones web como una "aplicación de una sola página". Al utilizar dcc.Link, la aplicación no se recarga completamente al navegar, lo que hace que la navegación sea muy rápida. Con Dash, puede crear aplicaciones de varias páginas utilizando componentes y callbacks dcc.Location y dcc.Link.

Dash Pages utiliza estos componentes y abstrae la lógica de callback necesaria para el enrutamiento de URL, lo que facilita la puesta en marcha de una aplicación de varias páginas. 

## Dash Pages

Dash Pages está disponible desde la versión 2.5.0 de Dash. Implementa funciones para simplificar la creación de una aplicación de varias páginas, manejando el enrutamiento de URL y ofreciendo una manera fácil de estructurar y definir las páginas de su aplicación.

Hay tres pasos básicos para crear una aplicación de varias páginas con Dash Pages:

- Cree archivos .py individuales para cada página de su aplicación y colóquelos en un directorio /pages.
- En cada uno de estos archivos de página:
    - Agrega un dash.register_page(__name__), que le indica a Dash que esta es una página en tu aplicación.
    - Defina el contenido de la página dentro de una variable llamada **layout** o una función llamada **layout** que devuelve el contenido.
- En el archivo principal de tu aplicación, app.py:
    - Al declarar su aplicación, establezca use_pages en True: app = Dash(__name__, use_pages=True)
    - Agregue dash.page_container en el diseño de su aplicación donde desea que se muestre el contenido de la página cuando un usuario visita una de las rutas de la página de la aplicación.

### Example: Simple Multi-Page App with Pages

Así es como se ve la estructura de una aplicación de tres páginas con Dash Pages:

```bash
- app.py
- pages
   |-- analytics.py
   |-- home.py
   |-- archive.py
```

Tiene el archivo app.py principal, que es el punto de entrada a nuestra aplicación de varias páginas (y en el que incluimos dash.page_container) y tres páginas en nuestro directorio de páginas.

Notas:

- path — Llamamos a dash.register_page en cada una de las tres páginas de nuestra aplicación. Para dos de las páginas, no configuramos una propiedad **path**. Si no configura la propiedad de **path**, se genera automáticamente en función del *nombre del módulo*. Entonces, el diseño de archives.py se muestra cuando un usuario accede a /archivos. De manera similar, el diseño de Analytics.py se muestra cuando el usuario accede a /analytics. Cuando llamamos a dash.register_page para home.py, configuramos la propiedad de ruta. Para home.py configuramos la propiedad de ruta porque no queremos que el contenido se muestre cuando el usuario vaya a /home, sino cuando el usuario vaya a la página de inicio: /

- page_registry — Las páginas que incluyen una llamada a **dash.register_page** se agregan al registro de páginas de nuestra aplicación. Este es un **OrderedDict** del que podemos extraer información sobre las páginas de nuestra aplicación. En nuestro app.py recorremos todas las páginas de nuestra aplicación (en dash.page_registry.values()) y agregamos enlaces para cada una. También podemos seleccionar estos enlaces individualmente desde dash.page_registry. La página con / como ruta siempre está en el índice 0 en el dict. Las demás páginas están en orden alfabético.

- page_container — app.py tiene un **dash.page_container**. Aquí es donde se muestra el contenido de la página cuando un usuario navega a la ruta de esa página.

```bash
1.ejemplo1
```

## Layout

En el ejemplo anterior, definimos el diseño de cada página usando una variable llamada diseño. Por ejemplo, en home.py arriba:

```bash
2.ejemplo2
```

## dash.register_page

Llamar a **dash.register_page** dentro de un archivo es la forma en que Dash sabe incluir el archivo como una página en su aplicación de varias páginas.

In this case, Dash generates the **path** the page is for, its title, and the link name based on the module name.

```bash
analytics.py -> /analytics -> title: Analytics
```

```bash
3.ejemplo3
```

## Dash Page Registry

Cualquier página que llame a **dash.register_page** se agrega a un registro de páginas para su aplicación.

El registro de la página es un **OrderedDict** llamado **dash.page_registry**. Cada entrada del registro tiene información para una página, incluidos los valores de propiedad establecidos cuando se llamó a **dash.register_page** y los valores inferidos por Dash. Al igual que con cualquier dict, puedes acceder y utilizar sus datos en tu código.

Aquí accedemos a la ruta de nuestros análisis y la usamos en un dcc.Link en app.py:

```bash
html.Div(dcc.Link('Dashboard', href=dash.page_registry['pages.analytics']['path']))
```

Para acceder a **dash.page_registry** desde un archivo en el directorio de páginas, deberá usarlo dentro de una función.

Aquí tenemos dos archivos dentro del directorio de páginas: side_bar.py y topic_1.py. La página topic_1 importa una barra lateral de side_bar.py. Observe cómo la función dentro de side_bar.py accede a **dash.page_registry**. Si esto no estuviera dentro de una función, la aplicación no funcionaría porque **dash.page_registry** no estaría listo cuando se carga la página.

```bash
4.ejemplo4
```

Nota: no funciona -- revisar.

## Dash Page Registry Order

De forma predeterminada, una página con una ruta definida como / se agrega al registro en el índice 0. Luego se agregan otras páginas en orden alfabético según el nombre del archivo.

También puede especificar el orden de las páginas en dash.page_registry configurando la propiedad de orden en cada página:

```bash
dash.register_page(__name__, order=3)
```

Si establece la propiedad de orden en una o más páginas, las páginas se agregan al registro:

- En el orden se especifican con la propiedad de pedido.
- Después de eso, en orden alfabético (para páginas sin la propiedad de orden establecida).

Configurar el orden puede resultar útil cuando desea poder recorrer los enlaces al crear una barra lateral o un encabezado de forma dinámica.

## Default and Custom 404

Si un usuario va a una ruta que no ha sido declarada en una de las páginas de su aplicación, Pages muestra un mensaje predeterminado '404 - Página no encontrada' al usuario.

Esta página se puede personalizar. Coloque un archivo llamado not_found_404.py en el directorio de páginas de su aplicación, agregue dash.register_page(__name__) al archivo y defina el contenido para el 404 personalizado dentro de una variable o función de diseño:

```bash
5.ejemplo5
```

## Variable Paths

Puede capturar variables dinámicas en la ruta utilizando el parámetro **path_template**. Especifique partes dinámicas de su URL colocándolas dentro de **nombre_variable**. nombre_variable será el argumento de la palabra clave con nombre pasado a su función de diseño. Los valores que recibe la función de diseño de la URL son siempre de tipo str.

Ejemplo: ruta de variable única








callback


