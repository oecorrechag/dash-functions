from dash import Dash, dcc, html, Input, Output, callback
import pandas as pd

app = Dash(__name__)
app.layout = html.Div([
    html.Button("Download Excel", id="btn_xlsx"),
    dcc.Download(id="download-dataframe-xlsx"),
])


df = pd.DataFrame({"a": [1, 2, 3, 4], "b": [2, 1, 5, 6], "c": ["x", "x", "y", "y"]})


@callback(
    Output("download-dataframe-xlsx", "data"),
    Input("btn_xlsx", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(df.to_excel, "mydf.xlsx", sheet_name="Sheet_name_1")


if __name__ == "__main__":
    app.run(debug=True)
