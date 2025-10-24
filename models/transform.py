from models import *
from shapely.wkt import loads

ENCODING = 'utf-8'
ORIGINAL_EPSG = 31983
WGS_EPSG = 4326
GEO_DIR = 'data/geo'

class Transformer:
    """Classe de consumo do arquivo CSV fonte.
    Retorna os dados tabulares em dados geoespaciais (coluna=GEOMETRIA (WKT))
    Propriedades:
    df -> DataFrame: Dados tabulares do CSV
    gdf -> GeoDataframe: Dados Geoespaciais do CSV
    """
    def __init__(self, csv_path: str, geom_col: str = 'GEOMETRIA', epsg: str | int = ORIGINAL_EPSG):
        self.csv = csv_path
        self._geom_col = geom_col
        self._crs = epsg
        self._geo_path = GEO_DIR
        if not os.path.exists(self._geo_path):
            os.makedirs(self._geo_path)
    
    @staticmethod     
    def _check_sep(csv_file: str):
        with open(csv_file, 'r', encoding=ENCODING) as f:
            f_lin = f.readline()
            if ';' in f_lin and ',' not in f_lin:
                sep = ';'
            elif ',' in f_lin:
                sep = ','
            else:
                sep ='\t'     
        return sep
        
        
    @cached_property
    def df(self) -> DataFrame:
        # Check sep
        sep = self._check_sep(self.csv)
        df = read_csv(self.csv, encoding=ENCODING, sep=sep)
        df[self._geom_col] = df[self._geom_col].apply(loads)
        return df
    
    @cached_property
    def gdf(self) -> GeoDataFrame:
        return GeoDataFrame(self.df, geometry=self._geom_col, crs=self._crs).to_crs(ORIGINAL_EPSG)
    
    def save_as_geojson(self, filename: str) -> None:
        """Salva o GDF em formato GeoJSON na pasta data/geo

        Args:
            filename (str): nome do arquivo
        """
        return self.gdf.to_file(os.path.join(self._geo_path, filename + '.geojson'))
    


if __name__ == '__main__':
    t = Transformer(r'data\csv\20251001_ponto_onibus.csv')
    print(t.gdf.head())
    # t2 = Transformer(r'data\csv\20230502_bairro_oficial.csv')
    # print(t2.gdf.head())
    # csv_list = os.listdir('data/csv')
    
    # for i in csv_list:
    #     csv_path = os.path.join('data/csv', i)
    #     t = Transformer(csv_path)
    #     print(i)
    #     print(t.df.head())
    #     print(t.gdf.head())
    #     file_name = i.replace('.csv', '')
    #     t.save_as_geojson(file_name)