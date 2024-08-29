#!/usr/bin/env python3

import os
import copy

def dict_merge(a, b):
    '''recursively merges dict's. not just simple a['key'] = b['key'], if
    both a and bhave a key who's value is a dict then dict_merge is called
    on both values and the result stored in the returned dictionary.'''
    if not a: return None
    if not b:
        print ('not b')
        return a
    if not isinstance(b, dict):
        return b
    result = copy.deepcopy(a)
    for k, v in b.items():
        if k in result and isinstance(result[k], dict):
            result[k] = dict_merge(result[k], v)
        else:
            result[k] = copy.deepcopy(v)
    return result

d1 = {
        'p1': 'pval1',
        'p2': 'pval2',
        'p3': 'pval3',
        'prec': { 'sp1': 1, 'sp2':2 }
        }

d2 = {
        'p1': 'pval11',
        'p2': 'pval22',
        'prec': None,
        #'prec': { 'sp2':2, 'sp3': 3 }
        }

print (dict_merge(d1,d2))
