import pytest

class TestMyClass:

    my_variable_value = 0

    @pytest.fixture(scope='class')
    def my_variable(self) -> int:
        return TestMyClass.my_variable_value

    def test_set_value(self):
        TestMyClass.my_variable_value = 42

    def test_use_value(self, my_variable):
        assert my_variable == 42

