

def data_types():
    a = 10
    b = "School21"
    c = 2.7
    d = True
    e = [11, 12, 13]
    f = {'name': 'Alice', 'age': 20}
    g = (11, 22, 33)
    h = {11, 22, 22, 33}
    temp = []
    temp.extend((type(a).__name__, type(b).__name__, type(c).__name__, type(
        d).__name__, type(e).__name__, type(f).__name__, type(g).__name__, type(h).__name__))
    result = '['
    for t in temp:
        result += (t+', ')
    print(result[:-2]+']')


if __name__ == '__main__':
    data_types()
