from threading import Thread
from time import sleep

# thread-funktion
def ausgabe(name):
    print("Thread '" + name + "' ist dran...")



# thread-funktion
def ausgabe2(name):
    while(True):
        print("Thread '"+name+"' ist dran...")
        sleep(1)


##### Hauptprogramm

t1 = Thread(target=ausgabe, args=("1"))
t2 = Thread(target=ausgabe, args=("2"))

#Zweiter Versuch...
t1 = Thread(target=ausgabe2, args=("1"))
t2 = Thread(target=ausgabe2, args=("2"))

t1.start()
t2.start()
print("Hier arbeitet wieder das Hauptprogramm...")

print("Hauptprogramm fertig.")