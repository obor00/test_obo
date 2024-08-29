import yaml
from yaml import load, dump
from yaml import Loader

with open('lists.yaml', 'r') as fp:
    nconf = load(fp, Loader=Loader)


print(yaml.dump(nconf))
print(nconf)
