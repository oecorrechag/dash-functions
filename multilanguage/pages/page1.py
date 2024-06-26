from dash import dcc, html, Input, Output, callback, State
import pandas as pd

from callbacks.callbacks_page1 import display1, grafico1

page1_en = html.Div([
    html.H3('Page 1'),    

    html.Br(),
    
    dcc.Dropdown(
        id='page1_menu',
        placeholder="Select City",
        options = ['SF', 'Montreal'],
        value="Montreal",
        multi=False,
        clearable=False
    ),
    
    display1,
    
    html.Br(),
    
    grafico1,
    
    html.Br(),
    
    html.Div([
        html.Button("Apply filter", id="btn_menu", style={'marginLeft':'10px', 'marginRight':'10px'}),
    ]),

    dcc.Link('Go to Page 2', href='/page2'),
    html.Br(),
    dcc.Link('Go to Page home', href='/home')
])

page1_es = html.Div([
    html.H3('Pagina 1'),    

    html.Br(),
    
    dcc.Dropdown(
        id='page1_menu',
        placeholder="Seleccione Ciudad",
        options = ['SF', 'Montreal'],
        value="Montreal",
        multi=False,
        clearable=False
    ),
    
    display1,
    
    html.Br(),
    
    grafico1,
    
    html.Br(),
    
    html.Div([
        html.Button("Aplicar filtros", id="btn_menu", style={'marginLeft':'10px', 'marginRight':'10px'}),
    ]),

    dcc.Link('Ir a Page 2', href='/page2'),
    html.Br(),
    dcc.Link('Ir a Page home', href='/home')
])


# Callback para guardar los datos filtrados
@callback(
    Output('filter_data', 'data'), 
    Input("btn_menu", "n_clicks"),
    State('original_data', 'data'),
    Input('page1_menu', 'value'),
    prevent_initial_call=True,
    memoize=True)
def filter_data(n_clicks, data, value):

    if n_clicks is None:
        data = pd.DataFrame.from_dict(data)
        return data.to_dict('dict')
    else:
        data = pd.DataFrame.from_dict(data)
        data = data[data['City'] == value]
        return data.to_dict('dict')
    