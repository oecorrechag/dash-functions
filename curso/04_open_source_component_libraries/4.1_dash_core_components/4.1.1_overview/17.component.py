from dash import Dash, dcc, html, Input, Output, callback
from dash.exceptions import PreventUpdate

app = Dash(prevent_initial_callbacks=True)

app.layout = html.Div(
    [html.Button("Download Text", id="btn_txt"), dcc.Download(id="download-text-index")]
)


@callback(Output("download-text-index", "data"), Input("btn_txt", "n_clicks"))
def func(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return dict(content="Hello world!", filename="hello.txt")


if __name__ == "__main__":
    app.run(debug=True)
