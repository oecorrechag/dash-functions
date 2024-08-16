# dcc.Tabs

Los componentes **dcc.Tabs** y **dcc.Tab** se pueden utilizar para crear secciones con pestañas en su aplicación. El componente dcc.Tab controla el estilo y el valor de cada pestaña, y el componente dcc.Tabs contiene una colección de componentes dcc.Tab.

## Method 1. Content as Callback

Adjunte un callback a la propiedad de valor Tabs y actualice la propiedad children de un contenedor en su callback.

```bash
1.content_as_callback.py
```

En el ejemplo anterior, nuestro callback contiene todo el contenido. En la práctica, mantendremos el contenido de la pestaña en archivos separados e importaremos los datos. Para ver un ejemplo, consulte el Tutorial de URL y aplicaciones de varias páginas.

https://dash.plotly.com/urls

## Method 2. Content as Tab Children

En lugar de mostrar el contenido a través de un callback, puede incrustar el contenido directamente como propiedad secundaria en el componente Pestaña:

```bash
2.content_as_tab_children.py
```

Tenga en cuenta que este método tiene una desventaja: requiere que calcule la propiedad children de cada pestaña individual por adelantado y envíe todo el contenido de la pestaña a través de la red a la vez. El método de callback le permite calcular el contenido de la pestaña sobre la marcha (es decir, cuando se hace clic en la pestaña).

# Styling the Tabs Component

## With CSS Classes

El estilo del componente Pestañas (y Tab) se puede realizar mediante clases CSS proporcionando las suyas propias a la propiedad className:

```bash
3.with_CSS_classes.py
```

Observa cómo el contenedor de las pestañas también se puede diseñar suministrando una clase a la propiedad parent_className, que usamos aquí para dibujar un borde debajo de ella, posicionando las pestañas reales (con relleno) más en el centro. También agregamos display: flex y justify-content: center a los componentes de pestaña regulares, de modo que las etiquetas con múltiples líneas no interrumpan el flujo del texto. El archivo CSS correspondiente (assets/tabs.css) se ve así. Guarda el archivo en una carpeta de activos (puede tener el nombre que quieras). Dash incluirá automáticamente este CSS cuando se cargue la aplicación. Obtén más información en Agregar CSS y JS y Anular la plantilla de carga de página.

```css
.custom-tabs-container {
    width: 85%;
}
.custom-tabs {
    border-top-left-radius: 3px;
    background-color: #f9f9f9;
    padding: 0px 24px;
    border-bottom: 1px solid #d6d6d6;
}

.custom-tab {
    color:#586069;
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    border-top: 3px solid transparent !important;
    border-left: 0px !important;
    border-right: 0px !important;
    border-bottom: 0px !important;
    background-color: #fafbfc;
    padding: 12px !important;
    font-family: "system-ui";
    display: flex !important;
    align-items: center;
    justify-content: center;
}
.custom-tab--selected {
    color: black;
    box-shadow: 1px 1px 0px white;
    border-left: 1px solid lightgrey !important;
    border-right: 1px solid lightgrey !important;
    border-top: 3px solid #e36209 !important;
}
```

## With Inline Styles

Una alternativa a proporcionar clases CSS es proporcionar diccionarios de estilo directamente:

```bash
4.with_inline_styles.py
```

Por último, puedes configurar los colores de los componentes de las pestañas en la propiedad de color, especificando los colores "border", "primary" y "background" en un diccionario. ¡Asegúrate de configurarlos todos, si los estás usando!

```bash
5.with_inline_styles.py
```

