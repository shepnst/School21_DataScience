import sys
from random import randint





class Research:
    def __init__(self, path):
        self.path=path
        self.data=self.file_reader()
        self.calculate=self.Calculations(self.data)

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
        def __init__(self, data):
            self.data=data

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
            
class Analytics(Research.Calculations):
    def __init__(self, data):
        super().__init__(data)

    def predict_random(self, num_predict):
        res=[]
        rand={0: [0,1], 1: [1,0]}
        for i in range(num_predict):
            res.append(rand[randint(0,1)])
        return res
    def predict_last(self):
        return self.data[-1]


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
        analytics=Analytics(content)
        predict=analytics.predict_random(3)
        predict_last=analytics.predict_last()
        print(content)
        print(*counts)
        print(*fractions)
        print(predict)
        print(predict_last)

    else:
        raise ValueError('you should pass the path')
