import copy

t={'a': 1}
l=['c', 'd', 'e']
bconf = {'a': []}
for n in l:
    newt = copy.deepcopy(t)
    newt['a'] = n
    #newt.update({'a': n})
    print(newt)
    bconf['a'].append (newt)
print(bconf)






