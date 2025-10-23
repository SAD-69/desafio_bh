from models import os
from geopandas import GeoDataFrame
from pandas import DataFrame, read_csv
from functools import cached_property


ORIGINAL_EPSG = 31983
WGS_EPSG = 4326
GEO_DIR = 'data/geo'

class Transformer:
    def __init__(self, csv_path: str, geom_col: str = 'GEOMETRIA', epsg: str | int = ORIGINAL_EPSG):
        self.csv = csv_path
        self._geom_col = geom_col
        self._crs = epsg
        self._geo_path = GEO_DIR
        if not os.path.exists(self._geo_path):
            os.makedirs(self._geo_path)
        
        
    @cached_property
    def df(self) -> DataFrame:
        return read_csv(self.csv)
    
    @cached_property
    def gdf(self) -> GeoDataFrame:
        return GeoDataFrame(self.df, geometry=self._geom_col, crs=self._crs).to_crs(ORIGINAL_EPSG)
    
    def save_geojson(self, filename: str) -> None:
        return self.gdf.to_file(os.path.join(self._geo_path, filename + '.geojson'))