import timeit
from functools import reduce
import sys


def loop_approach(num):
    res=0
    for i in range(1,num+1):
        res+=i*i
    return res

def reduce_approach(num):
    return reduce(lambda res, i: res+i*i, range(1,num+1),0)

def realisation(type, calls, number):
    if type=='loop':
        print(timeit.timeit(lambda: loop_approach(number), number = calls))
    elif type=='reduce':
        print(timeit.timeit(lambda: reduce_approach(number), number = calls))

    commands=['loop','reduce']
    if type not in commands:
        print('unknown command')
        return

   
if __name__=='__main__':
    if len(sys.argv)==4:
        realisation(sys.argv[1], int(sys.argv[2]),int(sys.argv[3]))
    else:
        exit(1)