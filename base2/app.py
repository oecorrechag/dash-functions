from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from pages import home, page1, page2

import pandas as pd

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

data_store = html.Div([dcc.Store(id="original_data", data=df.to_dict()),
                       dcc.Store(id="filter_data"),
                       ])

app = Dash(__name__, title = 'App Base',
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)
server = app.server


app.layout = html.Div([
    data_store,
    
    dcc.Location(id='url', pathname="/", refresh=False),
    
    html.Div(id='header'),
    
    html.Div(id='page-content')

])


@callback(Output('page-content', 'children'),
          Input('url', 'pathname'),
          )
def display_page(pathname):
        
    if (pathname == '/home') | (pathname == '/'):
        return home.layout
    elif (pathname == '/page1'):
        return page1.page1
    elif (pathname == '/page2'):
            return page2.page2
    else:
        return '404'
    
    
if __name__ == '__main__':
    app.run_server(debug=True)
    