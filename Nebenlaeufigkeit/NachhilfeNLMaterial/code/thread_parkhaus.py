from threading import *
from time import sleep
import random

##################################################################################
# Achtung: dieses Programm dient der Demonstration eines Thread-Problems. 
# Die Implementierung ist zu diesemZzweck an vielen Stellen absichtlich umständlich, um das Problem eindrücklich zu demonstrieren!
##################################################################################

# Die Stellen im Code, die mit ### MAGIC CODE markiert sind, sind zunächst einfach zu ignorieren
#- sie dienen nur der Ausgabe der korrekten Anzahl an Fahrzeugen


def wait_for_light_barrier(direction):
    sleepTime = random.randint(0, 3)
    # warte für eine Zeitspanne zwischen 0 und 3 ms
    sleep(sleepTime / 1000)

def enter_from_above():
    while (True):
        # Warte auf Lichtschrankensignal
        wait_for_light_barrier("enter_from_above")
        # Erhöhe den Zähler
        update_car_counter(car_counter + 1)
        ### MAGIG CODE
        update_correct(1)

def enter_from_below():
    while (True):
        # Warte auf Lichtschrankensignal
        wait_for_light_barrier("enter_from_below")
        # Erhöhe den Zähler
        update_car_counter(car_counter + 1)

        ### MAGIG CODE
        update_correct(1)

def exit_above():
    while (True):
        # Warte auf Lichtschrankensignal
        wait_for_light_barrier("exit_above")
        # Verringere den Zähler
        update_car_counter(car_counter - 1)
        ### MAGIG CODE
        update_correct(-1)

def exit_below():
    while (True):
        # Warte auf Lichtschrankensignal
        wait_for_light_barrier("exit_below")
        # Verringere den Zähler        
        update_car_counter(car_counter - 1)

        ### MAGIG CODE
        update_correct(-1)

def update_car_counter(new_value):    
    # simuliert eine kurze Bearbeitungsdauer
    sleep(0.00001)
    global car_counter
    car_counter = new_value

### MAGIG CODE
def update_correct(inc):
    with(correct_lock_obj):
        global car_counter_correct
        car_counter_correct = car_counter_correct + inc

### MAGIC CODE
def get_car_counter_correct():
    return car_counter_correct




# Globale Variablen
car_counter = 300
car_counter_correct = car_counter
### MAGIC CODE
counter_lock_obj = Lock()
correct_lock_obj = Lock()

if __name__ == "__main__":

    # Hauptprogramm

    print("Parkhaus ist aktuell mit {} Fahrzeugen belegt".format(car_counter))
    
    # starte alle Fahrzeug-Simulations-Threads

        
    t_enter_from_above = Thread(target=enter_from_above)
    t_enter_from_below = Thread(target=enter_from_below)
    t_exit_above = Thread(target=exit_above)
    t_exit_below = Thread(target=exit_below)


    t_enter_from_above.start()
    t_enter_from_below.start()
    t_exit_above.start()
    t_exit_below.start()


    while (True):
        sleep(1)
        current = car_counter
        current_correct = get_car_counter_correct()
        print("Aktueller Zählerstand: {} (richtig: {}, Differenz: {})".format(current, current_correct, (current-current_correct)))

