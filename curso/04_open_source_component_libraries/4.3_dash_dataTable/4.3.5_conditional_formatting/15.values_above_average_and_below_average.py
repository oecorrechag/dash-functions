from dash import Dash, dash_table
import pandas as pd
from collections import OrderedDict

data = OrderedDict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
        ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
        ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
        ("Humidity", [10, 20, 30, 40, 50, 60]),
        ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
    ]
)

df = pd.DataFrame(data)

app = Dash(__name__)

def highlight_above_and_below_max(df):
    df_numeric_columns = df.select_dtypes('number').drop(['id'], axis=1)
    mean = df_numeric_columns.mean().mean()
    return (
        [
            {
                'if': {
                    'filter_query': '{{{}}} > {}'.format(col, mean),
                    'column_id': col
                },
                'backgroundColor': '#3D9970',
                'color': 'white'
            } for col in df_numeric_columns.columns
        ] +
        [
            {
                'if': {
                    'filter_query': '{{{}}} <= {}'.format(col, mean),
                    'column_id': col
                },
                'backgroundColor': '#FF4136',
                'color': 'white'
            } for col in df_numeric_columns.columns
        ]
    )

df['id'] = df.index
app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    sort_action='native',
    columns=[{'name': i, 'id': i} for i in df.columns if 'id' not in df],
    style_data_conditional=highlight_above_and_below_max(df)
)

if __name__ == '__main__':
    app.run(debug=True)
