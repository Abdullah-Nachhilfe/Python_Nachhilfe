from threading import Thread
from time import sleep



# thread-funktion
def thread_funktion():
    global currentValue
    while(currentValue>0):
        print("Thread - Aktueller Wert: "+str(currentValue))
        currentValue = currentValue - 1
        sleep(1)


##### Hauptprogramm
global currentValue
currentValue = 10

t1 = Thread(target=thread_funktion)

t1.start()
print("Hier arbeitet wieder das Hauptprogramm...")
t1.join()
print("Jetzt ist der Thread fertig...")

print("Hauptprogramm beendet.")
