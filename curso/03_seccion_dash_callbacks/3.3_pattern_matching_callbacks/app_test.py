from dash import Dash, dcc, html, Input, Output, State, ALL, callback
import dash_bootstrap_components as dbc
import random


# Generar datos aleatorios
data = {
    "Región 1": [random.randint(100, 200) for _ in range(10)],
    "Región 2": [random.randint(100, 200) for _ in range(10)],
    "Región 3": [random.randint(100, 200) for _ in range(10)]
}

# Definir el layout del dashboard
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([
    html.H1("Dashboard de Ventas"),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="grafico-region-1"),
        ]),
        dbc.Col([
            dcc.Graph(id="grafico-region-2"),
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Button("Actualizar", id="boton-actualizar", className="mr-1")
        ])
    ])
])

# Definir los callbacks
@app.callback(
    [Output("grafico-region-1", "figure"), Output("grafico-region-2", "figure")],
    [Input("boton-actualizar", "n_clicks")]
)
def actualizar_graficos(n_clicks):
    if n_clicks is None:
        # Inicializar los datos en la primera carga
        data_region_1 = data["Región 1"]
        data_region_2 = data["Región 2"]
    else:
        # Generar nuevos datos aleatorios al hacer clic en el botón
        data_region_1 = [random.randint(100, 200) for _ in range(10)]
        data_region_2 = [random.randint(100, 200) for _ in range(10)]

    # Crear los gráficos de barras
    grafico_region_1 = {
        "data": [{"x": list(range(10)), "y": data_region_1, "type": "bar"}],
        "layout": {"title": "Región 1"},
    }
    grafico_region_2 = {
        "data": [{"x": list(range(10)), "y": data_region_2, "type": "bar"}],
        "layout": {"title": "Región 2"},
    }

    return grafico_region_1, grafico_region_2

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run_server(debug=True)
