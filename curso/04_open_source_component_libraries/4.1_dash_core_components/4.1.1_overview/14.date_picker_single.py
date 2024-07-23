from dash import Dash, dcc, html
from datetime import date

app = Dash(__name__)

app.layout = html.Div([
    dcc.DatePickerSingle(
        id='date-picker-single',
        date=date(1997, 5, 10)
    )
])

if __name__ == '__main__':
    app.run(debug=True)
