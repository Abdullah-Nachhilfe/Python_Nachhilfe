import time
from random import randint
from time import sleep
from threading import Thread, Lock
lager_lock = Lock()

def prüfe_lager(lager):
    while True:
        with lager_lock:
            if len(lager) == 0:
                for _ in range(10):
                    lager.append(randint(0,100))
                print('Lager ist aufgefüllt!')
                sleep(0.1)

def verbrauche(lager, id):
    while True:
        with lager_lock:
            if len(lager) != 0:
                max_elem = max(lager)
                print('ID: %s (MaxElem: %s)' % (id, max_elem))
                lager.remove(max_elem)
        sleep(0.001)
                

lager = []
pruefe_lager_Thread = Thread(target=prüfe_lager, args=(lager,))
verbrauche_1 = Thread(target=verbrauche, args=(lager, 1)) 
verbrauche_2 = Thread(target=verbrauche, args=(lager, 2)) 
verbrauche_3 = Thread(target=verbrauche, args=(lager, 3))

pruefe_lager_Thread.start()
verbrauche_1.start()
verbrauche_2.start()
verbrauche_3.start()