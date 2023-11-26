strok = input()
strok_mas = strok.split()
shet = 0
n_h = int(strok_mas[0])
m_h = int(strok_mas[1])
for i in range(n_h):
    i_h = str(i)
    i_d = len(i_h)
    polin = ""
    for j in range(i_d):
        polin += i_h[-len(i_h)+1+j]
    while (len(polin) != max(len(strok_mas[1])-1,len(strok_mas[0]))-1):
        polin += "0"
    if int(polin) < m_h:
        shet += 1
        print(" ",polin)
            
print(shet)
