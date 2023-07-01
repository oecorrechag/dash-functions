from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

app = Dash(__name__, title = 'Boton de descarga pdf',
           external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.icons.BOOTSTRAP,]
)

server = app.server

app.layout = html.Div([

    html.Br(),html.Br(),html.Br(),

    dbc.Button("Download pdf", id="btn_pdf", color="success", className="me-1"),
    dcc.Download(id="download_pdf")

])


@callback(
    Output("download_pdf", "data"),
    Input("btn_pdf", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):

    # if n_nlicks is None:
    #     return dash.no_update
    # else:
    #     df2 = df.copy()

    return dcc.send_file("assets/archiv_pdf.pdf")


if __name__ == "__main__":
    app.run_server(debug=True)