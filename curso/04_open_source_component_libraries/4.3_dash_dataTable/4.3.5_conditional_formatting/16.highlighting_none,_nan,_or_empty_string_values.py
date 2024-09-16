from dash import Dash, dash_table, html
import pandas as pd
import numpy as np

data_with_none = [
    {'Firm': 'Acme', '2017': '', '2018': 5, '2019': 10, '2020': 4},
    {'Firm': 'Olive', '2017': None, '2018': 3, '2019': 13, '2020': 3},
    {'Firm': 'Barnwood', '2017': np.NaN, '2018': 7, '2019': 3, '2020': 6},
    {'Firm': 'Henrietta', '2017': 14, '2018': 1, '2019': 13, '2020': 1},
]
df = pd.DataFrame(data_with_none)

app = Dash(__name__)

app.layout = html.Div([
    html.Pre(repr(df)),
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in df.columns],
        style_data_conditional=(
            [
                {
                    'if': {
                        'filter_query': '{{{}}} is blank'.format(col),
                        'column_id': col
                    },
                    'backgroundColor': 'tomato',
                    'color': 'white'
                } for col in df.columns
            ]
        )
    )
])

if __name__ == '__main__':
    app.run(debug=True)
