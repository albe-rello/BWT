def BWT_TRANS (testo):

    testo += "$"
    print(testo)
    lung = len(testo)
    rotazioni = []
    for i in range(lung):
    
        rotazione = testo[i:] + testo[:i]
        print(rotazione)
        rotazioni.append(rotazione)

    str = rotazioni.sort()
    print("Sort: ",str)

    bwt = ""
    for rot in rotazioni:
        bwt += rot[-1]


    return bwt