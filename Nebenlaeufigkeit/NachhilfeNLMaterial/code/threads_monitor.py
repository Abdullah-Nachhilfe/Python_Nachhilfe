from threading import *
from time import sleep
import random

# thread-funktion
def rechne1():
    global ressource1
    global ressource2

    while(True):
        with(lock1):
            with(lock2):
                ressource1 = ressource1 + 1
                ressource2 = ressource2 + 2
                print("[1] ressource1=" + str(ressource1)+", ressource2="+str(ressource2))


def rechne2():
    global ressource1
    global ressource2

    while (True):
        with(lock2):
            with(lock1):
                ressource1 = ressource1 + 1
                ressource2 = ressource2 + 2
                print("[1] ressource1=" + str(ressource1) + ", ressource2=" + str(ressource2))


##### Hauptprogramm
global ressource1
ressource1 = 0

global ressource2
ressource2 = 0

global lock1
lock1 = Lock()
global lock2
lock2 = Lock()

t1 = Thread(target=rechne1)
t2 = Thread(target=rechne2)

print("Starte Threads....")
t1.start()
t2.start()
