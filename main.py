from models.transform import Transformer, os

if __name__ == '__main__':
    csv_list = os.listdir('data/csv')
    
    for i in csv_list:
        csv_path = os.path.join('data/csv', i)
        t = Transformer(csv_path)
        print(i)
        print(t.df.head())
        print(t.gdf.head())
        file_name = i.replace('.csv', '')
        t.save_as_geojson(file_name)