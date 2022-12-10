# Globale Variablen am besten vermeiden

def foo():
    global n
    n = 42
    print('Lokal n in foo(): %s' % n)
    


n = 23
foo()
print(n)
    


# def bar():
#     n = 42 # lokal für die Funktion bar. Nur für diese Funktion sichtbar.
#     print('lokal n in bar(): %s' % n)

# n = 23 # n ist global. Für alle Funktionen im Hauptprogramm sichtbar
# bar()
# foo()
# print('Global n in Hauptprogramm: %s' % n)

