from dash import Dash, dcc, html, Input, Output, State, callback

app = Dash(__name__)

app.layout = html.Div([
    dcc.Textarea(
        id='textarea-state-example',
        value='Textarea content initialized\nwith multiple lines of text',
        style={'width': '100%', 'height': 200},
    ),
    html.Button('Submit', id='textarea-state-example-button', n_clicks=0),
    html.Div(id='textarea-state-example-output', style={'whiteSpace': 'pre-line'})
])

@callback(
    Output('textarea-state-example-output', 'children'),
    Input('textarea-state-example-button', 'n_clicks'),
    State('textarea-state-example', 'value')
)
def update_output(n_clicks, value):
    if n_clicks > 0:
        return 'You have entered: \n{}'.format(value)

if __name__ == '__main__':
    app.run(debug=True)
