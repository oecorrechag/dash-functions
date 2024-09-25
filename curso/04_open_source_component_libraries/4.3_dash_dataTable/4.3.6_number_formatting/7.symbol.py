from dash import Dash
from dash.html import Br, Div
from dash.dash_table import DataTable
from dash.dash_table.Format import Format, Symbol

app = Dash(__name__)

columns_1 = [
    dict(id='a', name='Default', type='numeric', format=Format()),
    dict(id='a', name='No Symbol', type='numeric', format=Format(symbol=Symbol.no)),
    dict(id='a', name='$ Symbol', type='numeric', format=Format(symbol=Symbol.yes)),
    dict(id='a', name='@ Symbol / Locale prefix', type='numeric', format=Format().symbol(Symbol.yes).symbol_prefix('@')),
    dict(id='a', name='@ Symbol / Locale prefix+suffix', type='numeric', format=Format().symbol(Symbol.yes).symbol_prefix('@').symbol_suffix('*'))
]

columns_2 = [
    dict(id='a', name='Binary', type='numeric', format=Format(symbol=Symbol.binary)),
    dict(id='a', name='Octal', type='numeric', format=Format(symbol=Symbol.octal)),
    dict(id='a', name='Hex', type='numeric', format=Format(symbol=Symbol.hex)),
    dict(id='a', name='Custom', type='numeric', format=dict(locale=dict(symbol=['@', '*']), specifier='$'))
]

values = [123.1, 123.12, 1234.123, 12345.12]
data = [dict(a=value) for value in values]

app.layout = Div([
    DataTable(columns=columns_1, data=data),
    Br(),
    DataTable(columns=columns_2, data=data)
])

if __name__ == '__main__':
    app.run(debug=True)
