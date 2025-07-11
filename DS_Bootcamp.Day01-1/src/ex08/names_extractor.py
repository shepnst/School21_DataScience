import sys


def table(path):
    with open(path, 'r') as input:
        with open('employees.tsv', 'w') as output:
            output.write('Name\tSurname\tE-mail\n')
            for line in input:
                name_surname = line.split('@')[0]
                name = name_surname.split('.')[0].capitalize()
                surname = name_surname.split('.')[1].capitalize()
                output.write(f'{name}\t{surname}\t{line}')


if __name__ == '__main__':

    if len(sys.argv) == 2:
        arg = sys.argv[1]
        table(arg)
    else:
        raise ValueError('wrong number of arguments')
