import random
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits

def genera(lunghezza):
    if lunghezza == 8:
        simboli = ascii_lowercase + digits 
        rand = random.SystemRandom()
        password = "".join(rand.choice(simboli) for i in range (8)) 
        print(password) 
    elif lunghezza == 20:
        simboli = ascii_letters
        rand = random.SystemRandom()
        password = "".join(rand.choice(simboli) for i in range (20)) 
        print(password) 
    else:
        print("numero inserito non valido...")

def main():
    lunghezza = (int(input("inserire il numero 8 per la password semplice, mentre il 20 se si vuole una password più difficile: ")))
    genera(lunghezza)

if __name__ == "__main__":
    main()


