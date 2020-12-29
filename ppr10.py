a=[int(s) for s in input().split()] #pobieram wszystko do jedej listy
i=0
while a[i]!=-1 : # pierwszy warunek załatwiamy już na wstępie: całość wykonuje sie tak długo aż w liście nie znajdzie -1
    if a[i]==0 : #jeśli sprawdzane miejsce w tabeli zawiera 0 to wyświetla wszystkie poprzednie składniki tabeli z wyłączeniem 0 i 1
        j=0
        while j<i : #przelatuje po kolej przez wszystkie składniki listy do momentu na którym program napotkał 0
            if a[j]!=0 and a[j]!=1 : #jeśli sprawdzana aktualnie liczba jest różna od 0 i 1
                print(a[j]) #wypisuje tą liczbę
                j=j+1 #j++ bo sprawdzamy kolejną liczbę
            else:
                j=j+1 #jeśli sprawdzana liczba jest równa 0 lub 1 to zwiększamy iterator żeby w następnej iteracji sprawdzić kolejną liczbę ale nic nie wypisujemy bo 0 i 1 to liczby funkcyjne które nie mają być wypisywane
    if a[i]==1 :  #jeśli sprawdzana liczba jest róna 1 to liczymy średnią wszystkich dotychczasowo podanych liczb z wyłączeniem zer i jedynek
        k=0
        sr=0 #zmienna w której będzie zapisana średnia
        y=0 licznik zer i jedynek potrzebny po to żeby odjąć te "puste iteracje" i dzielić średnią przez faktyczną liczbę jej składników
        while k<i : #przelatuje po kolej przez wszystkie składniki listy do momentu na którym program napotkał 1
            if a[k]!=0 and a[k]!=1 : #jeśli sprawdzana aktualnie liczba jest różna od 0 i 1
                sr=sr+a[k] #średnia plus sktualnie sprawdzana liczba
                k=k+1 #k++ bo sprawdzamy kolejną liczbę
            else:
                y=y+1 # licznik zer i jedynek napotkanych po po drodze
                k=k+1 #k++ bo pomijamy składniki listy w których są zera i jedynku
        sr=sr/(k-y) #suma liczb zapisanych w średniej / przez liczbe składników liczby - puste składniki(tam gdzie były zera i jedynki)
        print ('%.2f'%sr) #wynik z dokładnością 2 miejsc po przecinku
    i=i+1