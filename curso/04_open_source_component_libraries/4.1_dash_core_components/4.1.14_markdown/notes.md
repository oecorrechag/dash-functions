# dcc.Markdown

dcc.Markdown es un componente para renderizar texto Markdown, lo que permite formatear y diseñar fácilmente el contenido de texto en su aplicación Dash.

## Headers

```bash
1.headers.py
```

## Emphasis

```bash
2.emphasis.py
```

## Lists

```bash
3.lists.py
```

## Block Quotes

```bash
4.block_quotes.py
```

## Links

```bash
5.links.py
```

## Link Target

Con link_target puedes configurar el atributo HTML target para los enlaces en tu componente Markdown. En este ejemplo, configuramos link_target="_blank". Cuando se selecciona, el enlace de la Guía del usuario de Dash se abre en una nueva pestaña o ventana.

```bash
6.link_target.py
```

## Inline Code

```bash
7.inline_code.py
```

De forma predeterminada, solo se admiten determinados lenguajes en dcc.Markdown. Para obtener más detalles sobre cómo personalizar los idiomas y los esquemas de color, consulte Resaltado de sintaxis con Markdown en Cómo agregar CSS y JS y cómo anular la plantilla de carga de página.

## LaTeX

dcc.Markdown admite la representación de LaTeX. Utiliza la versión 3.2 de MathJax y se puede habilitar configurando mathjax=True en el componente. Para contenido matemático en línea, utilice delimitadores $. Para contenido matemático que desee mostrar como un bloque (normalmente contenido de varias líneas), utilice $$. Si necesita un $ literal, utilice la entidad HTML &#36;

```bash
8.laTeX.py
```
