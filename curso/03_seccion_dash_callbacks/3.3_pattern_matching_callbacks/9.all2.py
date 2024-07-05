from dash import Dash, dcc, html, Input, Output, State, ALL, callback
import plotly.express as px
import pandas as pd

# Crear una aplicación Dash
app = Dash(__name__)

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
    html.Button('Add Input', id='add-input', n_clicks=0),
    html.Div(id='input-container', children=[]),
    html.Div(id='output-container')
])

# Callback para agregar nuevos inputs dinámicamente
@callback(
    Output('input-container', 'children'),
    Input('add-input', 'n_clicks'),
    State('input-container', 'children')
)
def display_inputs(n_clicks, children):
    new_input = dcc.Input(
        id={'type': 'dynamic-input', 'index': n_clicks},
        value='SF',
        type='text'
    )
    children.append(new_input)
    return children

# Callback para actualizar el gráfico basado en los inputs
@app.callback(
    Output('example-graph', 'figure'),
    Input({'type': 'dynamic-input', 'index': ALL}, 'value')
)
def update_graph(selected_cities):
    # Filtrar los datos según la entrada
    filtered_df = df[df['City'].isin(selected_cities)]
    # Actualizar el gráfico
    fig = px.bar(filtered_df, x="Fruit", y="Amount", color="City", barmode="group")
    return fig

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
