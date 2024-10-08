# DataTable - Number Formatting

**DataTable** ofrece amplias posibilidades de formato y localización de números con la propiedad de columnas anidadas format y la propiedad de localización de toda la tabla **locale_format**.

La mayoría del formato y la localización de las columnas se pueden realizar a través de los asistentes de Python **dash_table.FormatTemplate** y **dash_table.Format**, pero también es posible utilizar el especificador **d3-format** y la configuración regional directamente.

## Using FormatTemplate

**FormatTemplate** proporciona las siguientes plantillas predefinidas:
- Dinero
- Porcentaje

```bash
1.using_formattemplate.py
```

## Using Format Helper

### Group

La agrupación se define con el formato de propiedades anidadas group y groups. group toma los valores True o Group.yes para alternar la agrupación de dígitos. groups toma una lista de números que se utilizan para definir el patrón de agrupación de dígitos. Si el número tiene más dígitos que los definidos en groups, recorre la lista nuevamente hasta que se queda sin números para agrupar.

```bash
2.group.py
```

### Align and Fill

La alineación y el relleno se definen con las propiedades anidadas de formato align, fill y padding_width. El asistente align toma los valores left, right y center. fill es un solo carácter que se utilizará para el relleno. padding_width es la longitud mínima de la cadena completa. Si el número formateado requiere más espacio del que permite padding_width, lo hará.

```bash
3.align_and_fill.py
```

### Padding and Padding Width

El relleno y el ancho de relleno se definen con las propiedades anidadas de formato padding y padding_width y se comportan de manera similar a fill y padding_width, pero no permiten la alineación.

```bash
4.padding_and_padding_width.py
```

### Precision and Scheme

```bash
5.precision_and_scheme.py
```

### Sign 

Cuándo mostrar un signo y qué tipo de signo mostrar se define con el formato prop. anidado sign. El asistente Sign toma valores negativos (mostrar signo cuando es negativo), positivos (mostrar siempre signo), paréntesis (cuando es negativo)

```bash
6.sign.py
```

### Symbol

La visualización de símbolos se define con el formato prop anidado symbol y los símbolos de prefijo/sufijo se definen con el formato prop anidado symbol. El ayudante Symbol toma los valores sí y no. El formato prop anidado symbol es una lista de cadenas de longitud 2 con el formato [prefijo, sufijo]. Las cadenas en symbol pueden tener cualquier longitud.

```bash
7.symbol.py
```

### Localization

```bash
8.localization.py
```
