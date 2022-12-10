# Os ==> Read, Write, append
import os

# # Lesen einer Datei
# if os.path.isfile('Nachhilfe.txt'):
#     fp = open('Nachhilfe.txt', 'r')
#     print(fp.read())
#     fp.close() # Close ist wichtig

# # Standard Lesen einer Datei
# with open('Nachhilfe.txt', 'r') as fp:
#     print(fp.read())

# os.remove('Nachhilfe.txt')

# Schreiben einer neuen Datei

# if not os.path.isfile('Nachhilfe.txt'):
#     with open('Nachhilfe.txt', 'w') as fp:
#         fp.write('Jeden Freitag haben wir Nachhilfe!\n')
#         fp.write('Heute machen wir eine Video zum Thema Dateien mit os')
# print(os.path.isfile('Nachhilfe.txt'))
# Lesen ....
# with open('Nachhilfe.txt', 'r') as fp:
#     print(fp.read())

# # append ...
# with open('Nachhilfe.txt', 'a') as fp:
#     fp.write('\nUm 15:30 Uhr.')

# with open('Nachhilfe.txt', 'r') as fp:
#     print(fp.read())

# Iterable: Listen, Strings, .....
# for x in interable: x "übernimmt" die Werte im iterable:

# with open('Nachhilfe.txt', 'r') as fp:
#     for line in fp:
#         print(line)

with open('tschüss.txt', 'r', encoding='utf-8') as fp:
    print(fp.read())