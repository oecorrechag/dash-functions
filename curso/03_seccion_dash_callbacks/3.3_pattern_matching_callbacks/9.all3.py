from dash import Dash, dcc, html, Input, Output, State, ALL
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
@app.callback(
    Output('input-container', 'children'),
    Input('add-input', 'n_clicks'),
    State('input-container', 'children')
)
def display_inputs(n_clicks, children):
    # Añadir diferentes tipos de inputs de manera dinámica
    new_input = html.Div([
        dcc.Input(
            id={'type': 'dynamic-input', 'index': n_clicks},
            value='SF',
            type='text',
            style={'margin': '10px'}
        ),
        # dcc.Dropdown(
        #     id={'type': 'dynamic-dropdown', 'index': n_clicks},
        #     options=[
        #         {'label': 'SF', 'value': 'SF'},
        #         {'label': 'Montreal', 'value': 'Montreal'}
        #     ],
        #     value='SF',
        #     style={'margin': '10px'}
        # ),
        # dcc.Slider(
        #     id={'type': 'dynamic-slider', 'index': n_clicks},
        #     min=0,
        #     max=10,
        #     step=1,
        #     value=5,
        #     marks={i: str(i) for i in range(11)},
        #     # style={'margin': '10px'}
        # )
    ])
    children.append(new_input)
    return children

# Callback para actualizar el gráfico basado en los inputs
@app.callback(
    Output('example-graph', 'figure'),
    Input({'type': 'dynamic-input', 'index': ALL}, 'value')
)
def update_graph(*args):

    # Recoger valores de los inputs
    values = [arg for arg in args if isinstance(arg, str)]
    
    # Filtrar los datos según las entradas
    filtered_df = df[df['City'].isin(values)]
    print(filtered_df.head())
    
    # Actualizar el gráfico
    fig = px.bar(filtered_df, x="Fruit", y="Amount", color="City", barmode="group")
    return fig

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
