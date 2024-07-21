from dash import Dash, html, dcc, callback, Input, Output, State, callback

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.Div(dcc.Input(id='input-box', type='text')),
    html.Button('Submit', id='button-example-1'),
    html.Div(id='output-container-button',
             children='Enter a value and press submit')
])


@callback(
    Output('output-container-button', 'children'),
    Input('button-example-1', 'n_clicks'),
    State('input-box', 'value'))
def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )


if __name__ == '__main__':
    app.run(debug=True)
