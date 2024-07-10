from dash import Dash, dcc, html, Input, Output, Patch, callback

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Button("Remove items", id="remove-button"),
        dcc.Checklist(id="checklist-remove-items"),
    ]
)

@callback(
    Output("checklist-remove-items", "options"),
    Input("remove-button", "n_clicks"),
)
def remove_records(n_clicks):
    if not n_clicks:
        return [
            "Boston",
            "Montreal",
            "New York",
            "Toronto",
            "San Francisco",
            "Vancouver",
        ]
    else:
        canadian_cities = ["Montreal", "Toronto", "Vancouver"]
        patched_list = Patch()
        for x in canadian_cities:
            patched_list.remove(x)
        return patched_list


if __name__ == "__main__":
    app.run(debug=True)
