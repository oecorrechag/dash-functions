import dash
from dash import dcc, html, Input, Output, ALL
import plotly.express as px
import pandas as pd

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Crear algunos datos de ejemplo
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# Crear un gráfico de ejemplo usando Plotly
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Definir el layout de la aplicación
app.layout = html.Div([
    html.H1("Ejemplo de Dashboard con Dash y Plotly"),
    dcc.Graph(id='example-graph', figure=fig),
    dcc.Input(
        id={'type': 'dynamic-input', 'index': 0},
        value='SF',
        type='text'
    ),
    html.Div(id='output-container')
])

# Definir los callbacks para la interactividad
@app.callback(
    Output('example-graph', 'figure'),
    Input({'type': 'dynamic-input', 'index': ALL}, 'value')
)
def update_graph(selected_city):
    # Filtrar los datos según la entrada
    filtered_df = df[df['City'].isin(selected_city)]
    # Actualizar el gráfico
    fig = px.bar(filtered_df, x="Fruit", y="Amount", color="City", barmode="group")
    return fig

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
