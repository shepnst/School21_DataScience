import sys


def ceasar(command, text, shift):
    result = []
    shift = int(shift)
    for ch in text:
        if ch.isalpha():
            if not ('a' <= ch <= 'z' or 'A' <= ch <= 'Z'):
                raise ValueError(
                    'The script does not support your language yet.')
            if ch.islower():
                base = ord('a')
            else:
                base = ord('A')
            offset = ord(ch)-base
            if command == 'encode':
                shifted = (offset+shift) % 26
            elif command == 'decode':
                shifted = (offset-shift) % 26
            sh_ch = chr(base+shifted)
            result.append(sh_ch)

        else:
            result.append(ch)

    return result


if __name__ == '__main__':

    if len(sys.argv) == 4:
        command = sys.argv[1]
        text = sys.argv[2]
        shift = sys.argv[3]
        if command not in ['encode', 'decode']:
            raise ValueError('wrong command')
        else:
            try:
                print(''.join(ceasar(command, text, shift)))
            except ValueError as error:
                print(error)
    else:
        print('wrong number of arguments')
        sys.exit(0)
