from models.db.postgres import Postgres
from models import GeoDataFrame
from typing import Literal

MedallionArch = Literal['bronze', 'silver', 'gold']

class Loader(Postgres):
    """Loader class. It loads things into the DB.
    Molde inicial de um carregador de dados pré-processados 
    (raw extraction -> transform to geo/some data - load (postgis_db))
    Para esse desafio serve apenas para carregar dados no banco de dados.
    Potencial de expansão para cargas direcionadas na API 
        (input usuario -> schema users; input novos dados -> schema bronze_raw)
    Args:
        Postgres (_type_): Classe de interação com banco de dados PostgreSQL
        layer: Layer hierárquica da Arquitetura Medalhão (Bronze - dados brutos, Silver - dados curados, Gold - dados refinados).
        Também indica o nome do esquema do banco de dados a ser inserido
    """
    def __init__(self, layer: MedallionArch):
        super().__init__()
        self.layer = layer.lower()
        
    def import_to_db(self, gdf: GeoDataFrame, table: str):
        if self.layer != 'public':
            self.create_schema(self.layer)
        return gdf.to_postgis(table, self.engine.connect(), schema=self.layer, if_exists='replace')
    
    