n = 40

zahlenreihe = list(range(2,n))
primzahlen = []
keine_primzahlen = []

while len(zahlenreihe) != 0:
    kleinste = zahlenreihe[0]
    primzahlen.append(kleinste)
    zahlenreihe.remove(kleinste)
    for i in zahlenreihe:
        if i%kleinste == 0:
            keine_primzahlen.append(i)
            zahlenreihe.remove(i)

print(primzahlen)
print(keine_primzahlen)
print(zahlenreihe)