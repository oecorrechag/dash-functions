# dcc.Input

El componente **dcc.Input** crea campos de entrada para texto, números, contraseñas y más, lo que permite una entrada dinámica del usuario.

## Supported Input Types

```bash
1.supported_input_types.py
```

## Debounce Delays the Input Processing

```bash
2.input_processing.py
```

## Number Input

El tipo de número ahora es similar al comportamiento de entrada nativo de HTML5 en todos los navegadores. También aplicamos una conversión de números estricta en los callbakcs: los números válidos se convierten en los tipos de números correspondientes y los números no válidos se convierten en Ninguno. Por ejemplo:

```python
dcc.Input(id='range', type='number', min=2, max=10, step=1)
```

```bash
3.number_input.py
```
