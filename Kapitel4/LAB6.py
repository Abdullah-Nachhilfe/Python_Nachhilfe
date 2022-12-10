from pprint import pprint
# 1
Studenten = {'Student 1' : 72.5, 
          'Student 2' : -1,
          'Student 3' : 51.5,
          'Student 4' : 84,
          'Student 5' : 64,
          'Student 6' : 97}
pprint(Studenten)
# 2
Studenten['Student 4'] += 0.5

print('Student 4', Studenten['Student 4']) 
# 3
for student in Studenten:
    if Studenten[student] == -1:
        nicht_teilgenommen = student
del Studenten[nicht_teilgenommen]

# 4 
def getNote(punkte):
    
    Notenschlüssel = { 5.0 : punkte < 50,
                    4.0 : 54 <= punkte <= 50,
                    3.7 : 59 <= punkte <= 54,
                    3.3 : 60 <= punkte <= 62,
                    3.0 : 63 <= punkte <= 66,
                    2.7 : 67 <= punkte <=  69,
                    2.3 : 70 <= punkte <=  74,
                    2.0 : 75 <= punkte <= 79,
                    1.7 : 80 <= punkte <= 84,
                    1.3 : 85 <= punkte <= 89,
                    1.0 : punkte >= 90}

    for key in Notenschlüssel:
        
        if Notenschlüssel[key]:
            Note = key
            return Note

# Noten = {}

# for student in Studenten:
#     punkte = Studenten[student]
#     Noten[student] = {'Punkte' : punkte, 'Note' : getNote(punkte)}
# pprint(Noten)