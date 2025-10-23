
import geopandas as gpd
import pandas as pd
from shapely.wkt import loads
import os
import matplotlib.pyplot as plt

EPSG = 31983

data_folder = 'data'
csv = os.path.join(data_folder, 'csv/20230502_bairro_oficial.csv')

geo_folder = os.path.join(data_folder, 'geo')
df = pd.read_csv(csv)
df['GEOMETRIA'] = df['GEOMETRIA'].apply(loads) 
gdf = gpd.GeoDataFrame(df, geometry='GEOMETRIA', crs=EPSG)
gdf.to_crs(4326, inplace=True)

gdf.to_file(os.path.join(geo_folder, 'bairros.geojson'))