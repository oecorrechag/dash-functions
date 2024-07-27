from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__)
app.layout = html.Div([
    html.Button("Download Text", id="btn-download-txt"),
    dcc.Download(id="download-text")
])


@callback(
    Output("download-text", "data"),
    Input("btn-download-txt", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dict(content="Hello world!", filename="hello.txt")


if __name__ == "__main__":
    app.run(debug=True)
