import pytest

@pytest.fixture(scope='class')
def my_fixture(version):
    # Setup logic
    print("Setup", version)
    yield
    # Teardown logic
    print("Teardown", version)

@pytest.mark.parametrize("version", ['v1', 'v2'], scope='class')
@pytest.mark.usefixtures('my_fixture')
class TestClass:
    def test_method1(self, version):
        # Test logic for method 1
        print("Running test_method1", version)

    def test_method2(self, version):
        # Test logic for method 2
        print("Running test_method2", version)

