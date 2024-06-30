from dash import Dash, html, dcc, Input, Output, callback, ctx

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div('Convert Temperature'),
    'Celsius',
    dcc.Input(
        id="celsius",
        value=0.0,
        type="number"
    ),
    ' = Fahrenheit',
    dcc.Input(
        id="fahrenheit",
        value=32.0,
        type="number",
    ),
])

@callback(
    Output("celsius", "value"),
    Output("fahrenheit", "value"),
    Input("celsius", "value"),
    Input("fahrenheit", "value"),
)
def sync_input(celsius, fahrenheit):
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]

    print(ctx.triggered[0]["prop_id"])

    if input_id == "celsius":
        fahrenheit= None if celsius is None else (float(celsius) * 9/5) + 32
    else:
        celsius = None if fahrenheit is None else (float(fahrenheit) - 32) * 5/9
    return celsius, fahrenheit

if __name__ == "__main__":
    app.run(debug=True)
