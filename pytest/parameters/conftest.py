
test_list = [ "./test1.sh", "./test2.sh" ]


def pytest_addoption(parser):
    parser.addoption("--all", action="store_true", help="run all combinations")
    parser.addoption("--script", action="store", help="run one ")

def pytest_generate_tests(metafunc):
    if "param1" in metafunc.fixturenames:
        if metafunc.config.getoption("all"):
            tlist = test_list
        else:
            #tlist = metafunc.config.getoption("--script")
            tlist = metafunc.config.getoption("script")
        print("!!!!!!!!!!!!!!!!!!!!!!!", tlist)
        # metafunc.parametrize("param1", tlist)

def mytools():
    print('hello my tool')

