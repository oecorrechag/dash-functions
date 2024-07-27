# dcc.DatePickerSingle

**dcc.DatePickerSingle** es un componente para representar un calendario desde el cual el usuario puede seleccionar una fecha.

Puede utilizar cadenas en el formato **AAAA-MM-DD** u objetos de fecha del módulo datetime para proporcionar fechas a los componentes Dash. Se prefieren las cadenas porque ese es el formato que toman las fechas como argumentos de callback. Si está utilizando objetos de fecha, le recomendamos utilizar **datetime.date** para que no haya una parte de hora. **dcc.DatePickerSingle** acepta fechas con una parte de hora, pero esto puede resultar confuso, en particular para la llamada inicial de una devolución de llamada. Después de que el usuario elija una nueva fecha, no habrá una parte de hora, solo la fecha. Si ya tiene un objeto **datetime.datetime**, puede convertirlo con **date()**.

## Month and Display Format

La propiedad **month_format** determina cómo se muestran los encabezados del calendario cuando se abre el calendario. La propiedad **display_format** determina cómo se muestran las fechas seleccionadas en el componente **dcc.DatePickerSingle**.

Ambas propiedades se configuran a través de cadenas que utilizan una combinación de cualquiera de los siguientes tokens.

![options](images/options.png)

## Simple DatePickerSingle Example

Este es un ejemplo simple de un componente **dcc.DatePickerSingle** vinculado a un callback.

Las propiedades **min_date_allowed** y **max_date_allowed** definen las fechas mínimas y máximas que se pueden seleccionar en el calendario, mientras que **nitial_visible_month** define el mes del calendario que se muestra primero cuando se abre el componente **dcc.DatePickerSingle**.

```bash
1.simple_date_picker_single.py
```

## Month Format Examples

Puede establecer **month_format** en cualquier permutación de los tokens de cadena que se muestran en Mes y formato de visualización arriba para cambiar cómo se muestran los títulos del calendario en el componente **dcc.DatePickerSingle**.

```python
from dash import dcc
from datetime import date

dcc.DatePickerSingle(
    month_format='MMM Do, YY',
    placeholder='MMM Do, YY',
    date=date(2017, 6, 21)
)
```

```python
from dash import dcc
from datetime import date

dcc.DatePickerSingle(
    month_format='M-D-Y-Q',
    placeholder='M-D-Y-Q',
    date=date(2017, 6, 21)
)
```

```python
from dash import dcc
from datetime import date

dcc.DatePickerSingle(
    month_format='MMMM Y',
    placeholder='MMMM Y',
    date=date(2020, 2, 29)
)
```

```python
from dash import dcc
from datetime import date

dcc.DatePickerSingle(
    month_format='X',
    placeholder='X',
    date=date(2017, 6, 21)
)
```

## Display Format Examples

Puede utilizar cualquier permutación de los tokens de cadena que se muestran en Mes y formato de visualización arriba para cambiar cómo se muestran las fechas seleccionadas en el componente **dcc.DatePickerSingle**.

```python
from dash import dcc

dcc.DatePickerSingle(
    date='2017-06-21',
    display_format='MMM Do, YY'
)
```

```python
from dash import dcc
from datetime import date

dcc.DatePickerSingle(
    date=date(2017, 6, 21),
    display_format='M-D-Y-Q',
)
```

```python
from dash import dcc
from datetime import date

dcc.DatePickerSingle(
    date=date(2017, 6, 21),
    display_format='MMMM Y, DD'
)
```

```python
from dash import dcc
from datetime import date

dcc.DatePickerSingle(
    date=date(2017, 6, 21),
    display_format='X',
)
```

## Vertical Calendar and Placeholder Text

El componente **dcc.DatePickerSingle** se puede representar en dos orientaciones, ya sea horizontal o vertical. Si **calendar_orientation** está configurado como "vertical", se representará verticalmente y, de manera predeterminada, será "horizontal" si no se define.

El marcador de posición define el texto predeterminado en gris definido en los cuadros de entrada del calendario cuando no se selecciona ninguna fecha.

```python
from dash import dcc
from datetime import date

dcc.DatePickerSingle(
    calendar_orientation='vertical',
    placeholder='Select a date',
    date=date(2017, 6, 21)
)
```

## Calendar Clear and Portals

Cuando la propiedad clearable se establece en True, el componente se representará con una x pequeña que eliminará todas las fechas seleccionadas cuando se seleccione.

El componente **dcc.DatePickerSingle** admite dos tipos de portales diferentes: uno es un portal de pantalla completa (with_full_screen_portal) y otro es una superposición de pantalla simple, como la que se muestra a continuación (with_portal).

```python
from dash import dcc
from datetime import date

dcc.DatePickerSingle(
    clearable=True,
    with_portal=True,
    date=date(2017, 6, 21)
)
```

## Right To Left Calendars and First Day of Week

Cuando la propiedad **is_RTL** se establece en True, el calendario se representará de derecha a izquierda.

La propiedad **first_day_of_week** le permite definir qué día de la semana se establecerá como el primer día de la semana. En el siguiente ejemplo, el martes es el primer día de la semana.
