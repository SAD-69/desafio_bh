from models.db.postgres import Postgres
from models import GeoDataFrame

class Loader(Postgres):
    def __init__(self, user = ..., password = ..., host = ..., port = ..., db = ...):
        super().__init__(user, password, host, port, db)
        
    def import_to_db(self, gdf: GeoDataFrame, table: str, schema: str = 'public'):
        return gdf.to_postgis(table, self.engine, schema=schema, if_exists='replace')
    
    