# Unpacking explicite avec une liste, puis un dictionnaire
def aire_rectangle(a, b):
    return a*b

def aire_rectangle(cote1=0, cote2=0):
    return cote1*cote2

if __name__ == '__main__':
    rec1 = [3, 8, 2]
    rec2 = {'cote1':4, 'cote2':8}
    # La liste rec1 va etre depaquetee en arguments unitaires
    print (aire_rectangle(*rec1))
    # Le dictionnaire rec2 va etre depaquete en arguments unitaires
    print (aire_rectangle(**rec2))

