testo = input("Inserisci una parola o frase: ")
testo += "$"
print(testo)
lung = len(testo)
rotazioni = []
for i in range(lung):
   
    rotazione = testo[i:] + testo[:i]
    rotazioni.append(rotazione)

rotazioni.sort()


bwt = ""
for rot in rotazioni:
    bwt += rot[-1]


print("\nRISULTATI")
print("Testo finale:", testo)
print("Risultato BWT:", bwt)