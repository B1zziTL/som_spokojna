#otvorenie suboru
subor = open("spokojnost_1.txt","r")

#zadeklarovanie premennej
vyjadrenia = 0

#vytvorenie prazdnych slovnikov
hodiny = {}
hodiny_ano = {}
hodiny_nie = {}

for riadok in subor: #cyklus na prechadzanie riadku v subore
    #zmena poctu vyjadreni
    vyjadrenia += 1

    #nastavenie pomocnych premennych
    hodina = riadok[0]+riadok[1]
    spokojnost = riadok[6]+riadok[7]+riadok[8]

    #podmienky pre ulozenie do slovnikov
    if spokojnost == "áno":
        if not hodina in hodiny_ano.keys():
            hodiny_ano[str(hodina)] = 0

        #zmena hodnoty v slovniku
        hodiny_ano[str(hodina)] += 1

    elif spokojnost == "nie":
        if not hodina in hodiny_nie.keys():
            hodiny_nie[str(hodina)] = 0

        #zmena hodnoty v slovniku
        hodiny_nie[str(hodina)] += 1

    if not hodina in hodiny.keys():
        hodiny[str(hodina)] = 0

    #zmena hodnoty v slovniku
    hodiny[str(hodina)] += 1

#zistenie najvacsich hodnot
max_hodina_ano = max(hodiny_ano, key=hodiny_ano.get)
max_zakaznici_ano = hodiny_ano.get(max_hodina_ano)

max_hodina_nie = max(hodiny_nie, key=hodiny_nie.get)
max_zakaznici_nie = hodiny_nie.get(max_hodina_nie)

#vypisanie pozadovanych hodnot
print("Celkový počet vyjadrení:",vyjadrenia)
print(max_hodina_ano+".","hodina mala najviac spokojných zákazníkov:",max_zakaznici_ano)
print(max_hodina_nie+".","hodina mala najviac nespokojných zákazníkov:",max_zakaznici_nie)

for i in hodiny.keys(): #cyklus na prechadzanie klucov v slovniku
    #nastavenie pomocnych premennych
    dokopy = hodiny.get(str(i))
    ano = hodiny_ano.get(str(i))

    #vypocet percent
    vypocet = round((ano/dokopy) * 100,2)
    percenta = str(vypocet)+"%"

    #vypisanie pozadovanej hodnoty
    print(i+".","hodina:",percenta)

#zatvorenie suboru
subor.close()
