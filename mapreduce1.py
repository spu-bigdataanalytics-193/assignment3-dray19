from functools import reduce
from itertools import groupby

class mapreduce():
    
    def __init__(self,lst):
        self.lst = lst
        
    def mapping_step(self):
        self.mapping = [(word, 1) for word in self.lst]
        print(self.mapping[1:12])
        
    def shuffling_step(self):
        self.sort = sorted(self.mapping)
        print('First Group:')
        print(self.sort[1:12])
        print('==' *40)
        print('Last Group:')
        print(self.sort[123534957:123534969])
        
    def reducing_step(self):
        grouper = groupby(self.sort, lambda p : p[0])
        final = dict(map(lambda l: (l[0], reduce(lambda x,y : x + y, map(lambda p: p[1],l[1]))) ,grouper))
        return(final)
        
     
       
    
     
