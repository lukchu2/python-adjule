

#robię tak ponieważ jest to najłatwiejsze znany mi sposób na pobranie kilku danych z jednej lini
#pobieram je jako jedną zmienną i dopiero wtedy dzielę z zmienna zmienia się na listę
#przykładowo jeśli na wejście będzie 3 10, tp program zapiszę  w m: "3 10" jako string po czym podzieli je na m[0]=3, m[1]=10 a następnie zamieni te liczby na inty aby mżna było wykonywać na nich działania
m=[int(s) for s in input().split()] #pobieram odpowiedznio m[0] - liczbe kandydatów
n=[int(s) for s in input().split()] #pobieram głosy, u jak wyżej dziele i zapusje w liście n na osobnych miejscach
l=[]  #lista w której będę zapisywał ile głosów mają kandydaci gdzie nr miejsca=r nakdydata
i=0
while i<=m[0] : #zapisuje 0 na miejscu wszystkich kandydatów, wykonuje się raz więcej dlatego żeby zapełnić miejsce zerowe które pomijam w dalszych działąniach dla uproszczenia sprawy
    l.append(0)
    i=i+1

i=0
while i<m[1] : #wykonuje się 10 razy
    l[n[i]]=l[n[i]]+1 #nie wygłada to zbyt przyjaźnie ale... na miejscu n[i] w tablicy l dodaje 1 bo pod n[i] kryje się nr kandydata na którego ktoś oddał głos. upraszczająć l[nr kandydata]++
    i=i+1

i=1
w=0
while i<=m[0] :
    print(i, ": ", l[i], sep="") #wyświetla i oraz to co się kryje pod l[i], po co sep? sep dfiniuje co jest separatorem. normalnie program zamiast przecina wstawia spacjęa jako że nam zależy żeby : był od razu po i to definiujemy że zamiast przecinka program ma wyświetlić "" czyli nic

    if l[i]>l[i-1] : # wyznacza kandydata z największą liczbę głosów poprzez porównanie kandydata x i kandydata x-1
        w=i #jeśli dany kandydat ma większą liczbę głosów niż poprzedni to jego numer jest zapisywany do zmiennej w
    i=i+1
print(w) #wypisuje kandydata który wygrał

