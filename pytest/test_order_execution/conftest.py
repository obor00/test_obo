import pytest
import logging

@pytest.fixture(scope='session')
def name():
    logging.info('fixture name')
    yield

@pytest.fixture(scope='session')
def setup1(request):
    logging.info('fixture setup1:' + request.param)
    print('*** SETUP setup1:' + request.param + '***')
    yield 'fixture setup1:(' + request.param + ')'
