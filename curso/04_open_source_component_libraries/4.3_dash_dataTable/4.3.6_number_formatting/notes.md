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

