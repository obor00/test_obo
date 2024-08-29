import os
import logging
import subprocess
import pytest

@pytest.fixture
def init(request):
    print('fixture with user:', request.param)
    return request.param

@pytest.mark.parametrize('init', [pytest.param(request.config.getoption("--report_name"))], indirect=True)
def test_timeline(init):
    for i in init:
        print(i)
    for i in initB:
        print(i)

