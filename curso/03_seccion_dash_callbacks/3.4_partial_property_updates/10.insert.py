from dash import Dash, html, dcc, Input, Output, Patch, callback
from plotly import graph_objects as go

app = Dash(__name__)

x = ["Product A", "Product C", "Product D", "Product E",]
y = [20, 14, 23, 8]

fig = go.Figure(data=[go.Bar(x=x, y=y)])

app.layout = html.Div(
    [
        html.Button("Update products", id="additional-product-insert"),
        dcc.Graph(figure=fig, id="insert-example"),
    ]
)


@callback(
    Output("insert-example", "figure"),
    Input("additional-product-insert", "n_clicks"),
    prevent_initial_call=True,
)
def add_data_to_fig(n_clicks):
    if n_clicks % 2 != 0:
        patched_figure = Patch()
        patched_figure["data"][0]["x"].insert(1, "Product B")
        patched_figure["data"][0]["y"].insert(1, 10)
        return patched_figure
    else:
        return fig

if __name__ == "__main__":
    app.run(debug=True)
