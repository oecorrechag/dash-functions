# Dash Core Components

Dash se envía con componentes supercargados para interfaces de usuario interactivas.

El módulo Dash Core Components (dash.dcc) le brinda acceso a muchos componentes interactivos, incluidos menús desplegables, listas de verificación y controles deslizantes.

Importe dash.dcc con:

```python
from dash import dcc
```

El módulo dcc es parte de Dash y encontrará su fuente en el repositorio de Dash GitHub.

https://github.com/plotly/dash

## Dropdown

```bash
1.dropdown.py
```

```bash
2.dropdown.py
```

## Slider

```bash
3.slider.py
```

```bash
4.slider.py
```

## RangeSlider

```bash
5.rangeslider.py
```

```bash
6.rangeslider.py
```

## Input

```bash
7.input.py
```

## Textarea

```bash
8.textarea.py
```

## Checkboxes

```bash
9.checkboxes.py
```

```bash
10.checkboxes.py
```

## Radio Items

```bash
11.radio_tems.py
```

```bash
12.radio_tems.py
```

## Button

En realidad, no hay ningún componente de botón en dash_core_components. El componente regular dash_html_components.Button hace el trabajo bastante bien, pero lo hemos incluido aquí porque este es el único componente html simple que se usa comúnmente como Input de un callback:

```bash
13.button.py
```

## DatePickerSingle

```bash
14.date_picker_single.py
```

## DatePickerRange

```bash
15.date_picker_range.py
```

## Markdown

```bash
16.markdown.py
```

## Dash and Markdown

Dash admite Markdown. Markdown es una forma sencilla de escribir y formatear texto. Incluye una sintaxis para cosas como texto en negrita y cursiva, enlaces, fragmentos de código en línea, listas, citas y más.

## Upload Component

El componente **dcc.Upload** permite a los usuarios cargar archivos en su aplicación mediante arrastrar y soltar o el explorador de archivos nativo del sistema.

## Download Component

El componente **dcc.Download** permite a los usuarios descargar archivos desde su aplicación a través de su navegador.

```bash
17.component.py
```

## Tabs

Los componentes **Tabs** y **Tab** se pueden usar para crear secciones con pestañas en su aplicación.

```bash
18.tabs.py
```

## Graphs

El componente **Graph** comparte la misma sintaxis que la biblioteca de código abierto plotly.py. 

```bash
19.graphs.py
```

## ConfirmDialogProvider

El componente **dcc.ConfirmDialogProvider** envía un **dcc.ConfirmDialog** cuando un usuario hace clic en los elementos secundarios del componente. En el siguiente ejemplo, se proporciona un html.Button como elemento secundario de dcc.ConfirmDialogProvider y cuando se hace clic en el botón, se muestra el cuadro de diálogo.

```bash
20.confirm_dialog_provider.py
```

## Store

El componente de la tienda se puede utilizar para conservar datos en el navegador del visitante. Los datos están dirigidos al usuario que accede a la página.

Tres tipos de almacenamiento (propiedad tipo_almacenamiento):

- memoria: predeterminado, conserva los datos mientras la página no se actualice.
- local: conserva los datos hasta que se borre manualmente.
- sesión: conserva los datos hasta que se cierre el navegador/pestaña.

En este ejemplo, el callback guarda el valor del botón de opción seleccionado en un almacén de memoria. Cuando el valor en la tienda cambia, el segundo callback genera el nuevo valor y la marca de tiempo modificada en un componente html.Div.

```bash
21.store.py
```

## Loading Component

El componente Cargando se puede utilizar para envolver componentes para los que desea mostrar un control giratorio, si tardan demasiado en cargarse.

Para ello, comprueba si alguno de los elementos secundarios de los componentes de carga tiene un conjunto de propiedades de estado de carga donde is_loading es verdadero. Si es verdadero, mostrará uno de los controles giratorios CSS integrados.

Este ejemplo muestra una rueda giratoria cada vez que un usuario selecciona un botón de opción, ya que la devolución de llamada tarda 2 segundos en actualizar el componente html.Div (id=loading-demo) dentro del componente dcc.Loading.

```bash
22.loading_component.py
```

## Location

El componente de ubicación representa la barra de ubicaciones en su navegador web. A través de sus propiedades href, nombre de ruta, búsqueda y hash, puedes acceder a diferentes partes de la URL de tu aplicación. Por ejemplo, dada la URL http://127.0.0.1:8050/page-2?a=test#quiz:

- href = "http://127.0.0.1:8050/page-2?a=test#quiz"
- pathname = "/page-2"
- search = "?a=test"
- hash = "#quiz"

```python
dcc.Location(id="url", refresh=false)
```
