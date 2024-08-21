# dcc.Upload

El componente **dcc.Upload** permite que los usuarios de su aplicación carguen archivos, como hojas de cálculo de Excel o imágenes, en su aplicación. Su aplicación Dash puede acceder al contenido de una carga escuchando la propiedad contents del componente **dcc.Upload**.

contents es una cadena codificada en base64 que contiene el contenido de los archivos, sin importar el tipo de archivo: archivos de texto, imágenes, archivos .zip, hojas de cálculo de Excel, etc.

## Displaying Uploaded Spreadsheet Contents

A continuación se muestra un ejemplo que analiza archivos CSV o Excel y muestra los resultados en una Dash DataTable.

```bash
1.displaying_uploaded_spreadsheet_contents.py
```

## Displaying Uploaded Images

El siguiente ejemplo responde a las cargas de imágenes mostrándolas en la aplicación con el componente html.Img.

```bash
2.displaying_uploaded_images.py
```

## Styling the Upload Component
