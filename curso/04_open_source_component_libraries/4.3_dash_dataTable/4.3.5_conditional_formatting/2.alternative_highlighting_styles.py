from dash import Dash, dash_table
import pandas as pd
from collections import OrderedDict
from dash.dash_table.Format import Format, Sign

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

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    sort_action='native',
    columns=[
        {"name": i, "id": i} for i in df.columns
    ],
    style_data_conditional=[
        {
            'if': {
                'filter_query': '{Humidity} > 19 && {Humidity} < 41',
                'column_id': 'Humidity'
            },
            'color': 'tomato',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{Pressure} > 19',
                'column_id': 'Pressure'
            },
            'textDecoration': 'underline'
        }
    ]
)

if __name__ == '__main__':
    app.run(debug=True)
