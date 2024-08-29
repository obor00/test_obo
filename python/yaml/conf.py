from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

with open('test.yaml', 'r') as fp:
    data = load(fp, Loader=Loader)

output = dump(data, Dumper=Dumper)

print(output)
print(data)
print(data['debut']['i1'])

v = data.get('debut', None)
print(v)
print(data['debut']['ilist'][1])
print(data['debut']['idict']['4'])
print(data['debut']['ituple'][0])
