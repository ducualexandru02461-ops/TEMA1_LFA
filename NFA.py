f = open("NFA.in")
w = open("NFA.out", "w")

nr_stari = f.readline().strip()
stari = {x for x in f.readline().strip().split(" ")}

nr_tranzitii = f.readline().strip()

delta = {}
for i in range (int(nr_tranzitii)): #Cream dictionarul pentru functia tranzitie
    tranzitie = f.readline().strip().split(" ")
    stare_initiala = tranzitie[0]
    stare_finala = tranzitie[1]
    litera = tranzitie[2]
    if stare_initiala not in delta: #Daca starea curenta din fisier nu este cheie in dictionar, atunci cream dictionarul din interior cu cheia "stare_initiala"
        delta[stare_initiala] = {}
    if litera not in delta[stare_initiala]: #Daca simbolul curent din fisier nu este cheie in dictionarul interior, atunci initializam o lista ce va avea drept cheie litera curenta citita din fisier
        delta[stare_initiala][litera] = []
    delta[stare_initiala][litera].append(stare_finala) #Vom adauga in lista creata anterior starea la care se poate ajunge din starea initiala.
print(delta)

stari_initiale = set()
stari_initiale = {x for x in f.readline().strip().split(" ")}
numar_stari_finale = f.readline().strip()
stari_finale = {x for x in f.readline().strip().split(" ")}

numar_cuvine_de_verificat = f.readline().strip()

for i in range(int(numar_cuvine_de_verificat)): # Luam pe rand fiecare cuvant din fisier
    cuv = f.readline().strip()
    print(cuv)
    stari_curente = stari_initiale
    for litera in cuv: # Luam pe rand fiecare simbol din cuvantul curent si actualizam multimea "stari_curente"
        stari_noi = set()
        for stare in stari_curente:
            stari_noi.update(delta.get(stare,{}).get(litera,[])) # Adaugam in multimea "stari_noi" starile la care putem ajunge din "stari_curente"
        stari_curente = stari_noi
    i = 0
    for j in stari_curente: # Dupa parcurgerea fiecarei litere din cuvant, verificam daca minim o stare din "stari_curente" se afla in "stari_finale"
        i += 1
        if j in stari_finale:
            w.write("CUVANT ACCEPTAT!")
            w.write("\n")
            break
        if i == len(stari_curente):
            w.write("CUVANT RESPINS!")
            w.write("\n")
f.close()
w.close()
