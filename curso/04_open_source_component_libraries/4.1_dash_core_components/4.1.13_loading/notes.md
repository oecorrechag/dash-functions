# dcc.Loading

El componente **dcc.Loading** muestra un indicador de carga personalizable hasta que se haya procesado el componente envuelto.

## Basic Loading

A continuación se muestra un ejemplo simple en el que el componente de carga envuelve las salidas de un par de componentes de entrada.

- El callback para la primera entrada demuestra el uso básico con un componente de control predeterminado.
- El callback para la segunda entrada muestra cómo incluso los elementos secundarios anidados establecerán el estado de carga del componente envuelto.
- Hay 5 tipos de control integrados. El dcc.Loading que envuelve la segunda entrada usa type="circle"

```bash
1.basic_loading.py
```

## Delay Show and Delay Hide

Para evitar que el spinner parpadee rápidamente durante tiempos de carga rápidos, ajuste las propiedades delay_show y delay_hide.

En este ejemplo, el callback demora aproximadamente 100 milisegundos.

Pruebe lo siguiente:

- Presione el botón Cargar con ambos retrasos en 0. Observe que el indicador giratorio aparece brevemente.
- Para evitar que se muestre el indicador giratorio, aumente delay_show a 500
- Para extender el tiempo en que el indicador giratorio está visible, aumente delay_hide a 500 o más y configure delay_show en 0.

```bash
2.delay_hide.py
```

## Loading Overlay Style

De forma predeterminada, el indicador de giro oculta el componente envuelto durante la carga. Para que el componente envuelto sea visible y difumine el contenido, puede configurar el siguiente CSS en la propiedad overlay_style:

```bash
3.overlay_style.py
```

## Custom Spinner Component

En lugar de utilizar uno de los indicadores integrados, puede utilizar un componente Dash como indicador. Este ejemplo establece la propiedad custom_spinner en un componente que incluye un indicador de la biblioteca de componentes de arranque de Dash, pero puede utilizar cualquier componente para establecer la propiedad custom_spinner.

Tenga en cuenta que las propiedades type, fullscreen, debug, color, style y className son específicas de los tipos de indicadores integrados y no funcionan con componentes de indicadores personalizados. 

```bash
4.spinner_component.py
```

## Target Components

Utilice la propiedad target_components para especificar qué combinaciones de id. de componente y propiedad de componente que envuelve pueden activar el indicador de carga. El componente indicador se muestra solo cuando uno de los componentes y propiedades de destino ingresa al estado de carga.

target_components es un diccionario donde la clave es el id. de componente y el valor es el nombre de propiedad, o una lista de nombres de propiedad o "*"

Por ejemplo, esto mostrará el indicador solo cuando se esté actualizando la propiedad rowData de AgGrid.

```python
app.layout=dcc.Loading(
    html.Div([
        dag.AgGrid(id="grid"),
        html.Div(id="output-div")
    ]),
    target_components={"grid": "rowData" }
)
```

Esto mostrará el control giratorio mientras se actualiza cualquiera de las propiedades de la cuadrícula:

```python
target_components ={"grid": "*"}
```

Esto mostrará el indicador cuando se estén actualizando los datos de fila o las definiciones de columna de la cuadrícula:

```python
target_components ={"grid": ["rowData", "columnDefs"]}
```

En este ejemplo, el componente dcc.Loading envuelve dos salidas de callback, pero solo una activa el spinner.

```bash
5.target_components.py
```

## Manually Display Loading Spinner

Utilice la propiedad de visualización para mostrar u ocultar manualmente el indicador de carga. Establezca en "mostrar", "ocultar" o "automático" (valor predeterminado).

```bash
6.loading_spinner.py
```
