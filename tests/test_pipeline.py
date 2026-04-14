from src.utils import transform_data

def test_transform():
    assert transform_data([1, 2]) == [2, 4]