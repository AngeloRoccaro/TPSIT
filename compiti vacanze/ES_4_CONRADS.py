def main(): 
 dizionario = {'a':'p','b':'q','c':'r','d':'s','e':'t','f':'u','g':'v','h':'W','i':'x','j':'y','k':'z','l':'a','m':'b','n':'c','o':'d','p':'e','q':'f','r':'g','s':'h','t':'i','u':'j','v':'k','W':'l','x':'m','y':'n','z':'o'}
 stringa= (input("Inserire la striga da codificare o decodificare"))

 codifica_decodifica(dizionario,stringa)
def codifica_decodifica(dizionario,stringa):
    prossimastringa=""
    for carattere in stringa:
        if carattere in dizionario:
            prossimastringa += dizionario[carattere]
        else: prossimastringa += carattere
    print (prossimastringa)
if __name__ == "__main__":
    main()