from dash import Dash, dcc
from plotly.express import data

df = data.medals_long()

app = Dash(__name__)

app.layout = dcc.RadioItems(df.columns, df.columns[0])

if __name__ == "__main__":
    app.run(debug=True)
