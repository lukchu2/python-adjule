
n=[int(s) for s in input().split()] #pobieram 2 zmienne: n[0] ;iczba woerszy n[1] liczba kolumn
i=0 #iterator pętli
jed=[] #lista w której będą zapisywane liczby
while i<n[0]: #pętla która zapisuje liczby w liście dwuwymiarowej w postaci [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '11', '12']]
                #pod jed[0] kryje się ['1', '2', '3', '4'], składniki tej listy są kolejnymi listami
                #pod jed[0][2] kryje się 3 itd  nazwa_listy_głównej[numer_listy_wewnętrznej][nr_składnika_listy_wewnętrz...] wszystko w listach jest numerowane od 0
    a=input().split() #pobiera wiersz jako listę
    jed.append(a) #dodaje go na końcu jako składnik listy głównej
    i=i+1
i=n[0]-1 #i=liczba wierszy z początku zadania która wykorzustana jest tutaj jako liczba kolumn
j=0
#pętla wyświetla po kolei pierwszy składnik ostatniej podlisty, pierwszy drugiej podlisty i pierwszy składnik pierwszej podlisty
#następnie drugi z trzeciej podlisty drugi z drugiej podlisty i drugi z pierwszej podlisty
#mówiąc pierwszy mam na myśli ten który jest na miejscu zerowym
while j<n[1] : #numer podlisty
    i=n[0]-1
    while i>=0 : #numer składnika podlisty
        print(jed[i][j])
        i=i-1#i jako numer podlisty maleje

    j=j+1#j jako numer skłądnika podlisty rośnie