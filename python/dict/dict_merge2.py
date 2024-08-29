#!/usr/bin/env python3

import os
import copy

def is_dict(a):
    return isinstance(a, dict)


def dict_merge(a, b):
    ''' merge b dans a si l'entrée n'existe pas
        si a est un dict, alors  merge b si b est un dict
    '''
    for key in a:
        if is_dict(a[key]):
            if key in b:
                if is_dict(b[key]):
                    a[key] = dict_merge(a[key],b[key])
    for key in b:
        if key not in a:
            a[key] =b[key]

    return a


d1 = {
        'p1': 'pval1',
        'p2': 'pval2',
        'p3': 'pval3',
        'prec': { 'sp1': 1, 'sp2':2, 'sps':{'r':66} }
        }

d2 = {
        'p1': 'pval11',
        'p2': 'pval22',
        'prec': None,
        'prec': { 'sp2':22, 'sp3': 3, 'sps':{'r':77}}
        }

print (dict_merge(d2,d1))
