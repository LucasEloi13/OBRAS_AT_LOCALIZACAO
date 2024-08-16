import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from pyproj import Proj, Transformer


def load_and_process_data(file_path):
    df = pd.read_excel(file_path)
    df = df.dropna(subset=['COORDENADA X', 'COORDENADA Y'])

    utm_proj = Proj(proj='utm', zone=22, south=False, datum='WGS84')
    geo_proj = Proj(proj='latlong', datum='WGS84')
    transformer = Transformer.from_proj(utm_proj, geo_proj)

    gdf = gpd.GeoDataFrame(df,
                           geometry=gpd.points_from_xy(df['COORDENADA X'],
                                                       df['COORDENADA Y']))
    gdf['geometry_transformed'] = gdf['geometry'].apply(
        lambda geom: Point(transformer.transform(geom.x, geom.y)))

    df['geometry_transformed'] = gdf['geometry_transformed'].apply(
        lambda geom: Point(geom.y, geom.x))

    return gdf
