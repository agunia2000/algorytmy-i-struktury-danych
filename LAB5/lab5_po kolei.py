from time import *
from random import *

f = open('packages/packages500.txt', 'r')

size=500

h_bp=w_bp=size
val_bp=0
I=[]
W=[]
H=[]
V=[]
R=[]
BP=[]

for line in f:
    try:
        l=line.split(',')
        i=l[0]
        w=l[1]
        h=l[2]
        v=l[3]
        I.append(int(i))
        W.append(int(w))
        H.append(int(h))
        V.append(int(v))
    except:
        continue

time0=perf_counter()

for i in range(len(I)):
    iden=I[i]-1
    if W[iden]<=w_bp and H[iden]<=h_bp:
        BP.append(I[iden])
        h_bp=h_bp-H[iden]
        w_bp=w_bp-W[iden]
        val_bp=val_bp+V[iden]
    elif W[iden]<=h_bp and H[iden]<=w_bp:
        BP.append(I[iden])
        h_bp=h_bp-W[iden]
        w_bp=w_bp-H[iden]
        val_bp=val_bp+V[iden]

time1=perf_counter()-time0

print('')
print('Algorytm "po kolei"')
print('Czas wykonania algorytmu:',time1)
print('Wielkosc plecaka:',size,'x',size)
print('Wartosc przedmiotow w plecaku:',val_bp)
print('Ilosc przedmiotow w plecaku:',len(BP))