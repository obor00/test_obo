import yaml



def flat_dict(dic: dict, cle: str = "", lres=[]) -> dict:  # recursive function
    for key, value in dic.items():
        if isinstance(value, dict):
            flat_dict(value, cle + key + ".", lres)  # if value is a dict, call recursively
        elif isinstance(value, list):
            for i, elt in enumerate(value):  # if value is a list, scan iter each element
                if isinstance(elt, dict):
                    flat_dict(elt, cle + key + "." + str(i) + ".", lres)  # if value is a dict, call recursively
                else:  # otherwise add element to list
                    lres.append({cle + key + "." + str(i): elt})
        else:
            # Sinon ajoute la valeur à la liste
            lres.append({cle + key: value})
    return lres


d = {
    'a': 'b',
    'f': {'c': 'd'},
    'h': ['e', {'k': 'l'}]
}

res = flat_dict(d)
print(yaml.dump(res))



