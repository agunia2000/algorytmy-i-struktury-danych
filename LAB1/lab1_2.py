"""Sortowanie przez scalanie"""

from random import *
from time import *

print('Sortowanie przez scalanie')
print('Podaj dlugosc ciagu: ')
dlugosc=input()
n=int(dlugosc)

print('Podaj ilosc iteracji: ')
ilosc=input()
q=int(ilosc)

T=[]
alltime=0

def mergesort(A):
    if len(A)>1:
        c=len(A)//2
        L=A[:c]
        R=A[c:]
        mergesort(L)
        mergesort(R)

        i=j=k=0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k]=L[i]
                i+=1
            else:
                A[k] = R[j]
                j+=1
            k+=1

        while i < len(L):
            A[k]=L[i]
            i+=1
            k+=1

        while j < len(R):
            A[k]=R[j]
            j+=1
            k+=1
    return A

for w in range(q) :
    A=[]
    for p in range(n):
        x=random()
        A.append(x)

    time0=time()
    mergesort(A)
    time1=time()-time0
    alltime+=time1
    T.append(time1)

T.sort()
print('Calkowity czas wykonania wszystkich iteracji:',alltime)
print('Czas najszybszej iteracji:',T[0])
print('Czas najwolniejszej iteracji:',T[q-1])
print('Sredni czas iteracji',alltime/q)
