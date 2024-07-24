# dcc.Clipboard

El componente **dcc.Clipboard** copia texto al portapapeles del usuario con un solo clic.

Encuentre algunos ejemplos de uso a continuación.

## Simple Clipboard Example

La forma más sencilla de activar la copia es mediante la propiedad target_id. ¡No se requiere callback! Coloque **dcc.Clipboard** en el diseño donde desea ubicar el ícono de copia. Especifique el target_id del componente con el texto para copiar. En este ejemplo, el contenido de la propiedad value de **dcc.Textarea** se copia al portapapeles.

```bash
1.simple_clipboard.py
```

## Clipboard Icon inside a Scrollable Div

El estilo y el nombre de clase se pueden utilizar para cambiar el diseño o la posición del icono de copia. Este ejemplo muestra el icono colocado en la esquina superior derecha de un div desplazable.

```bash
2.clipboard_icon.py
```

## Updating the Clipboard Text in a Callback

Cuando no se especifica **target_id**, el contenido de la propiedad de **text** se copia al portapapeles. Esto funciona bien con componentes como DataTable donde es posible que desee personalizar el texto en una devolución de llamada. En este ejemplo, el marco de datos se convierte en texto con pandas **to_csv()**. Consulte la documentación de pandas para conocer otras opciones de formato, como incluir o excluir encabezados.

```bash
3.updating_clipboard.py
```

## Limitations

Este componente utiliza la **API** del Portapapeles. Esta función está disponible solo en **contextos seguros** (HTTPS), en algunos o todos los navegadores compatibles. Cuando la API del Portapapeles no está disponible, el icono no aparecerá en la aplicación y se escribirá un mensaje de advertencia en la consola.

Actualmente, **dcc.Clipboard** solo admite copiar texto al portapapeles. No admite pegar ni otras operaciones del portapapeles.

https://dash.plotly.com/dash-core-components/clipboard
