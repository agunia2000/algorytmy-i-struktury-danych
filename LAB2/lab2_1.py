"""Hanoi rekurencyjnie"""

from time import  *

S=['sour']
D=['dest']
B=['buff']

licznik=0

def przenies(a,b):
    global licznik
    licznik+=1
    print(licznik,'. from', a, 'to', b)
    print('   ',S, B, D)


def Hanoi(n, S, D, B):
    if n==1:
        D.append(S.pop())
        przenies(S[0], D[0])
    else:
        Hanoi(n-1, S, B, D)
        D.append(S.pop())
        przenies(S[0], D[0])
        Hanoi(n-1, B, D, S)


print('Hanoi rekurencyjnie')
print('Podaj ilosc krazkow:' )
number=input()
n=int(number)

for m in range(n):
    S.append(n-m)

print(S, B, D)
time0=perf_counter()
Hanoi(n,S,D,B)
time1=perf_counter()-time0
print('Ilosc ruchow:',licznik)
print('Czas wykonania:',time1)

