from math import *
from time import *


f = open('TSP.txt', 'r')

M=[]
X=[]
Y=[]
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

for i in range (99):
   sciezka=sciezka+M[i+1]+'->'
   r=sqrt((((X[i+1]-X[i])**2)+((Y[i+1]-Y[i])**2)))
   trasa=trasa+r

sciezka=sciezka+M[0]
r=sqrt((((X[0]-X[99])**2)+((Y[0]-Y[99])**2)))
trasa=trasa+r

time1=perf_counter()-time0

print('')
print('TRASA "miasta po kolei"')
print('Trasa komiwojazera to:',sciezka)
print('Dlugosc trasy komiwojazera wyniosla:',trasa)
print('')
print('Czas wykonywania algorytmu:',time1)