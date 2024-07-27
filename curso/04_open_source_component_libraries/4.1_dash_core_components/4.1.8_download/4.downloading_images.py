from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__)
app.layout = html.Div([
    html.Button("Download Image", id="btn_image"),
    dcc.Download(id="download-image")
])


@callback(
    Output("download-image", "data"),
    Input("btn_image", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file(
        "./dash_docs/assets/images/gallery/dash-community-components.png"
    )


if __name__ == "__main__":
    app.run(debug=True)
