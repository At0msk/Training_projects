kol = int(input())
massiv_strok = input()
massiv = massiv_strok.split()
result = list(map(int, massiv))
shet = 0
if kol == len(result):
    if kol%2 == 0:
        sred = 2*sum(result)/kol
        if sred.is_integer():
            result.sort()
            for i in range(int(len(result)//2)):
                if(sred - result[i] == result[-1-i]):
                    shet += 1
            if shet*2 == kol:
                print(int(sred))
            else:
                print(-1)
        else:
            print(-1)
    else:
        print(-1)
else:
    print(-1)
