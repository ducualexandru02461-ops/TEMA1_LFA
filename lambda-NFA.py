f = open("lambda-NFA.in")
w = open("lambda-NFA.out", "w")

nr_stari = f.readline().strip()
stari = {x for x in f.readline().strip().split(" ")}

nr_tranzitii = f.readline().strip()

delta = {}
for i in range (int(nr_tranzitii)): # Cream dictionarul pentru functia tranzitie
    tranzitie = f.readline().strip().split(" ")
    stare_initiala = tranzitie[0]
    stare_finala = tranzitie[1]
    litera = tranzitie[2]
    if stare_initiala not in delta:
        delta[stare_initiala] = {}
    if litera not in delta[stare_initiala]:
        delta[stare_initiala][litera] = []
    delta[stare_initiala][litera].append(stare_finala)
print(delta)

stari_initiale = set()
stari_initiale = {x for x in f.readline().strip().split(" ")}
numar_stari_finale = f.readline().strip()
#print(numar_stari_finale)
stari_finale = {x for x in f.readline().strip().split(" ")}
#print(stari_finale)

def lambda_inchidere(stari_initiale, delta): # Functia pentru lambda-inchidere
    inchidere = set(stari_initiale)
    stiva = list(stari_initiale)
    while stiva:
        stare_curenta = stiva.pop() # Luam fiecare stare din stiva
        for stare_urmatoare in delta.get(stare_curenta, {}).get("lambda", []): # Luam fiecare stare in care putem ajunge cu "lambda" din "stare_curenta"
            if stare_urmatoare not in inchidere: # Verificam daca am adaugat deja starea la care am ajuns in "inchidere", urmand sa o adaugam, in caz contrar, in "inchidere" si in "stiva"
                inchidere.add(stare_urmatoare)
                stiva.append(stare_urmatoare)
    return inchidere

#print(lambda_inchidere(stari_initiale, delta))

numar_cuvinte_de_verificat = f.readline().strip()
#print(numar_cuvinte_de_verificat)

for i in range (int(numar_cuvinte_de_verificat)): # Luam pe rand fiecare cuvant din fisier
    cuv = f.readline().strip()
    stari_curente = lambda_inchidere(stari_initiale, delta) # Aplicam functia lambda-inchidere pentru starile initiale
    for litera in cuv: # Luam pe rand fiecare simbol din cuvant
        stari_noi = set()
        for stare in stari_curente:
            stari_noi.update(delta.get(stare, {}).get(litera, [])) # Adaugam in multimea "stari_noi" starile la care putem ajunge din "stari_curente"
        stari_curente = lambda_inchidere(stari_noi, delta)
    k = 0
    ok = 1
    for j in stari_curente: # Verificam daca cel putin o stare din multimea "stari_curente" se gaseste in multimea "stari_finale"
        if ok == 1:
            k += 1
            if j in stari_finale:
                w.write("CUVANT ACCEPTAT!")
                w.write("\n")
                ok = 0
            if k == len(stari_curente):
                w.write("CUVANT RESPINS!")
                w.write("\n")
        else:
            break
f.close()
w.close()
