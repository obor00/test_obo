import pytest
import subprocess

TTT_VERSIONS_UPDATE = [
      {"acs-4.12", "master"},
      {"acs-4.13", "toto"}
  ]

@pytest.fixture(scope='module')
def release_from():
    rfrom, rto = zip(*TTT_VERSIONS_UPDATE)
    print(rfrom)
    yield rfrom

@pytest.fixture(scope='module')
def release_to():
    rfrom, rto = zip(*TTT_VERSIONS_UPDATE)
    yield rto


def test_one(release_from, release_to):
    print (release_from)

# @pytest.mark.parametrize("release_from, release_to", TTT_VERSIONS_UPDATE, scope='module')
def test_two(release_from, release_to):
    print (release_to)

def test_three():
    print ('hello')
