# dcc.DatePickerRange

**dcc.DatePickerRange** es un componente para representar calendarios entre los que los usuarios pueden seleccionar un rango de fechas.

Puede usar cadenas en el formato AAAA-MM-DD u objetos de fecha del módulo de fecha y hora para proporcionar fechas a los componentes de Dash. Se prefieren las cadenas porque esa es la forma que toman las fechas como argumentos de callback. Si está utilizando objetos de fecha, le recomendamos usar datetime.date para que no haya parte de tiempo. **dcc.DatePickerRange** acepta fechas con una parte de tiempo, pero esto puede resultar confuso, especialmente para la llamada inicial de un callback. Después de que el usuario elija una nueva fecha, no habrá parte de tiempo, solo la fecha. Si ya tiene el objeto adatetime.datetime, puede convertirlo con date().

## Month and Display Format

La propiedad Month_format determina cómo se muestran los encabezados del calendario cuando se abre el calendario. La propiedad display_format determina cómo se muestran las fechas seleccionadas en el componente **dcc.DatePickerRange**.

Ambas propiedades se configuran mediante cadenas que utilizan una combinación de cualquiera de los siguientes tokens.

![options](images/options.png)

## Simple DatePickerRange Example

Este es un ejemplo sencillo de un componente **dcc.DatePickerRange** vinculado a un callback.

Las propiedades **min_date_allowed** y **max_date_allowed** definen las fechas mínimas y máximas seleccionables en el calendario, mientras que **initial_visible_month** define el mes calendario que se muestra por primera vez cuando se abre el componente **dcc.DatePickerRange**.

```bash
1.simple_date_picker_range.py
```

## Month Format Examples

Puede establecer **month_format** en cualquier permutación de los tokens de cadena que se muestran en Mes y formato de visualización arriba para cambiar cómo se muestran los títulos del calendario en el componente **dcc.DatePickerRange**.

```python
from dash import dcc
from datetime import date

dcc.DatePickerRange(
    month_format='MMM Do, YY',
    end_date_placeholder_text='MMM Do, YY',
    start_date=date(2017, 6, 21)
)
```

```python
from dash import dcc
from datetime import date

dcc.DatePickerRange(
    month_format='M-D-Y-Q',
    end_date_placeholder_text='M-D-Y-Q',
    start_date=date(2017, 6, 21)
)
```

```python
from dash import dcc
from datetime import date

dcc.DatePickerRange(
    month_format='MMMM Y',
    end_date_placeholder_text='MMMM Y',
    start_date=date(2017, 6, 21)
)
```

```python
from dash import dcc
from datetime import date

dcc.DatePickerRange(
    month_format='X',
    end_date_placeholder_text='X',
    start_date=date(2017, 6, 21)
)
```

## Display Format Examples

Puede utilizar cualquier permutación de los tokens de cadena que se muestran en Mes y formato de visualización arriba para cambiar cómo se muestran las fechas seleccionadas en el componente **dcc.DatePickerRange**.

```python
from dash import dcc
from datetime import date

dcc.DatePickerRange(
    end_date=date(2017, 6, 21),
    display_format='MMM Do, YY',
    start_date_placeholder_text='MMM Do, YY'
)
```

```python
from dash import dcc
from datetime import date

dcc.DatePickerRange(
    end_date=date(2017, 6, 21),
    display_format='M-D-Y-Q',
    start_date_placeholder_text='M-D-Y-Q'
)
```

```python
from dash import dcc
from datetime import date

dcc.DatePickerRange(
    end_date=date(2017, 6, 21),
    display_format='MMMM Y, DD',
    start_date_placeholder_text='MMMM Y, DD'
)
```

```python
from dash import dcc
from datetime import date

dcc.DatePickerRange(
    end_date=date(2017, 6, 21),
    display_format='X',
    start_date_placeholder_text='X'
)
```

## Vertical Calendar and Placeholder Text

El componente **dcc.DatePickerRange** se puede representar en dos orientaciones, ya sea horizontal o vertical. Si **calendar_orientation** se establece en "vertical", se representará verticalmente y, de manera predeterminada, será "horizontal" si no se define.

**start_date_placeholder_text** y **end_date_placeholder_text** definen el texto predeterminado en gris definido en los cuadros de entrada del calendario cuando no se selecciona ninguna fecha.

```python
from dash import dcc

dcc.DatePickerRange(
    start_date_placeholder_text="Start Period",
    end_date_placeholder_text="End Period",
    calendar_orientation='vertical',
)
```

## Minimum Nights, Calendar Clear, and Portals

La propiedad **minimum_nights** define la cantidad de noches que deben estar entre el rango de dos fechas seleccionadas.

Cuando la propiedad **clearable** se establece en True, **dcc.DatePickerRange** se muestra con una pequeña "x" que el usuario puede seleccionar para eliminar las fechas seleccionadas.

El componente **dcc.DatePickerRange** admite dos tipos de portales diferentes: uno es un portal de pantalla completa (with_full_screen_portal) y otro es una superposición de pantalla simple, como la que se muestra a continuación (with_portal).

```python
from dash import dcc
from datetime import date

dcc.DatePickerRange(
    minimum_nights=5,
    clearable=True,
    with_portal=True,
    start_date=date(2017, 6, 21)
)
```

## Right to Left Calendars and First Day of Week

Cuando la propiedad **is_RTL** se establece en True, el calendario se representará de derecha a izquierda.

La propiedad **first_day_of_week** le permite definir qué día de la semana se establecerá como el primer día de la semana. En el siguiente ejemplo, el martes es el primer día de la semana.

```python
from dash import dcc
from datetime import date

dcc.DatePickerRange(
    is_RTL=True,
    first_day_of_week=3,
    start_date=date(2017, 6, 21)
)
```
