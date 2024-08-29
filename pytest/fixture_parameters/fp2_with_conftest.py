import os
import pytest

@pytest.mark.parametrize(
    'init',
    ('A', 'B', 'C', os.uname()[1]),
    indirect=True
)
def test_timeline(init):
    for i in init:
        print(i)

if __name__ == "__main__":
    pytest.main([__file__])
