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

