from pprint import pprint
from time import sleep
from numpy import random
from threading import Thread
from threading import Lock

konto_lock = Lock()

def verbuche(betrag, konto):
    with konto_lock:
        saldo_neu = konto['saldo'] + betrag
        if saldo_neu >= konto['limit']:
            sleep(0.01 * random.rand()) # künstliche
            konto['saldo'] = saldo_neu
        

konto = {'nummer' : 'ABD123',
         'saldo' : 1000,
         'limit' : -1000}

t1 = Thread(target=verbuche, args=(500, konto))
t2 = Thread(target=verbuche, args=(-500, konto))


t1.start()
t2.start()
t1.join()
t2.join()
print(konto)

