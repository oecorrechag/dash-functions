# dcc.Store

El componente **dcc.Store** se utiliza para almacenar datos JSON en el navegador.

Para obtener más información y ejemplos, consulte la Parte 4 del tutorial de Dash sobre cómo compartir datos entre calbacks.

## Share Data Between Callbacks
 
```bash
1.share_data_between_callbacks.py
```

## Store Clicks

```bash
2.store_clicks.py
```

## Retrieving the Initial Store Data

Si utiliza la propiedad data como output, no podrá obtener los datos iniciales al cargarla. Para contrarrestar esto, puede utilizar modified_timestamp como input y data como estado.

## Storage Limitations

- El espacio de almacenamiento máximo del navegador está determinado por los siguientes factores:
    - Móvil o portátil
    - El navegador, en el que se implementa un algoritmo sofisticado dentro de la Gestión de cuotas
    - Codificación de almacenamiento donde UTF-16 puede terminar ahorrando solo la mitad del tamaño de UTF-8
    - En general, es seguro almacenar hasta 2 MB en la mayoría de los entornos y entre 5 y 10 MB en la mayoría de las aplicaciones exclusivas de escritorio.
-   modified_timestamp es de solo lectura
