import yaml

liste = []


def flat_dict(dic: dict, cle: str = "") -> dict:  # recursive function
    for key, value in dic.items():
        if isinstance(value, dict):
            flat_dict(value, cle + key + ".")  # if value is a dict, call recursively
        elif isinstance(value, list):
            for i, elt in enumerate(value):  # if value is a list, scan iter each element
                if isinstance(elt, dict):
                    flat_dict(elt, cle + key + "." + str(i) + ".")  # if value is a dict, call recursively
                else:  # otherwise add element to list
                    liste.append({cle + key + "." + str(i): elt})
        else:
            # Sinon ajoute la valeur à la liste
            liste.append({cle + key: value})


d = {
    'a': 'b',
    'f': {'c': 'd'},
    'h': ['e', {'k': 'l'}]
}

flat_dict(d)
print(yaml.dump(liste))



