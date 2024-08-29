#!/usr/bin/python3
import argparse
blocksize = '4k'
rwmix = '100'
rwtype = 'rw'
options = {'bs': blocksize, 'rwmixread': rwmix, 'readwrite': rwtype}

def read_file(fio_conf):
    section_name = 'noname'
    fconf = {}
    with open(fio_conf, 'r') as fp:
        for newline in fp:
            line = newline.strip("\n")
            if line.startswith("["):
                section_name = line.strip("[]")
                fconf[section_name] = {}
                continue
            if line.startswith("#"):
                continue
            if line.strip(' \t') == '':
                continue
            if '=' in line:
                key, value = line.split("=")
            else:
                key = line
                value = ''
            if section_name not in fconf:
                fconf[section_name] = {}
            fconf[section_name][key] = value
    return fconf

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="file name")
args = parser.parse_args()

file_name = args.file
data_dict = read_file(file_name)
data_dict['global'].update(options)
print(data_dict)

for sec in data_dict:
    print ('[' + sec + ']')
    for key, value  in data_dict[sec].items():
        if value == '':
            print (key)
        else:
            print(f'{key}={value}')

