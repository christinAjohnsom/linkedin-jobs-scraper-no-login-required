thonfrom .utils import save_json

class Exporter:
    def export(self, data):
        file_path = 'data/sample.json'
        save_json(data, file_path)
        print(f"Data saved to {file_path}")