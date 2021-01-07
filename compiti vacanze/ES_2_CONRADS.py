import random
def main():
    genera_mac()


def genera_mac():
    caratteri="0123456789ABCDEF"
    MAC=""
    duepunti=0
    for i in range(6):
        for i in range(2):
            MAC += random.choice(caratteri)
        if duepunti < 5:
            MAC += ":"
            duepunti += 1
    print (MAC)

if __name__ == "__main__":
    main()