from time import *

f = open('patterns/8000_pattern.txt', 'r')
txt=f.read()

N=8000

P=['A','B','C','B','C']
S=[]

licznik=0
q=11111111

time000=time()
T=list(txt)
for i in range(N):
      del T[i*N+N]

for i in range(N*N):
    S.append('')

time001=time()-time000

time0=time()
p=0
for i in range(5):
    p=(16*p+ord(P[i]))%q

for i in range (N-2):
    for j in range (N-2):
        x=(i*N)+j
        ts=(65536*ord(T[x])+4096*ord(T[x+1])+256*ord(T[x+2])+16*ord(T[x+N])+ord(T[x+2*N]))%q
        S[x]=ts
time00=time()-time0

time1=time()
for i in range (N-2):
    for j in range (N-2):
        x=(i*N)+j
        if p==S[x]:
            if T[x]=='A' and T[x+1]=='B' and T[x+2]=='C' and T[x+N]=='B' and T[x+2*N]=='C':
                licznik=licznik+1
time2=time()-time1

print('')
print('Czas tworzenia tablicy z tekstem:',time001)
print('')
print('Czas przygotowania algorytmu "Rabina-Karpa":',time00)
print('')
print('W macierzy o wielkosci', N, 'x', N, 'liczba wystapien wzorca wyniosla:',licznik)
print('Czas wykonania algorytmu "Rabina-Karpa":',time2)
