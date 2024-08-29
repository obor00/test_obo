import configparser
import re

config = configparser.ConfigParser()
#config.SECTCRE = re.compile(r"=====\s*([a-z0-9A-Z ]+\s*)\s*======")
config.SECTCRE = re.compile(r"===== *(?P<header>[^]]+?) *======")
config.read_file(open('discover.out.hacked'))

# getfloat() raises an exception if the value is not a float
# getint() and getboolean() also do this for their respective types

print (config.sections())
for sec in config.sections():
    print (config.items(sec))

for sec in config.sections():
    print (config.get(sec,'portid'))
    print (config.get(sec,'subnqn'))

#a_float = config.getfloat('Section1', 'a_float')
#an_int = config.getint('Section1', 'an_int')
#print(a_float + an_int)
#
## Notice that the next output does not interpolate '%(bar)s' or '%(baz)s'.
## This is because we are using a RawConfigParser().
#if config.getboolean('Section1', 'a_bool'):
#    print(config.get('Section1', 'foo'))
