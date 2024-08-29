import pytest
import logging

class Test_t1:
    def test_t1(self):
        logging.info("in test_t1")
        assert False

@pytest.mark.parametrize("setup1", [pytest.param('first_setup')], indirect=True)
@pytest.mark.usefixtures('setup1')

class Test_t2:
    def test_t2(self, setup1):
        logging.info("in test_t2")
        print("in test_t2:" + setup1)

    def test_t3(self, setup1):
        logging.info("in test_t3")
        print("in test_t3:" + setup1)
