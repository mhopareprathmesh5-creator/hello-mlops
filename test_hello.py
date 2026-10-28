from hello import greet

def test_greet():
    result = greet()
    print("Test case output:", result)
    assert result == "Hello, MLOps!"