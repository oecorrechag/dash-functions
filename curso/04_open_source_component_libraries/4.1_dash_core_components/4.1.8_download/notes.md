# dcc.Download

Con el componente **dcc.Download**, puede permitir que los usuarios descarguen archivos directamente desde su aplicación. Estos archivos incluyen (entre otros) hojas de cálculo, imágenes, archivos de texto, etc. **dcc.Download** abre un cuadro de diálogo de descarga cuando cambia la propiedad de datos.

Tenga en cuenta que los siguientes ejemplos utilizan el atributo **prevent_initial_call** para evitar que se activen los callbacks cuando se procesan inicialmente las entradas de la aplicación. Consulte callbacks avanzados para obtener más detalles.

## Downloading Content as Strings

A continuación se muestra un ejemplo de descarga de contenido como cadena, mientras se muestra el JSON sin formato:

```bash
1.downloading_content_as_strings.py
```

## Downloading a Dataframe as a CSV file

Para descargar marcos de datos, se admiten los distintos métodos de exportación de Pandas. A continuación, descargamos un marco de datos como CSV:

```bash
2.downloading_a_dataframe_as_a_CSV_file.py
```

## Downloading a Dataframe as an Excel file

Para descargar un marco de datos como un archivo Excel con Pandas, agregue xlsxwriter o openpyxl como una dependencia de la aplicación:

```bash
3.downloading_a_dataframe_as_an_EXCEL_file.py
```

## Downloading Images

Para descargar un archivo del disco, utilice **dcc.send_file**, teniendo cuidado de especificar la ruta del archivo.

```bash
4.downloading_images.py
```
