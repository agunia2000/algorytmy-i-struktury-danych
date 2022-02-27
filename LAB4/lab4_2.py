from math import *
from time import *

f = open('TSP.txt', 'r')

M=[]
X=[]
Y=[]
U=['1']
sciezka='1->'
trasa=0

for line in f:
    w=line.split("\t")
    m=w[0]
    x=w[1]
    y=w[2]
    M.append(m)
    X.append(float(x))
    Y.append(float(y))

time0=perf_counter()

prev=0
for i in range (99):
    min=1000000
    for j in range (100):
        r=sqrt((((X[j]-X[prev])**2)+((Y[j]-Y[prev])**2)))
        if r<=min and M[j] not in U:
            min=r
            min_index=j
    U.append(M[min_index])
    prev=min_index
    trasa=trasa+min
    sciezka=sciezka+(M[min_index])+'->'

time1=perf_counter()-time0

sciezka=sciezka+M[0]
r=sqrt((((X[0]-X[prev])**2)+((Y[0]-Y[prev])**2)))
trasa=trasa+r

print('')
print('TRASA "optymalna"')
print('Trasa komiwojazera to:',sciezka)
print('Dlugosc trasy komiwojazera wyniosla:',trasa)
print('')
print('Czas wykonywania algorytmu:',time1)
