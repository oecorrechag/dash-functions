import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc


# data
df = pd.DataFrame({'a': [1, 2, 3, 4, 1, 2], 
                   'b': [2, 1, 5, 6, 9, 2],
                   'c': ['x', 'x', 'y', 'y', 'x', 'y']})


app = Dash(__name__, title = 'Descargar csv o excel',
           external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.icons.BOOTSTRAP,]
)

server = app.server

app.layout = html.Div([

    html.Br(),html.Br(),html.Br(),
    
    html.Div([
    
            dbc.Button("Download", id="btn", className="btn-platzi me-2"),
            dcc.Download(id="download"),

    ])

])

@callback(
    Output("download", "data"), 
    Input("btn", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_nlicks):
    
    # if n_nlicks is None:
    #     return dash.no_update
    # else:
    #     df2 = df.copy()

    df2 = df.copy()

    return dcc.send_data_frame(df2.to_csv, "mydf.csv", index = False)

# dcc.send_data_frame(df2.to_csv, "mydf.csv", index = False)
# dcc.send_data_frame(df.to_excel, "mydf.xls", index = False)


if __name__ == '__main__':
    app.run_server(debug=True)
