import pytest
import logging

class Test_t11:
    def test_t11(self):
        logging.info("in test_t1")

@pytest.mark.parametrize("setup1", [pytest.param('first_setup')], indirect=True)
@pytest.mark.usefixtures('setup1')

class Test_t12:
    def test_t12(self, setup1):
        logging.info("in test_t12")
        #print("in test_t12:" + setup1)
        print("in test_t12:" )

    def test_t13(self, setup1):
        logging.info("in test_t13")
        print("in test_t13:" + setup1)

#@pytest.mark.parametrize("setup1", [pytest.param('first_setup')], indirect=True)
@pytest.mark.parametrize("setup1", [pytest.param('second_setup')], indirect=True)
class Test_t333:
    def test_t33(self, setup1):
        logging.info("in test_t33")
        print("in test_t33:" + setup1)

