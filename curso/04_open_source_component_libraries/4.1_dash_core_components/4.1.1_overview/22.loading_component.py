from dash import Dash, dcc, html, Input, Output, callback
import time

app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.RadioItems(
            ["Montreal", "New York", "London"], "London", id="loading-demo-dropdown"
        ),
        dcc.Loading([html.Div(id="loading-demo")]),
    ]
)

@callback(Output("loading-demo", "children"), Input("loading-demo-dropdown", "value"))
def update_loading_div(value):
    time.sleep(2)
    return f"You selected {value}"

if __name__ == "__main__":
    app.run(debug=True)
