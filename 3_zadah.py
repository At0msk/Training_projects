slov = {}
slov_y = {}
kol = int(input())
masiv_strok = []
for i in range(kol):
    masiv_strok.append(input())
for i in range(kol):
    strok = masiv_strok[i]
    mas = strok.split()
    klih = list(slov.keys())
    maxx_s = mas[0]
    if not (mas[0] in  klih):
        if mas[0] in list(slov_y.keys()):
            slov[mas[0]] = slov_y[mas[0]] + int(mas[1])
            del slov_y[mas[0]]
        else:
            slov[mas[0]] = mas[1]
    else:
        slov_y[mas[0]] = -int(slov[mas[0]]) + int(mas[1])
        del slov[mas[0]]
    sym = 0
    maxx =0
    klih = list(slov.keys())
    for j in range(len(klih)):
        sym += abs(- int(slov[klih[j]]) + int(mas[1]))
        if (maxx < abs(-int(slov[klih[j]]) + int(mas[1]))):
            maxx = abs(-int(slov[klih[j]]) + int(mas[1]))
            maxx_s = klih[j]
        elif maxx == abs(-int(slov[klih[j]]) + int(mas[1])):
            if (maxx_s >= klih[j]):
                maxx_s = klih[j]   
    print(maxx_s + " " + str(sym -2*maxx))
