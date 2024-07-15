# Duplicate Callback Outputs

```bash
Nuevo en Dash 2.9: Dash admite el argumento enable_duplicate=True para permitir que múltiples devoluciones de llamada apunten al mismo resultado. Consulte el ejemplo "Configuración de enable_duplicate en salidas duplicadas" a continuación.
```

El Output de un callback duplicado se produce cuando el mismo par component-property es una salida en más de un callback. Un par component-property significa la identificación del componente y la propiedad. En este componente **html.H1**, el par component-property es 'app-heading', 'children':

```bash
html.H1(children='Analytics app', id='app-heading')
```

If you add **'app-heading', 'children'** as an Output on two callbacks in your app you'll get a "Duplicate callback outputs" error when running in debug mode as the the default behavior of callbacks is that a component/property pair can only be the Output of one callback.



el callback

los callbacks

un callback

callback