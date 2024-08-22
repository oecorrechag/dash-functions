# Dash HTML Components

Dash es un marco de trabajo para aplicaciones web que ofrece abstracción pura de Python en torno a HTML, CSS y JavaScript.

En lugar de escribir HTML o usar un motor de plantillas HTML, puedes componer tu diseño usando Python con el módulo Componentes HTML de Dash (dash.html).

Importa dash.html con:

```python
from dash import html
```

El módulo Componentes HTML de Dash es parte de Dash y encontrarás el código fuente en el repositorio de GitHub de Dash.

https://github.com/plotly/dash

A continuación se muestra un ejemplo de una estructura HTML simple:

```python
from dash import html

html.Div([
    html.H1('Hello Dash'),
    html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
    ])
])
```

que se convierte (entre bastidores) en el siguiente HTML en su aplicación web:

```html
<div>
    <h1>Hello Dash</h1>
    <div>
        <p>Dash converts Python classes into HTML</p>
        <p>This conversion happens behind the scenes by Dash's JavaScript front-end</p>
    </div>
</div>
```

Si no te sientes cómodo con HTML, ¡no te preocupes! Puedes lograr el 95 % del proceso con solo unos pocos elementos y atributos.

Si quieres usar Markdown en tu aplicación, puedes usar el componente Markdown de Dash Core Components:

```markdown
from dash import dcc

dcc.Markdown('''
#### Dash and Markdown

Dash supports [Markdown](http://commonmark.org/help).

Markdown is a simple way to write and format text.
It includes a syntax for things like **bold text** and *italics*,
[links](http://commonmark.org/help), inline `code` snippets, lists,
quotes, and more.
''')
```

## HTML Component Properties

Si utiliza componentes HTML, también tendrá acceso a propiedades como estilo, clase e id. Todos estos atributos están disponibles en las clases de Python.

Los elementos HTML y las clases Dash son prácticamente iguales, pero existen algunas diferencias clave:

- La propiedad de estilo es un diccionario
- Las propiedades del diccionario de estilo están en mayúsculas y minúsculas
- La clave de clase se renombra como className
- Las propiedades de estilo en unidades de píxeles se pueden proporcionar simplemente como números sin la unidad px

```python
from dash import html

html.Div([
    html.Div('Example Div', style={'color': 'blue', 'fontSize': 14}),
    html.P('Example P', className='my-class', id='my-p-element')
], style={'marginBottom': 50, 'marginTop': 25})
```

Ese código Dash representará este marcado HTML:

```html
<div style="margin-bottom: 50px; margin-top: 25px;">

    <div style="color: blue; font-size: 14px">
        Example Div
    </div>

    <p class="my-class", id="my-p-element">
        Example P
    </p>

</div>
```

## n_clicks and disable_n_clicks





