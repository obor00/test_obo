
from typing import Dict, List, Union

d = {
    'entry1': {
        'k1': 1,
        'k2': 2,
        'run': 1,
        'xx': 1,
        'yy': 11 },
    'entry2': {
        'k1': 1,
        'k2': 2,
        'run': 2,
        'xx': 1,
        'yy': 10 },
    'entry3': {
        'k1': 1,
        'k2': 9,
        'run': 1,
        'xx': 2,
        'yy': 13 },
    'entry4': {
        'k1': 1,
        'k2': 2,
        'run': 3,
        'xx': 1,
        'yy': 13 },
    }


conf = {'k1': 1, 'k2': 2}

def filter_from_keys_values(adict: Dict, keys_val: Dict) -> Dict:
    filtered_dict = {}
    for fname, idic in adict.items():
        for skey, sval in  keys_val.items():
            if skey in idic:
                if sval == idic[skey]:
                    continue
            break;
        else:  # found all key match
            filtered_dict.update({fname: idic})
    return filtered_dict


res = filter_from_keys_values(d, conf)
print (res)
# build list with all y values
alist = []
for afname in res:
    alist.append(res[afname]['yy'])
print(alist)
avg = sum(alist) / len(alist)
print (min(alist), max(alist), avg)



