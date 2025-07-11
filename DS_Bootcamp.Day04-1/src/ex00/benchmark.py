import timeit




def loop_emails(emails):
    res=[]
    for e in emails:
        if e.endswith('@gmail.com'):
            res.append(e)
    return res

def list_comprehension(emails):
    return [e  for e in emails if e.endswith('@gmail.com')]

def realisation():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    exec_loop=timeit.timeit(lambda: loop_emails(emails), number = 90000000)
    exec_list_compr=timeit.timeit(lambda: list_comprehension(emails), number = 90000000)
    if exec_list_compr<=exec_loop:
        print('it is better to use a list comprehension')
    else:
        print('it is better to use a loop')
    print(f'{min(exec_loop, exec_list_compr)} vs {max(exec_loop, exec_list_compr)}')


if __name__=='__main__':
    realisation()