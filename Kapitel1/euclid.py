def inputInt(prompt):
    while True:
        try:
            eingabe = input(prompt)
            n = int(eingabe)
            return n
        except ValueError:
            print("Fehleingabe.")


def ggT(a, b):

    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


a = inputInt("a = ")
b = inputInt("b = ")
ggT = ggT(a, b)
print("ggT(" + str(a) + ", " + str(b) + ") = " + str(ggT))
