from models.db.postgres import Postgres
from models import GeoDataFrame

class Loader(Postgres):
    """Loader class. It loads things into the DB.
    Molde inicial de um carregador de dados pré-processados 
    (raw extraction -> transform to geo/some data - load (postgis_db))
    Para esse desafio serve apenas para carregar dados no banco de dados.
    Potencial de expansão para cargas direcionadas na API 
        (input usuario -> schema users; input novos dados -> schema bronze_raw)
    Args:
        Postgres (_type_): Classe de interação com banco de dados PostgreSQL
    """
    def __init__(self, user = ..., password = ..., host = ..., port = ..., db = ...):
        super().__init__(user, password, host, port, db)
        
    def import_to_db(self, gdf: GeoDataFrame, table: str, schema: str = 'public'):
        return gdf.to_postgis(table, self.engine, schema=schema, if_exists='replace')
    
    