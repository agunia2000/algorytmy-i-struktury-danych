from time import *

f = open('patterns/3000_pattern.txt', 'r')
txt=f.read()

N=3000

licznik=0

time000=time()
T=list(txt)
for i in range(N):
      del T[i*N+N]
time001=time()-time000

time1=time()
for i in range (N-2):
    for j in range (N-2):
        x=(i*N)+j
        if T[x]=='A' and T[x+1]=='B' and T[x+2]=='C' and T[x+N]=='B' and T[x+2*N]=='C':
            licznik=licznik+1
time2=time()-time1

print('')
print('Czas tworzenia i przygotowania tablicy z tekstem:',time001)
print('')
print('W macierzy o wielkosci', N, 'x', N, 'liczba wystapien wzorca wyniosla:',licznik)
print('Czas wykonania algorytmu "naiwnego":',time2)
