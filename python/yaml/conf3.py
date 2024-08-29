from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

with open('test3.yaml', 'r') as fp:
    data = load(fp, Loader=Loader)

output = dump(data, Dumper=Dumper)

print(output)
print(data)

