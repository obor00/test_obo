import pytest


class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# Arrange
@pytest.fixture
def fruit_bowl():
    print("apple, banana")


@pytest.fixture
@pytest.mark.usefixtures("fruit_bowl")
def mega_fruit_bowl(fruit_bowl):
    print("abricot")
    return('hello')


@pytest.mark.repeat(3)
@pytest.mark.usefixtures("mega_fruit_bowl")
def test_fruit_salad():
    # Act
    print("test_fruit_salad")

