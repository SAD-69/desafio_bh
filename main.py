from models.transform import Transformer, os
from models.load import Loader

if __name__ == '__main__':
    csv_list = os.listdir('data/csv')
    loader = Loader('bronze')
    
    for i in csv_list:
        csv_path = os.path.join('data/csv', i)
        t = Transformer(csv_path)
        print(i)
        file_name = i.replace('.csv', '')
        # t.save_as_geojson(file_name)
        loader.import_to_db(t.gdf, file_name)