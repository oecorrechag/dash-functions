from dash import Dash, dcc, html, Input, Output, State, callback

app = Dash(__name__)

app.layout = html.Div([
    dcc.Store(id='my-store'),
    dcc.RadioItems(['NYC', 'MTL', 'SF'], 'NYC', id='my-store-input'),
    html.Div(id='current-store')
])

@callback(
    Output('my-store', 'data'),
    Input('my-store-input', 'value')
)
def update_store(value):
    return value

@callback(
    Output('current-store', 'children'),
    Input('my-store', 'modified_timestamp'),
    State('my-store', 'data')
)
def display_store_info(timestamp, data):
    return f"The store currently contains {data} and the modified timestamp is {timestamp}"

if __name__ == '__main__':
    app.run(debug=True)
