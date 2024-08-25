# Dash DataTable

Dash DataTable (**dash.dash_table.DataTable**) es un componente de tabla interactivo diseñado para ver, editar y explorar grandes conjuntos de datos.

Este componente se escribió desde cero en React.js específicamente para la comunidad Dash. Su API se diseñó para que sea ergonómica y su comportamiento es completamente personalizable a través de sus propiedades. DataTable se representa con el marcado HTML semántico estándar <table/>, lo que lo hace accesible, responsivo y fácil de diseñar.

Importar DataTable con:

```python
from dash import dash_table
```

```bash
1.dash_datatable.py
```

Las propiedades de datos y columnas son los dos primeros argumentos de dash_table.DataTable. Puede configurarlas con argumentos posicionales o de palabras clave. Los siguientes ejemplos definen la misma DataTable:

```python
dash_table.DataTable(
    df.to_dict('records'),
    [{"name": i, "id": i} for i in df.columns]
)
```

```python
dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{"name": i, "id": i} for i in df.columns]
)
```

También puede omitir columnas. Cuando no se proporciona ningún argumento de columnas, las columnas se generan automáticamente en función de la primera fila de datos.

```python
dash_table.DataTable(df.to_dict('records'))
```

## Table with Click Callback

```bash
2.table_with_click_callback.py
```


