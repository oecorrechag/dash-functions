from dash import Dash
from dash.html import Br, Div
from dash.dash_table import DataTable
from dash.dash_table.Format import Format, Group, Prefix, Scheme, Symbol

app = Dash(__name__)

columns_1 = [
    dict(id='a', name='Symbol', type='numeric', format=Format(symbol=Symbol.yes)),
    dict(id='a', name='Symbol prefix', type='numeric', format=Format(symbol=Symbol.yes, symbol_prefix='CAD$ ')),
    dict(id='a', name='Symbol suffix', type='numeric', format=Format(symbol=Symbol.yes, symbol_suffix=' $CAD')),
    dict(id='a', name='Symbol custom', type='numeric', format=dict(specifier='$', locale=dict(symbol=['@', '*'])))
]

columns_2 = [
    dict(id='a', name='Decimal', type='numeric', format=Format(decimal_delimiter=':').scheme('f').precision(2)),
    dict(id='a', name='Custom decimal', type='numeric', format=dict(specifier='.2f', locale=dict(decimal=':'))),
    dict(id='a', name='Group', type='numeric', format=Format(group_delimiter=':', group=Group.yes, groups=[2])),
    dict(id='a', name='Custom group', type='numeric', format=dict(specifier=',', locale=dict(group=':', grouping=[2])))
]

columns_3 = [
    dict(id='a', name='Custom numerals', type='numeric', format=dict(locale=dict(numerals=['0', 'AA', 'b', 'CC', '', '', '', '77', '88', '99']))),
    dict(id='a', name='Percent symbol', type='numeric', format=dict(specifier='.2%', locale=dict(percent='@'))),
    dict(id='a', name='Group 4 digits', type='numeric', format=dict(specifier=',.0f', locale=dict(separate_4digits=False))),
    dict(id='a', name='SI', type='numeric', format=Format(si_prefix=Prefix.milli).precision(0)),
    dict(id='a', name='SI+space', type='numeric', format=Format(si_prefix=Prefix.milli, symbol=Symbol.yes, symbol_suffix=' ').precision(0)),
    dict(id='a', name='Explicit SI', type='numeric', format=Format(si_prefix=10 ** -3).precision(0))
]

values = [123, 123, 1234, 12345, 123456789]
data = [dict(a=value) for value in values]

app.layout = Div([
    DataTable(columns=columns_1, data=data),
    Br(),
    DataTable(columns=columns_2, data=data),
    Br(),
    DataTable(columns=columns_3, data=data)
])

if __name__ == '__main__':
    app.run(debug=True)
