import math

# print 1. foo, 2. bar ... 
liste = ['foo', 'bar', 'bas', 'asote']
for i in range(len(liste)):
    print(str(i+1)+'. '+liste[i])


# mittelwert
summe = 0
zahlen = [18.5, 0, 5.2, -1.5, 9, 10.8]

for i in range(len(zahlen)):
    summe += zahlen[i]

n = len(zahlen)
mean = summe/n
print(mean)

# remove alle Vorkommen eines Elements
def remove_all(liste, n):
    vorkommen = liste.count(n)

    while vorkommen != 0:
        liste.remove(n)
        vorkommen -= 1

liste = [17, 3, 3, 17, 42, 17]
remove_all(liste, 17)
print(liste)

# parkplatz
fzg1 = ('UL-AB 123', 'weiß')
fzg2 = ('UL-CD 234', 'silber')
fzg3 = ('UL-EF 345', 'blau')
parkplatz = [fzg1, fzg2, fzg3]

print(parkplatz)

# Entferne das Fahrzeug mit der Nummer 'UL-CD 234'
for fzg in parkplatz:
    if fzg[0] == 'UL-CD 234':
        parkplatz.remove(fzg)

print(parkplatz)

# add Vektoren
def addiere_vektoren(vektor1, vektor2):
    # Vektor 1 als Tupel
    vektor1_x = vektor1[0]
    vektor1_y = vektor1[1]
    # Vektor 2 als Tupel
    vektor2_x = vektor2[0]
    vektor2_y = vektor2[1]
    
    return (vektor1_x+ vektor2_x ,  vektor1_y + vektor2_y) # Rückgabe wert ist ein Tupel

vektor1_x = (42, -1)
v2 = (5, 12)
v_sum = addiere_vektoren(vektor1_x, v2)
print(v_sum)

# wie viel 'i's gibt es. Einfacher mit .count('i')
mein_str = 'Dies ist ein String mit fünf "i"s.'
vorkommen_i = 0
for buchstabe in mein_str:
    if buchstabe == 'i':
        vorkommen_i += 1
ws
print(vorkommen_i)

# Ausgabe aller Zaheln von 0 bis 19, die nicht in der Liste a enthalten sind.
a = [2, 13, 6, 17, 8]
for zahl in range(20):
    if zahl not in a:
        print(zahl)

def getNorm(vektor):
    x = vektor[0]
    y = vektor[1]
    norm = math.sqrt(x**2+y**2)
    return norm

vektor1_x = (47, 11)
v2 = (32, 3)
