
import time

class FiboIter():

    def __init__(self, max :int):
        self.max =max

    def __iter__(self):
        self.n1=0
        self.n2=1
        self.counter=0
        return self
        
    def __next__(self):        
            if self.counter==0:
                self.counter+=1
                return self.n1
            elif self.counter==1:
                 self.counter+=1
                 return self.n2
            else:
                if(self.counter<=self.max):
                    self.aux=self.n1+self.n2
                #self.n1 = self.n2
                #self.n2 = self.aux
                    #swapping
                    self.n1, self.n2 = self.n2,self.aux
                    self.counter+=1
                    return self.aux
                else:
                     raise  StopIteration
                    

if __name__ == "__main__":
    fibonaci = FiboIter(5)
    for element in fibonaci:
        print(element)
        time.sleep(1)