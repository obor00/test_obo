import pytest
import subprocess

vg = "hi"

@pytest.fixture
def setup_conf():
    print("setup")

#@pytest.mark.repeat(2)
@pytest.mark.parametrize("name", [  './test1.sh', './test2.sh'  ])
#def test_repeat_decorator(param1,name, setup_conf):
def test_repeat_decorator(name, setup_conf):
    assert vg == "hi", "Global var HI"
    print ("my globals", vg)
    ret = subprocess.run ("bash -c ./test1.sh" , shell = True)

#def test_repeat_decorator(param1,name, setup_conf):
@pytest.mark.parametrize("name", [ [ './test1.sh', 1 ], [ './test2.sh', 2]  ])
def test_param_list(name):
    print ('premier parametre ' + name[0])
    print ('second parametre ' + str(name[1]))
    #mytools()
