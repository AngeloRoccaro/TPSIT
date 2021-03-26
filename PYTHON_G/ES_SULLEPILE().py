def main():
    stringa = input("inserisci la stringa: ")
    verifica(stringa)

def verifica(stringa):
    ris = True
    k=0
    pila = []
    for elemento in stringa:
        if elemento == "{" or elemento == "[" or elemento == "(":
            pila.append(elemento)
            k=k+1
        if elemento == "}" or elemento == "]" or elemento == ")":
            x = pila.pop()
            k=k-1
            if (x=="{" and elemento!="}"):
                ris = False
            if (x=="[" and elemento!="]"):
                ris = False
            if (x=="(" and elemento!=")"):
                ris = False
    if (k!=0):
        ris=False
    if (ris==True):
        print("corretta")
    else:
        print("sbagliata")

if __name__=="__main__":
    main()