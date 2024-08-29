import pytest

@pytest.mark.usefixtures('my_fixture')
class TestClass:
    def test_method1(self, request, my_fixture):
        # Test logic for method 1
        print("Running test_method1",my_fixture[0])

    def test_method2(self, my_fixture):
        # Test logic for method 2
        print("Running test_method2",my_fixture[1])
