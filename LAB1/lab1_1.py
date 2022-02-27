"""Sortowanie przez wstawianie"""

from random import *
from time import *

print('Sortowanie przez wstawianie')
print('Podaj dlugosc ciagu: ')
dlugosc=input()
n=int(dlugosc)

print('Podaj ilosc iteracji: ')
ilosc=input()
q=int(ilosc)

T=[]
alltime=0
for k in range(q):
    L=[]
    for i in range(n):
        x=random()
        L.append(x)

    time0=time()
    for i in range(1,len(L)) :
        x=L[i]
        j=i-1
        while j>=0 and L[j]>x :
            L[j+1]=L[j]
            j=j-1
        L[j+1]=x

    time1=time()-time0
    alltime+=time1
    T.append(time1)

T.sort()
print('Calkowity czas wykonania wszystkich iteracji:',alltime)
print('Czas najszybszej iteracji:',T[0])
print('Czas najwolniejszej iteracji:',T[q-1])
print('Sredni czas iteracji',alltime/q)
