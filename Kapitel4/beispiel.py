def print_lines(lines, n=4, skip=0):
    for line in lines[skip:skip+n]:
        print(line)

monate = ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez']
print_lines(monate, skip=6, n=3)