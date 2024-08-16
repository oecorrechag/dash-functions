from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__)

app.layout = html.Div([
    dcc.Tabs(id="tabs-styled-with-props", value='tab-1', children=[
        dcc.Tab(label='1', value='tab-1'),
        dcc.Tab(label='2', value='tab-2'),
    ], colors={
        "border": "white",
        "primary": "gold",
        "background": "cornsilk"
    }),
    html.Div(id='tabs-content-props')
])

@callback(Output('tabs-content-props', 'children'),
              Input('tabs-styled-with-props', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])

if __name__ == '__main__':
    app.run(debug=True)
