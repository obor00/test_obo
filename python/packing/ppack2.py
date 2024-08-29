# packing explicite
def aire_rectangle(*args):  # les arguments passes en parametre sont paquetes dans args qui se comporte comme un tuple
    if len(args) == 2:
        return args[0]*args[1]
    else:
        print('Merci de stipuler deux parametres')

def aire_rectangle2(**kwargs):  # les arguments passes en parametre sont paquetes dans kwargs qui se comporte comme un dictionnaire
    if len(kwargs) == 2:
        result = 1
        for key, value in kwargs.items():
            result *=value
        return result
    else:
        print('Merci de stipuler deux parametres')

if __name__ == '__main__':
    # Une liste va etre creee a partir des arguments fournis
    print (aire_rectangle(3,8))
    # Un dictionnaire va etre cree a partir des arguments nommes
    print (aire_rectangle2(cote1=4, cote2=8))

