# dcc.Tooltip

**dcc.Tooltip** le ofrece una información sobre herramientas que apunta a una ubicación precisa de píxeles en la página. Fue diseñado principalmente para brindar mayor flexibilidad a la información flotante incorporada en las figuras de dcc.Graph, pero se puede usar con cualquier componente que dibuje diagramas o gráficos en la página.

## Using URLs to Load Images and Text in Tooltips

A continuación se muestra un ejemplo de creación de una información sobre herramientas con imágenes y texto, cargados por sus URL:

```bash
1.images_and_text_in_tooltips.py
```

## Visualizing t-SNE Plot of MNIST Images

El siguiente ejemplo visualiza los resultados de t-SNE de imágenes de dígitos escritos a mano del conjunto de datos MNIST, con las imágenes mostradas en la información sobre herramientas cuando se pasa el mouse sobre ellas:

```bash
2.plot_of_MNIST_images.py
```

## Using base64 Encoded Images

Este ejemplo utiliza la biblioteca **PIL** de Python para codificar una imagen en formato base64 y luego la devuelve desde un callback:

```bash
3.base64_encoded_images.py
```

## Loading Text

El texto de carga de la información sobre herramientas se puede configurar mediante **loading_text**, que está configurado como "Cargando..." de manera predeterminada. Aquí se muestra un ejemplo que utiliza el parámetro **loading_text** junto con un callback de interfaz.

```bash
4.loading_text.py
```

## Styling Tooltip with Background and Border Color



