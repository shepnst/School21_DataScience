import sys, os



class Research:
    def __init__(self, path):
        self.path=path
        self.calculate=self.Calculations()

    def file_reader(self, has_header=True):
        with open(self.path, 'r') as file:
            lines=file.readlines()
        result=[]
        if len(lines)<2:
            raise ValueError('number of line should be greater than 2')
        if has_header and len(lines[0].strip().split(','))!=2:
            raise ValueError('there should be TWO headers')
        start_ind=0
        if has_header==True:
            start_ind=1
        for i in range(start_ind, len(lines)):
            temp=[]
            temp.append(str(lines[i][0]))
            temp.append(str(lines[i][2]))
            if temp != ['0', '1'] and temp!= ['1', '0']:
                raise ValueError('the file should contain only 0 and 1')
            result.append(list(map(int, lines[i].strip().split(','))))
        return result
    
    class Calculations:
        def counts(self, data):
            heads=0
            tails=0
            res=[]
            for i in data:
                if i[0]==1:
                    heads+=1
                if i[1]==1:
                    tails+=1
            res.append(heads)
            res.append(tails)
            return res
            
        def fractions(self, h_t):
            res=[]
            for value in h_t:
                res.append(value/sum(h_t)*100)
            return res
            

if __name__=='__main__':
    if len(sys.argv) == 2 or len(sys.argv) == 3:
        path = sys.argv[1]
        r=Research(path)
        if len(sys.argv) == 3:
            has_header=sys.argv[2]
            content=r.file_reader(has_header=has_header)
        if len(sys.argv) == 2:
            content=r.file_reader()
        counts=r.calculate.counts(content)
        fractions=r.calculate.fractions(counts)
        print(content)
        print(*counts)
        print(*fractions)

    else:
        raise ValueError('you should pass the path')
