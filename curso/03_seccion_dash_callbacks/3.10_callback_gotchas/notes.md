# Callback Gotchas

```bash
Para aprovechar al máximo esta página, asegúrese de haber leído sobre las callbacks básicas en los Fundamentos de Dash.
```

Hay algunos aspectos de cómo funciona Dash que pueden resultar complicados, especialmente cuando se trata de callbacks. Esta página describe algunos errores comunes que puede encontrar al comenzar a crear aplicaciones Dash más complejas.

## Callbacks require their Inputs, States, and Output to be present in the layout

De forma predeterminada, Dash aplica validación a sus callbacks, lo que realiza comprobaciones como validar los tipos de argumentos de callbacks y verificar si los componentes de entrada y salida especificados realmente tienen las propiedades especificadas. Para una validación completa, todos los componentes dentro de su callbacks deben existir en el diseño cuando se inicia su aplicación y verá un error si no es así.

Sin embargo, en el caso de aplicaciones Dash más complejas que implican una modificación dinámica del diseño (como aplicaciones de varias páginas), no todos los componentes que aparecen en sus callbacks se incluirán en el diseño inicial. Puede eliminar esta restricción deshabilitando la validación de callbacks de esta manera:
