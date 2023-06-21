from dash import dcc, html, Input, Output, callback
import pandas as pd
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc

import geopandas as gpd 


gdf = gpd.read_file('data/df_italia.geojson')
gdf['geoid'] = gdf.index.astype(str)
gdf.geometry = gdf.geometry.to_crs(epsg = 4326) # 4326    # 3857


df_punticos = pd.read_csv('data/df_punticos.csv', sep = ',', decimal = '.', header = 0, encoding = 'utf-8')
df_punticos = df_punticos[df_punticos['DEN_UTS'] == 'Milano']
df_punticos = df_punticos.reset_index(drop=True)
df_punticos = df_punticos.iloc[0:100]
df_punticos['geo'] = df_punticos.index.astype(int)
df_punticos['geo2'] = df_punticos.index.astype(str)

# Display 
display2 = dbc.Row(children=[
    dcc.Markdown(id='display2')
])
@callback(
    Output('display2', 'children'),
    Input('page-2-dropdown', 'value'),
    )
def display_value(value):
    return f'You have selected {value}'


grafico2 = dbc.Row(children=[
    
    dcc.Graph(id='grafico2', figure={})
])
@callback(
    Output('grafico2', 'figure'),
    Input('filter_data', 'data'),
    )
def display_value(data):
    df = pd.DataFrame.from_dict(data)
    df = data.copy()
    grafico = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    return grafico


grafico3 = dbc.Row(children=[
    dcc.Graph(id='grafico3', figure={})
])
@callback(
    Output('grafico3', 'figure'),
    Input('page-2-dropdown', 'value'),
    )
def display_value(value):
    
    # print('Geopandas')
    # print(gdf.head())
    # print('***')
    
    x = value
    grafico3 = px.choropleth_mapbox(gdf,
                                    geojson=gdf.__geo_interface__,#['geometry']
                                    locations=gdf.geoid,
                                    color='count',
                                    hover_data=["DEN_UTS"],
                                    labels={'count':'Unidades'},
                                    featureidkey='properties.geoid',
                                    center={'lat': 45.48, 'lon':9.14},
                                    mapbox_style='carto-positron',
                                    zoom=10,
                                    opacity=0.5,
                                    )


    # Agregar evento de clic
    grafico3.update_layout(
        clickmode='event+select',
        showlegend=False
    )

    selected_polygons = []

    def handle_click(trace, points, selector):
        if points.point_inds:
            selected_polygon = points.point_inds[0]
            if selected_polygon not in selected_polygons:
                selected_polygons.append(selected_polygon)
            else:
                selected_polygons.remove(selected_polygon)
            print(f"Polígonos seleccionados: {selected_polygons}")

    grafico3.data[0].on_click(handle_click)

    # print('df')
    # print(df_punticos.head())
    # print('***')

    grafico3.add_scattermapbox(
             lat=df_punticos['latitude'],
             lon=df_punticos['longitude'],
             mode='markers',
             marker=dict(
                 size=8,
                 color=df_punticos['geo'],
                 opacity=0.1,
             ),
             text=df_punticos['DEN_UTS'] + '<br>' + df_punticos['geo2']
    )



    # selected_points = []

    # def handle_click(trace, points, state):
    #     for point in points.point_inds:
    #         selected_points.append((trace.x[point], trace.y[point]))
    #     grafico3.data[1].x = [point[0] for point in selected_points]
    #     grafico3.data[1].y = [point[1] for point in selected_points]
    #     grafico3.update_layout(overwrite=True)

    # # Agrega la función de manejo de clics a los gráficos de polígonos
    # grafico3.data[0].on_click(handle_click)




    # Agrandar y mover labels
    grafico3.update_layout(margin={'l': 0, 't': 0, 'r': 0, 'b': 0})
    grafico3.update_coloraxes(
             colorbar=dict(
                 lenmode="fraction",
                 len=0.4,
                 x=0,
                 y=0.25
             )
    )

    # grafico3.update_layout(width=800, height=400)

    return grafico3




container_principal = dbc.Row(children=[
    html.Div(id='container_principal'),
])
@callback(
    Output('container_principal','children'),
    Input('grafico3','selectedData'))
def selectData(selectedData):
    return str('Selecting points produces a nested dictionary: {}'.format(selectedData))



grafico4 = dbc.Row(children=[
    dcc.Graph(id='grafico4', figure={})
])
@callback(
    Output('grafico4', 'figure'),
    Input('grafico3','selectedData'))
def selectData(selectedData):
    
    if selectedData is None:
        
        y = [367, 100]
        x = ['cajones', 'bolitas']
        grafico4 = px.bar(x=x, y=y, title="Wide-Form Input")
        
    else:    
        
        partes = []
        puntillas = []
             
        for i in range(len(selectedData['points'])):
            
            if selectedData['points'][i]['curveNumber'] == 0:
                punto = selectedData['points'][i]['pointNumber']
                partes.append(punto)
                
            else:
                punto = selectedData['points'][i]['pointNumber']
                puntillas.append(punto)
                
        print('partes: ', partes)    
        print('puntillas: ', puntillas)    
        
        df2 = df_punticos.copy()
        df2 = df2[np.isin(df2["geo"], puntillas)]  

        print('df2')
        print(df2.head())
        print('***') 
                
        y = [len(set(partes)), len(set(puntillas))]
        x = ['cajones', 'bolitas']

        grafico4 = px.bar(x=x, y=y, title="Wide-Form Input")
        
    return grafico4
