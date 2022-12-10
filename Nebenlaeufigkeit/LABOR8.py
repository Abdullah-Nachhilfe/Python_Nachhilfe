import random
from time import sleep
from threading import Thread, Lock
global lager
lager = []

lager_lock = Lock()
def pruefeLager():
    i = 0
    while i != 50:
        with lager_lock:
            if len(lager) == 0: # ist lager leer?
                for _ in range(10):
                    e = random.randint(0, 100)
                    lager.append(e)
                print('Das Lager ist befüllt!\n')
                print(lager,'\n')
                sleep(0.1)
                i += 1
                print('i ist gleich: ', i)

def verbraucher(verbraucherNummer):
    while True:
        with lager_lock:
            if len(lager) != 0:
                maximum = max(lager)
                print('VerbraucherNummer: %s (Maximum: %s)'% (verbraucherNummer, maximum))
                lager.remove(maximum)

lager_prüfe_thread = Thread(target=pruefeLager, args=())
verbraucherThread1 = Thread(target=verbraucher, args=(1,))
verbraucherThread2 = Thread(target=verbraucher, args=(2,))
verbraucherThread3 = Thread(target=verbraucher, args=(3,))

lager_prüfe_thread.start()
verbraucherThread1.start()
verbraucherThread2.start()
verbraucherThread3.start()

            