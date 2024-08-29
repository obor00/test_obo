dict = { 'ref1': {
    "cle1": "valeur1",
    "cle2": "valeur2",
    "cle3": "valeur3"
},
'ref2': {
    "cle1": "valeur1",
    "cle2": "valeur3",
    "cle3": "valeur5"
},
'ref3':  {
    "cle1": "valeur1",
    "cle2": "valeur2",
    "cle3": "valeur4"
},
'ref4':  {
    "cle1": "valeur1",
    "cle2": "valeur3",
    "cle3": "valeur7"
} }

dict_keys = list(dict.keys())

grouped_refs = {}

for key in dict_keys:
    ref_values = [dict[key]['cle1'], dict[key]['cle2']]
    if tuple(ref_values) in grouped_refs:
        grouped_refs[tuple(ref_values)].append(key)
    else:
        grouped_refs[tuple(ref_values)] = [key]

for ref_values, keys in grouped_refs.items():
    print("References {} have the same values for keys 'cle1' and 'cle2': {}".format(keys, ref_values))


