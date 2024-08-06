from dash import Dash, dcc
from plotly.express import data

df = data.medals_long()

app = Dash(__name__)

app.layout = dcc.RadioItems(df.nation.unique(),df.nation.unique()[1])

if __name__ == "__main__":
    app.run(debug=True)
