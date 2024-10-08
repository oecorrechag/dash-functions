from dash import Dash
from dash.dash_table import DataTable
from dash.dash_table.Format import Format, Padding

app = Dash(__name__)

columns = [
    dict(id='a', name='No padding', type='numeric', format=Format()),
    dict(id='a', name='Padding 12', type='numeric', format=Format(padding=True, padding_width=12)),
    dict(id='a', name='Padding 9', type='numeric', format=Format(padding=Padding.yes).padding_width(9)),
    dict(id='a', name='Padding 6', type='numeric', format=dict(specifier='06'))
]

values = [123, 123, 1234, 12345, 123456789]

app.layout = DataTable(columns=columns, data=[dict(a=value) for value in values])

if __name__ == '__main__':
    app.run(debug=True)
