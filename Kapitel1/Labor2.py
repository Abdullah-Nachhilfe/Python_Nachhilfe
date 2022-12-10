# Denke dich eine Zahl in einem Festgelegten Suchbereich:
# Z.B. zahl = 10, Suchbereich [0,50]
# Der Computer soll diese Zahl Raten
# Suchbereich ist int, da N


# Hauptprogramm: Ich denke mir eine Zahl z.B. 10(nur für mich)
# Ich gebe dem Programm einen Suchbereich
# Das Program wirft mir eine Zahl, z.B 5 und danach fragt:
# ist diese Zahl korrekt, kleiner oder groeßer usw.

# verarbeitet Konsoleingabe --> inputs
# Zahlen für die Grenzwerte --> int für Suchbereich
# Text als Antwort vom Benutzer
# benutze try-catch

# Zahl oder Text
def konsoleneingabe_verarbeiten(option, prompt):
    while True:
        if option == "Zahl":

            try:
                grenze = input(prompt)
                n = int(grenze)
                return n
            except ValueError:
                print("Falsche Eingabe")
        elif option == "Text":
            antwort = input(prompt)
            return antwort
        else:
            print('Bitte geben Sie "Text" oder "Zahl" als erstes Parameter ein ')
            break


# Hauptprogramm
oberegrenze = konsoleneingabe_verarbeiten("Zahl", "Oberegrenze: ")
unteregrenze = konsoleneingabe_verarbeiten("Zahl", "Unteregrenze: ")
i = 1
while i == 1:

    wert = int((oberegrenze + unteregrenze) / 2)
    print("Die gesucht Zahl ist: " + str(wert) + " ?")
    antwort = konsoleneingabe_verarbeiten(
        "Text", "Ist die Antwort großer, kleiner oder richtig: "
    )
    if antwort == "richtig":
        print("Siiiiiiiiii!!!")
        i = 0
    if antwort == "kleiner":
        unteregrenze = wert
    if antwort == "großer":
        oberegrenze = wert
