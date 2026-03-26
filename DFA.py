f = open("DFA.in")
w = open("DFA.out", "w")

nr_stari = f.readline().strip()
stari = [x for x in f.readline().strip().split(" ")]
nr_tranzitii = f.readline().strip()

dictionar = {}

for i in range(int(nr_tranzitii)): # Cream dictionarul pentru functia tranzitie
    litere = []
    tranzitie = [x for x in f.readline().strip().split(" ")]
    for j in range(2,len(tranzitie)):
        litere.append(tranzitie[j])
    if dictionar.get(tranzitie[0]) == None:
        dictionar[tranzitie[0]] = []
    for k in litere:
        dictionar[tranzitie[0]].append({k: tranzitie[1]})
print(dictionar)

stare_initiala = f.readline().strip()
nr_stari_finale = f.readline().strip()
stari_finale = [x for x in f.readline().strip().split(" ")]
numar_cuvinte_de_verificat = f.readline().strip()

cuv = 0

while cuv < int(numar_cuvinte_de_verificat): # Luam pe rand fiecare cuvant din fisier
    stare_curenta = stare_initiala
    cuvant = f.readline().strip()
    for i in range(len(cuvant)): # Luam pe rand fiecare simbol din cuvant
        litera = cuvant[i]
        if i != len(cuvant) - 1: # In cazul in care nu am ajuns la finalul cuvantului, verificam daca din starea curenta avem drum in alta stare
            ok = 0
            for j in dictionar.get(stare_curenta):
                if litera in j.keys():
                    ok = 1
                    stare_curenta = j[litera]
                    break
            if ok == 0:
                w.write("CUVANT RESPINS")
                w.write("\n")
                cuv += 1
                break
        else: # In cazul in care am ajuns la finalul cuvantului, verificam daca starea curenta este stare finala si trecem la urmatorul cuvant
            for j in dictionar.get(stare_curenta):
                if litera in j.keys():
                    stare_curenta = j[litera]
                    if stare_curenta in stari_finale:
                        w.write("CUVANT ACCEPTAT")
                        w.write("\n")
                        break
                    else:
                        w.write("CUVANT RESPINS")
                        w.write("\n")
            cuv += 1
