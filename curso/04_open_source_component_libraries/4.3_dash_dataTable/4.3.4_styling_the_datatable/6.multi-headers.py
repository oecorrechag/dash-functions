from dash import Dash, dash_table
import pandas as pd

app = Dash(__name__)

app.layout = dash_table.DataTable(
    columns=[
        {"name": ["", "Year"], "id": "year"},
        {"name": ["City", "Montreal"], "id": "montreal"},
        {"name": ["City", "Toronto"], "id": "toronto"},
        {"name": ["City", "Ottawa"], "id": "ottawa"},
        {"name": ["City", "Vancouver"], "id": "vancouver"},
        {"name": ["Climate", "Temperature"], "id": "temp"},
        {"name": ["Climate", "Humidity"], "id": "humidity"},
    ],
    data=[
        {
            "year": i,
            "montreal": i * 10,
            "toronto": i * 100,
            "ottawa": i * -1,
            "vancouver": i * -10,
            "temp": i * -100,
            "humidity": i * 5,
        }
        for i in range(10)
    ],
    merge_duplicate_headers=True,
)

if __name__ == '__main__':
    app.run(debug=True)
