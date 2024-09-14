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

def style_table_by_max_value(df):
    if 'id' in df:
        numeric_columns = df.select_dtypes('number').drop(['id'], axis=1)
    else:
        numeric_columns = df.select_dtypes('number')
    max_across_numeric_columns = numeric_columns.max()
    max_across_table = max_across_numeric_columns.max()
    styles = []
    for col in max_across_numeric_columns.keys():
        if max_across_numeric_columns[col] == max_across_table:
            styles.append({
                'if': {
                    'filter_query': '{{{col}}} = {value}'.format(
                        col=col, value=max_across_table
                    ),
                    'column_id': col
                },
                'backgroundColor': '#39CCCC',
                'color': 'white'
            })
    return styles


df['id'] = df.index
app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    sort_action='native',
    columns=[{'name': i, 'id': i} for i in df.columns if i != 'id'],
    style_data_conditional=style_table_by_max_value(df)
)

if __name__ == '__main__':
    app.run(debug=True)
