from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__)

app.layout = html.Div([
    dcc.Textarea(
        id='textarea-example',
        value='Textarea content initialized\nwith multiple lines of text',
        style={'width': '100%', 'height': 300},
    ),
    html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'})
])

@callback(
    Output('textarea-example-output', 'children'),
    Input('textarea-example', 'value')
)
def update_output(value):
    return 'You have entered: \n{}'.format(value)

if __name__ == '__main__':
    app.run(debug=True)
