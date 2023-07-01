from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from pages import home, page1, page2
from layouts import header, header2

import pandas as pd

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

data_store = html.Div([dcc.Store(id="original_data", data=df.to_dict()),
                       dcc.Store(id="filter_data"),
                       dcc.Store(id="language"),
                       ])

app = Dash(__name__, title = 'App Base',
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)
server = app.server


app.layout = dbc.Container([
    # dcc.Store(id="original_data", data=df.to_dict()),
    # dcc.Store(id="filter_data"),
    data_store,
    
    dcc.Location(id='url', pathname="/", refresh=False),
    
    html.Div(id='header'),
    
    html.Div(id='page-content')

], fluid=True)



@callback(Output('header', 'children'),
          Input('url', 'pathname')
          )
def display_h(pathname):
    if (pathname == '/home') | (pathname == '/'):
        return header
    else:
        return header2


@callback(
    Output('language', 'data'), 
    Input('select_language', 'value'),
          )
def filter_l(value):
    return value


@callback(Output('page-content', 'children'),
          Input('url', 'pathname'),
          Input('language', 'data'),
          )
def display_page(pathname, data):
    if data is not None:
       n_switches = len(data)
    else: 
        n_switches = 1
    
    if (pathname == '/home') | (pathname == '/'):
        return home.layout
    elif (pathname == '/page1') & (n_switches == 1):
        return page1.page1_en
    elif (pathname == '/page1') & (n_switches == 0):
        return page1.page1_es
    elif (pathname == '/page2') & (n_switches == 1):
            return page2.page2_en
    elif (pathname == '/page2') & (n_switches == 0):
        return page2.page2_es   
    else:
        return '404'
    
    
if __name__ == '__main__':
    app.run_server(debug=True)
    