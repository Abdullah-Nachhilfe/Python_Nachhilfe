# Video Aufname
# Schreiben
# Sprechen

import time
from time import sleep
from threading import Thread

def schreiben():
    sleep(2) # 2 seconden <-> imagine 2 minuten
def sprechen():
    sleep(1) # 1 seeconde <-> imagine 1 minute

# Video Aufnahme
beginn = time.time()

for i in range(5):
    t1 = Thread(target=schreiben, args=()) # Schreibe Code
    t2 = Thread(target=sprechen, args=()) # Erkläre Code
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    end = time.time()

print('Video hat %.3f minuten gedauert.' % (end - beginn))

