from dash import Dash, dash_table
import pandas as pd
from collections import OrderedDict


moby_dick_text = [
    'Call me Ishmael. ',
    ''.join([
        'Some years ago- never mind how long precisely- having little or no money ',
        'in my purse, and nothing particular to interest me on shore, ',
        'I thought I would sail about a little and see the watery part of the world. ',
    ]),
    'It is a way I have of driving off the spleen and regulating the circulation.'
]

moby_dick = OrderedDict(
    [
        (
            'Sentence Number', [i+1 for i in range(len(moby_dick_text))],
        ),
        (
            'Text', [i for i in moby_dick_text]
        )
    ]
)
df = pd.DataFrame(moby_dick)

app = Dash(__name__)

app.layout = dash_table.DataTable(
    style_data={
        'whiteSpace': 'normal',
    },
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    css=[{
        'selector': '.dash-spreadsheet td div',
        'rule': '''
            line-height: 15px;
            max-height: 30px; min-height: 30px; height: 30px;
            display: block;
            overflow-y: hidden;
        '''
    }],
    tooltip_data=[
        {
            column: {'value': str(value), 'type': 'markdown'}
            for column, value in row.items()
        } for row in df.to_dict('records')
    ],
    tooltip_duration=None,

    style_cell={'textAlign': 'left'} # left align text in columns for readability
)

if __name__ == '__main__':
    app.run(debug=True)
