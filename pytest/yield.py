def yield_func():
    n = range(3)
    for i in n:
        yield i*i
        print ('was ' + str(i))

gen = yield_func()
print(gen)
for i in gen:
    print(i)
