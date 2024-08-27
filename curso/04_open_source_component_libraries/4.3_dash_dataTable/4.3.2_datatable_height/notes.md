# DataTable Height

De forma predeterminada, la altura de la tabla se ampliará para mostrar hasta 250 filas. Después de 250 filas, la tabla mostrará una interfaz de paginación que permite ver hasta 250 filas a la vez.

## Setting Table Height with Pagination

Si utiliza paginación, puede controlar la altura mostrando menos filas a la vez. En lugar de 250 filas, podría mostrar 10 filas a la vez. De forma predeterminada y sin ajuste, cada fila ocupa 30 px. Por lo tanto, 10 filas con un encabezado establecerían la tabla en 330 px de alto. La interfaz de paginación en sí tiene alrededor de 60 px de alto.

```bash
1.setting_table_height_with_pagination.py
```

## Setting Table Height with Vertical Scroll

Si la tabla contiene menos de aproximadamente 1000 filas, una opción es eliminar la paginación, restringir la altura y mostrar una barra de desplazamiento vertical.

```bash
2.setting_table_height_with_vertical_scroll.py
```

Si tiene más de 1000 filas, el navegador se ralentizará al intentar representar la tabla. Con más de 1000 filas, recomendamos cambiar a paginación de navegador o servidor (como se indica más arriba) o virtualización (como se indica más abajo).

## Vertical Scroll With Pagination

Si tiene más de ~1000 filas, puede mantener la paginación en la parte inferior de la tabla, restringir la altura y mostrar una barra de desplazamiento vertical.

```bash
3.vertical_scroll_with_pagination.py
```

## Vertical Scroll With Fixed Headers

También puedes fijar los encabezados para que el contenido de la tabla se desplace pero los encabezados permanezcan visibles.

```bash
4.vertical_scroll_with_fixed_headers.py
```

## Limitations


