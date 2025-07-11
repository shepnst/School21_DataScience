import sys


def letter(email):
    with open('employees.tsv', 'r') as file:
        for line in file:
            if line.split('\t')[2].strip('\n') == email:
                name = line.split('\t')[0].strip('\n')
                return f'Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.'
            else:
                continue


if __name__ == '__main__':

    if len(sys.argv) == 2:
        arg = sys.argv[1]
        if letter(arg) == None:
            print('sorry, such email wasnt found')
        else:
            print(letter(arg))
    else:
        raise ValueError('wrong number of arguments')
