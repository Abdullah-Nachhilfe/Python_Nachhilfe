from time import sleep
from threading import Thread

def langsam(text):
    for c in text:
        sleep(0.5)
        print(c, end='')
# langsam('Nachhilfe')

t1 = Thread(target=langsam , args=('Nachhilfe',))
t2 = Thread(target=langsam , args=('ASOTE',))

t1.start()
t2.start()
t1.join()
t2.join()

print('\nHier endet Das Hauptprogramm')
