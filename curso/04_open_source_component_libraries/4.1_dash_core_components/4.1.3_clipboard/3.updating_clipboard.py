from dash import Dash, dcc, html, Input, Output, State, dash_table, callback
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")

app.layout = html.Div(
    [
        dcc.Clipboard(id="table_copy", style={"fontSize":20}),
        dash_table.DataTable(
            df.to_dict("records"),
            [{"name": i, "id": i} for i in df.columns],
            id="table_cb",

        )
    ]
)


@callback(
    Output("table_copy", "content"),
    Input("table_copy", "n_clicks"),
    State("table_cb", "data"),
)
def custom_copy(_, data):
    dff = pd.DataFrame(data)
    # See options for .to_csv() or .to_excel() or .to_string() in the  pandas documentation
    return dff.to_csv(index=False)  # includes headers

if __name__ == "__main__":
    app.run(debug=True)
