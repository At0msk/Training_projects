def ostatk(slovar):
    kluh = list(slovar.keys())
    mas_ded = {}
    min_d = 10000000000
    n_min = 0
    for i in kluh:
        mas_ded[i] = (slovar[i][1]-slovar[i][0])
        if min_d > slovar[i][1]-slovar[i][0]:
            min_d = slovar[i][1]-slovar[i][0]
            n_min = i
    return mas_ded,min_d,n_min



"""massiv_strok = input()
massiv = massiv_strok.split()
n = int(massiv[0])
k = int(massiv[1])
slovar = {}
indeks = 1
maks_d = 0



for i in range(n):
    strok = input()
    massiv = strok.split()
    t = int(massiv[0])
    d = int(massiv[1])
    slovar[i] = [t,d]
    if t>d:
        print("NO")
        indeks = 0
    if maks_d < d:
        maks_d = d"""
n = 5
k = 2
slovar = {0:[3,3], 1:[2,2], 2:[3,6], 3:[2,4], 4:[2,6]}
maks_d =6
indeks = 1
if indeks == 1:
    try:
        slovar_sotr = {} 
        slovar_zad = {}
        for i in range(k):
            slovar_sotr[i] = (maks_d) 
            slovar_zad[i] = []
        for i in range(k):
            for j in range(k):
                if slovar_sotr[j] <= maks_d - i:
                    mas_ded,min_d,klih = ostatk(slovar)
                    if min_d != 10000000000:
                        slovar_sotr[j] = maks_d - slovar[klih][1] 
                        mas_s = slovar_zad[j]
                        mas_s.append(klih+1)
                        slovar_zad[j] = mas_s
                        del slovar[klih]
                    else:
                        break
        print("YES")
        for i in range(k):
            seth = 0
            indeks = -1
            strok = str(len(slovar_zad[i])) + " "
            for j in range(len(slovar_zad[i])):
                strok += str(slovar_zad[i][j]) + " "
            print( strok)
    except:
        print("NO")

