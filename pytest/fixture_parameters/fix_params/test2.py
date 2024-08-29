import pytest

# Define a list of greetings
greetings = [
    "Hello, World!",
    "Bonjour, le Monde!",
    "Hola, Mundo!",
    # Add more greetings as needed
]

# Parametrize the greeting fixture to provide different greetings
@pytest.fixture(params=greetings)
def greeting(request):
    return request.param

# Custom fixture to control the order
@pytest.fixture
def order_control():
    yield  # The first test will run
    yield  # The second test will run

# Test that uses the parametrized greeting fixture
@pytest.mark.run(order=1)  # Set order for the first test
def test_display_greeting_first(greeting, order_control):
    print(greeting)

# Second test that uses the parametrized greeting fixture
@pytest.mark.run(order=2)  # Set order for the second test
def test_display_greeting_second(greeting, order_control):
    print(greeting)
