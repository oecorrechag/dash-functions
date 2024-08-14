# dcc.Tab

Los componentes dcc.Tab y dcc.Tabs se pueden utilizar para crear secciones con pestañas en su aplicación. El componente Tab controla el estilo y el valor de cada pestaña y el componente Tabs contiene una colección de componentes Tab.

## Method 1. Content as Callback

Adjunte un callback a la propiedad de valor Tabs y actualice la propiedad children de un contenedor en su callback.

```bash
1.content_as_callback.py
```

## Method 2. Content as Tab Children

En lugar de mostrar el contenido a través de un callback, puede incrustar el contenido directamente como propiedad secundaria en el componente Pestaña:

```bash
2.content_as_tab_children.py
```

Tenga en cuenta que este método tiene una desventaja: requiere que calcule la propiedad children de cada pestaña individual por adelantado y envíe todo el contenido de la pestaña a través de la red a la vez. El método de callback le permite calcular el contenido de la pestaña sobre la marcha (es decir, cuando se hace clic en la pestaña).

# Styling the Tabs Component


