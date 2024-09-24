from dash import Dash
from dash.dash_table import DataTable
from dash.dash_table.Format import Format, Align

app = Dash(__name__)

columns = [
    dict(id='a', name='No fill', type='numeric', format=Format()),
    dict(id='a', name='Align left (10)', type='numeric', format=Format().align(Align.left).fill('-').padding_width(10)),
    dict(id='a', name='Align right (8)', type='numeric', format=Format(align=Align.right, fill='-', padding_width=8)),
    dict(id='a', name='Align center (6)', type='numeric', format=dict(specifier='-^6'))
]

values = [123, 123, 1234, 12345, 123456789]

app.layout = DataTable(
    columns=columns,
    data=[dict(a=value) for value in values]
)

if __name__ == '__main__':
    app.run(debug=True)
