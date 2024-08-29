import pytest

PARAMS = {'pic1': [1, 2, 3],
          'pic2': [14, 15],
          'pic3': [100, 200, 300]}

test_pic_params = [(key, el) for key, nums in PARAMS.items()
                   for el in nums]
print(test_pic_params)

class TestPic:
    def test_setup(self):
        assert True
    @pytest.mark.parametrize('file, num', test_pic_params)
    def test_pic(self, file, num):
        print(file, num)
        assert True
