from threading import Thread, Lock
from time import sleep
from numpy import random
# Fehlerquelle durch Lock Tockens


# bibliothek:
bestand = 10
verliehen = 0
lock_bestand = Lock()
lock_verliehen = Lock()
def verleihe():
    global bestand
    global verliehen
    
    with lock_bestand:
            bestand_neu = bestand - 1
            sleep(random.rand() * 0.001)
            with lock_verliehen:
                verliehen_neu = verliehen + 1
                if bestand_neu >= 1:
                    bestand = bestand_neu
                    verliehen = verliehen_neu
                
def nimmzurück():
    global bestand
    global verliehen
    
    with lock_bestand:
        with lock_verliehen:
            verliehen_neu = verliehen - 1
            sleep(random.rand() * 0.001)
            bestand_neu = bestand + 1
            if verliehen_neu >= 0:
                bestand = bestand_neu   
                verliehen = verliehen_neu      

def verleihe_loop():
    for _ in range(1000):
        verleihe()
        print('%s/%s' % (bestand, bestand + verliehen))
        
def nimmzurück_loop():
    for _ in range(1000):
        nimmzurück()
        print('%s/%s' % (bestand, bestand + verliehen))
        
verleih_thread = Thread(target=verleihe_loop, args=())
zurück_thread = Thread(target=nimmzurück_loop, args=())

verleih_thread.start()
zurück_thread.start()
