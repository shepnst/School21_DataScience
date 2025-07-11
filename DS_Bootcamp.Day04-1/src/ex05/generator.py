import sys
import resource
import time
import psutil


def read_csv_gen(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            yield line


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('wrong number of arguments')
        exit(1)
    else:
        file_csv = read_csv_gen(sys.argv[1])
        start = time.time()
        for i in file_csv:
            pass
        end = time.time()
        overall = end-start
        memory = psutil.Process().memory_info().rss/(1024**3)
        print(f'Peak Memory Usage = {memory:.2f} GB')
        print(f'User Mode Time + System Mode Time = {overall:.2f}s')
    print(file_csv)
