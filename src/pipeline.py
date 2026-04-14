from src.utils import extract_data, transform_data, load_data

def run_pipeline():
    print("Pipeline started...")

    data = extract_data()
    transformed = transform_data(data)
    load_data(transformed)

    print("Pipeline completed!")