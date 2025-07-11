import timeit




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

def realisation():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    exec_loop=timeit.timeit(lambda: loop_emails(emails), number = 900)
    exec_list_compr=timeit.timeit(lambda: list_comprehension(emails), number = 900)
    exec_map=timeit.timeit(lambda: map_emails(emails), number = 900)
    least_time=min(exec_loop,exec_list_compr,exec_map)
    if least_time==exec_list_compr:
        print('it is better to use a list comprehension') 
    elif least_time==exec_loop:
        print('it is better to use a loop')
    else:
        print('it is better to use a map')
    print(f'{sorted([exec_loop,exec_list_compr,exec_map])[0]} vs {sorted([exec_loop,exec_list_compr,exec_map])[1]} vs {sorted([exec_loop,exec_list_compr,exec_map])[2]}')


if __name__=='__main__':
    realisation()