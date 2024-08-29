import os
import logging
import subprocess
import pytest

def pytest_addoption(parser):
    parser = argparse.ArgumentParser()
    parser.addoption('--user', action="store", help="user")
    args, unknown = parser.parse_known_args()

