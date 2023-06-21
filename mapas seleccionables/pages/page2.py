from dash import dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px

from callbacks.callbacks_page2 import display2, grafico2, grafico3, container_principal, grafico4

page2_en = html.Div([
    html.H3('Page 2'),
    dcc.Dropdown(
        {f'Page 2 - {i}': f'{i}' for i in ['London', 'Berlin', 'Paris']},
        id='page-2-dropdown'
    ),
 
    display2,
   
    html.Br(),

    grafico2,
    
    html.Br(),

    grafico3,
    
    html.Br(),
    
    container_principal,
        
    html.Br(),
    
    grafico4,
    
    dcc.Link('Go to Page 1', href='/page1'),
    html.Br(),
    dcc.Link('Go to Page home', href='/home')
])

page2_es = html.Div([
    html.H3('Pagina 2'),
    dcc.Dropdown(
        {f'Page 2 - {i}': f'{i}' for i in ['London', 'Berlin', 'Paris']},
        id='page-2-dropdown'
    ),
 
    display2,
   
    html.Br(),

    grafico2,
    
    dcc.Link('Ir a pagina 1', href='/page1'),
    html.Br(),
    dcc.Link('Ir a pagina home', href='/home')
])
