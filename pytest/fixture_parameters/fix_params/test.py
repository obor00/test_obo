import pytest


# Définissez la fixture target_A_or_B
@pytest.fixture
@pytest.mark.parametrize("a_target", [
    'target_MTA',
    'target_MTB'
#    pytest.param('target_MTA'),
#    pytest.param('target_MTB')
])
def target_A_or_B(a_target):
    yield a_target


class TestContent:
    def test_example1(target_A_or_B):
        print('HELLO')
        target_name = target_A_or_B
        print(target_name)

    def test_example2(target_A_or_B):
        target_name = target_A_or_B
        print(target_name)

