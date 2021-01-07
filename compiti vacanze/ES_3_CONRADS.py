def main():
    N=1
    FIBONACCI(N)
def FIBONACCI(N):
    if N <= 1:

        return N 

    else: return FIBONACCI(N-1) + FIBONACCI(N-2)
limite= int (input ("Inserire il limite dei numeri"))
for NUM in range (1,limite + 1):
  print (FIBONACCI(NUM))