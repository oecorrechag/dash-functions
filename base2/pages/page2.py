from dash import dcc, html

from callbacks.callbacks_page2 import display2, grafico2

page2 = html.Div([
    html.H3('Page 2'),
    dcc.Dropdown(
        {f'Page 2 - {i}': f'{i}' for i in ['London', 'Berlin', 'Paris']},
        id='page-2-dropdown'
    ),
 
    display2,
   
    html.Br(),

    grafico2,
    
    dcc.Link('Go to Page 1', href='/page1'),
    html.Br(),
    dcc.Link('Go to Page home', href='/home')
])
