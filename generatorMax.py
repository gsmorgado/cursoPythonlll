import time

def fibo_gen_mac():
    n1 = 0
    n2 = 1
    counter = 0
    aux = 0
    num_max =int(input("""Set a limit for the Fibonacci Succecsion: """))
    while aux < num_max:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            if(counter <= num_max):
                aux = n1+n2
                #self.n1 = self.n2
                #self.n2 = self.aux
                # swapping
                n1, n2 = n2, aux
                counter += 1
                yield aux
            else:
                raise StopIteration


def run():
    fibonaci = fibo_gen_mac()
    for element in fibonaci:
        print(element)
        time.sleep(1)

if __name__ == '__main__':
    run()
