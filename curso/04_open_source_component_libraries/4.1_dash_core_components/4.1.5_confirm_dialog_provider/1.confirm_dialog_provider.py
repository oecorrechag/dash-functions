from dash import Dash, Input, Output, html, dcc, callback

app = Dash(__name__)

app.layout = html.Div([
    dcc.ConfirmDialogProvider(
        children=html.Button('Click Me',),
        id='danger-danger-provider',
        message='Danger danger! Are you sure you want to continue?'
    ),
    html.Div(id='output-provider')
])


@callback(Output('output-provider', 'children'),
              Input('danger-danger-provider', 'submit_n_clicks'))
def update_output(submit_n_clicks):
    if not submit_n_clicks:
        return ''
    return """
        It was dangerous but we did it!
        Submitted {} times
    """.format(submit_n_clicks)


if __name__ == '__main__':
    app.run(debug=True)
