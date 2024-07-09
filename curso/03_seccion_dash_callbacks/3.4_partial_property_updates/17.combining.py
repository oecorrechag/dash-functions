from dash import Dash, html, dcc, Input, Output, Patch, callback
from plotly import graph_objects as go

app = Dash(__name__)

x = ["Product A", "Product B", "Product C"]
y = [20, 14, 23]

fig = go.Figure(data=[go.Bar(x=x, y=y)])

app.layout = html.Div(
    [
        html.Button("Update products", id="add-product-d-e"),
        dcc.Graph(figure=fig, id="prepend-append-example-graph"),
    ]
)


@callback(
    Output("prepend-append-example-graph", "figure"),
    Input("add-product-d-e", "n_clicks"),
    prevent_initial_call=True,
)
def add_data_to_fig(n_clicks):
    if n_clicks % 2 != 0:
        patched_figure = Patch()
        patched_figure["data"][0]["x"].prepend("Product D")
        patched_figure["data"][0]["y"].prepend(34)
        patched_figure["data"][0]["x"].append("Product E")
        patched_figure["data"][0]["y"].append(34)
        return patched_figure
    else:
        return fig

if __name__ == "__main__":
    app.run(debug=True)
