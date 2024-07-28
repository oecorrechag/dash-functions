from dash import Dash, dcc, html, Input, Output, callback
from plotly.express import data

df = data.medals_long()

app = Dash(__name__)
app.layout = html.Div([
    dcc.Dropdown(df.columns, id='pandas-dropdown-1'),
    html.Div(id='pandas-output-container-1')
])


@callback(
    Output('pandas-output-container-1', 'children'),
    Input('pandas-dropdown-1', 'value')
)
def update_output(value):
    return f'You have selected {value}'


if __name__ == '__main__':
    app.run(debug=True)
