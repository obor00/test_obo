import concurrent.futures
import math
import time

my_bashs = [ 'ls', 'uname', 'toto', 'titi', 'tata' ]

def run_bash(sh):
    print (sh)
    time.sleep(3)
    return '**' + sh + '--'

class Mytest:
    def run_test1 (self, p):
        print(p)
        return '**' + p + '--'


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for n1, n2  in zip(my_bashs, executor.map(run_bash, my_bashs)):
            print('%s ==> %s' % (n1, n2))

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for n1, n2  in zip(my_bashs, executor.map(Mytest().run_test1, my_bashs)):
            print('%s ==> %s' % (n1, n2))

if __name__ == '__main__':
    main()

