import folium

def generate_map(gdf, icon_path):
    mapa = folium.Map(
        location=[gdf['geometry_transformed'].y.mean(), gdf['geometry_transformed'].x.mean()],
        zoom_start=12
    )

    for index, row in gdf.iterrows():
        tooltip_content = f"""
        Tipo de Estrutura: {row['TIPO DE ESTRUTURA']}<br>
        Esforço/Altura: {row['ESFORÇO/ALTURA']}
        """
        folium.Marker(
            [row['geometry_transformed'].y, row['geometry_transformed'].x],
            tooltip=folium.Tooltip(tooltip_content, permanent=True, offset=(0, 0)),
            icon=folium.CustomIcon(icon_image=icon_path, icon_size=(32, 32))
        ).add_to(mapa)

    coordenadas = [[row['geometry_transformed'].y, row['geometry_transformed'].x] for index, row in gdf.iterrows()]
    folium.PolyLine(locations=coordenadas, color='blue', weight=2.5, opacity=1).add_to(mapa)

    return mapa
