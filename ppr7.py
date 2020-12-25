a=int(input())
b=[int(s) for s in input().split()] #pobiera dzieli i zmienia na int liczbę

if a%2==0: #jeśli a jest podzielne przez 2 to wypisz co drugą liczbę zaczynając od pierwszej od końca
    i = len(b) - 1
    while i>0:
        print(b[i])
        i=i-2
else:    #jeśli a nie jest podzielne przez 2 to wypisz co drugą liczbę zaczynając od drugiej od końca
    i = len(b) - 2
    while i>0:
        print(b[i])
        i=i-2
