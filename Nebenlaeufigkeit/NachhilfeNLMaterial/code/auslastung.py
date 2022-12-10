from threading import *
from time import sleep

from math import *

def threadf(nr):
    a = 10
    while(True):
        a = sqrt(a)
        #a = a*a
        print("["+str(nr)+"]: "+str(a))
        sleep(0.000001)


t1 = Thread(target=threadf, args=(1,))
t2 = Thread(target=threadf, args=(2,))
t3 = Thread(target=threadf, args=(3,))
t4 = Thread(target=threadf, args=(4,))

t1.start()
t2.start()
t3.start()
t4.start()


#for i in range(100):
#    t = Thread(target=threadf, args=(i,))
#    t.start()
