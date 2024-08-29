import pytest

@pytest.mark.tcp
class TestMark:
    @pytest.mark.short
    def test_short(self):
        pass

    @pytest.mark.most
    def test_most(self):
        pass

