from threading import Thread, Lock
from time import sleep

# Sehr wichtig, ist kritische Abschnitte zu erkennen.
# Treten nur bei geteilten Resourcen auf.

# 1. Check-then-act Situationen

# zahlen = [1,2,4,8,10,-15,0,2,3,7]
# liste_lock = Lock()
# def entferneElement(liste, elem):
#     with liste_lock:
#         if elem in liste: # kritischer Abschnitt
#             sleep(0.5)
#             liste.remove(elem)

# t1 = Thread(target=entferneElement, args=(zahlen, 7))
# t2 = Thread(target=entferneElement, args=(zahlen, 7))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(zahlen)

# 2. Read-modify-write Situationen

# global_zaehler = 0
# inc_lock = Lock()
# print(global_zaehler)
# def inc():
#     global global_zaehler
#     with inc_lock:
#         alter_wert = global_zaehler # Read / Lese
#         neuer_wert = alter_wert + 1 # Modify
#         sleep(0.1)
#         global_zaehler = neuer_wert # Write
    
# t1 = Thread(target=inc, args=())
# t2 = Thread(target=inc, args=())
# t1.start()
# t2.start()
# t1.join()
# t2.join()


# print(global_zaehler)

# 3. Moderfizierende Zuweisungen:

global_zaehler = 0
mod_lock = Lock()
print(global_zaehler)
def inc():
    global global_zaehler
    with mod_lock:
        alter_wert = global_zaehler
        alter_wert += 1
        sleep(0.1)
        global_zaehler = alter_wert
    
t1 = Thread(target=inc, args=())
t2 = Thread(target=inc, args=())
t1.start()
t2.start()
t1.join()
t2.join()


print(global_zaehler)