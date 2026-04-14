def extract_data():
    print("Extracting data...")
    return [1, 2, 3, 4]

def transform_data(data):
    print("Transforming data...")
    return [x * 2 for x in data]

def load_data(data):
    print("Loading data...")
    print(data)