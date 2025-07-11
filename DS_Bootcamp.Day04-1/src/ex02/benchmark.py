import timeit

import sys


def loop_emails(emails):
    res=[]
    for e in emails:
        if e.endswith('@gmail.com'):
            res.append(e)
    return res

def list_comprehension(emails):
    return [e  for e in emails if e.endswith('@gmail.com')]

def map_emails(emails):
    return list(map(lambda e: e if e.endswith('@gmail.com') else None, emails))

def filter_emails(emails):
    return list(filter(lambda e: e.endswith('@gmail.com'), emails))

def realisation(type, number):
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    if type=='loop':
        print(timeit.timeit(lambda: loop_emails(emails), number = number))
    elif type=='list_comprehension':
        print(timeit.timeit(lambda: list_comprehension(emails), number = number))
    elif type=='map':
        print(timeit.timeit(lambda: map_emails(emails), number = number))
    elif type=='filter':
        print(timeit.timeit(lambda: filter_emails(emails), number = number))

    commands=['loop','list_comprehension','map','filter']
    if type not in commands:
        print('unknown command')
        return

   


if __name__=='__main__':
    if len(sys.argv)==3:
        realisation(sys.argv[1], int(sys.argv[2]))
    else:
        exit(1)