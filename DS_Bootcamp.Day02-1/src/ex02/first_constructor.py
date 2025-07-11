import sys, os


class Research:
    def __init__(self, path):
        self.path=path

    def file_reader(self):
        with open(self.path, 'r') as file:
            lines=file.readlines()
        
        if len(lines)<2:
            raise ValueError('number of line should be greater than 2')
        if len(lines[0].strip().split(','))!=2:
            raise ValueError('there should be TWO headers')
        for i in range(1, len(lines)):
            if lines[i][0] not in ['0', '1'] or lines[i][2] not in ['0', '1']:
                raise ValueError('the file should contain only 0 and 1')

        return [l.strip() for l in lines]


if __name__=='__main__':
    if len(sys.argv) == 2:
        path = sys.argv[1]
        r=Research(path)
        content=r.file_reader()
        for l in content:
            print(l)

    else:
        raise ValueError('you should pass the path')
