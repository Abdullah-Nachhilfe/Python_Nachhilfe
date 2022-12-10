import random
import numpy as n

Gewicht = []
Groeße = []
Tage = 5

# simuliere Gweicht und Größe Annahme

for tag in range(Tage):
    sub_Gewicht = []
    sub_Groeße = []
    probanden = random.randint(8, 12)
    for person in range(probanden):
        rn_gewicht = random.randint(60, 80)
        rn_groeße = random.randint(160, 180)
        while rn_gewicht in sub_Gewicht:
            rn_gewicht = random.randint(60, 80)
        while rn_groeße in sub_Groeße:
            rn_groeße = random.randint(160, 180)
        
        sub_Gewicht.append(rn_gewicht)
        sub_Groeße.append(rn_groeße)
    Gewicht.append(sub_Gewicht)
    Groeße.append(sub_Groeße)

Gewicht_gesamt = []
Groeße_gesamt = []

for liste in Gewicht:
    Gewicht_gesamt += liste

for liste in Groeße:
    Groeße_gesamt += liste

# einen mit 62kg?
print('Es gibt', Gewicht_gesamt.count(62), 'mit 62kg.')

# Sort lists
zipped_lists = zip(Groeße_gesamt, Gewicht_gesamt)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
Groeße_sorted, Gewicht_sorted = [list(tuple) for tuple in tuples]

# # Größter Proband
print('Der größte Proband hat eine Größe von',
      Groeße_sorted[-1], 'cm und ein Gewicht von', Gewicht_sorted[-1], 'kg.')

# # zweit größte
print('Der zweit größte', Groeße_sorted[-2],
      'cm Gewicht von', Gewicht_sorted[-2], 'kg.')


# Gewicht im Mittel
perzentil = round(((len(Groeße_sorted)*10)/100))
n = perzentil
summme = 0
for i in range(perzentil):
    summme += Gewicht_sorted[i]
mean = summme/n
print('Die größten Probanden besaßen im Mittel',mean,'kg')    


gr_sorted = sorted(Groeße_gesamt)

gw_sorted = Gewicht_gesamt
j = 0
for gr in Groeße_gesamt:
    index_in_sorted = gr_sorted.index(gr)
    gr_sorted[index_in_sorted] = 0
    gw = Gewicht_gesamt[j]
    gw_sorted[index_in_sorted] = gw
    j +=1
gr_sorted = sorted(Groeße_gesamt)

# # Größter Proband
print('Der größte Proband hat eine Größe von',
      gr_sorted[-1], 'cm und ein Gewicht von', gw_sorted[-1], 'kg.')

# # zweit größte
print('Der zweit größte', gr_sorted[-2],
      'cm Gewicht von', gw_sorted[-2], 'kg.')

perzentil = round(((len(gr_sorted)*10)/100))
n = perzentil
neu_summme = 0
for i in range(perzentil):
    neu_summme += gw_sorted[i]
neu_mean = neu_summme/n
print('Die größten Probanden besaßen im Mittel',neu_mean,'kg')
print(gr_sorted)