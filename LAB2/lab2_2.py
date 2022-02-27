"""Hanoi iteracyjnie"""


from time import  *

S=['sour']
D=['dest']
B=['buff']

licznik=0
i=1

def przenies(a,b):
    global licznik
    licznik+=1
    print(licznik,'. from', a, 'to', b)
    print('   ',S, B, D)



def Hanoi(n, S, D, B):
    global i
    while S!=['sour'] or B!=['buff']:
        if i%3==1 and n%2==1:
            try:
                if S[-1]<D[-1] and  S[-1]!='sour':
                    D.append(S.pop())
                    przenies(S[0], D[0])

                elif D[-1]<S[-1] and D[-1]!='dest':
                    S.append(D.pop())
                    przenies(D[0], S[0])
            except:
                if D[0]=='dest' and S[-1]!='sour':
                    D.append(S.pop())
                    przenies(S[0], D[0])

                elif S[0]=='sour' and D[-1]!='dest':
                    S.append(D.pop())
                    przenies(D[0], S[0])
        if i%3==2 and n%2==0:
            try:
                if S[-1]<D[-1] and  S[-1]!='sour':
                    D.append(S.pop())
                    przenies(S[0], D[0])

                elif D[-1]<S[-1] and D[-1]!='dest':
                    S.append(D.pop())
                    przenies(D[0], S[0])
            except:
                if D[0]=='dest' and S[-1]!='sour':
                    D.append(S.pop())
                    przenies(S[0], D[0])

                elif S[0]=='sour' and D[-1]!='dest':
                    S.append(D.pop())
                    przenies(D[0], S[0])

        if i%3==1 and n%2==0:
            try:
                if S[-1]<B[-1] and S[-1]!='sour':
                    B.append(S.pop())
                    przenies(S[0], B[0])

                elif B[-1]<S[-1] and B[-1]!='buff':
                    S.append(B.pop())
                    przenies(B[0], S[0])
            except:
                if B[0]=='buff' and S[-1]!='sour':
                    B.append(S.pop())
                    przenies(S[0], B[0])

                elif S[0]=='sour' and B[-1]!='buff':
                    S.append(B.pop())
                    przenies(B[0], S[0])

        if i%3==2 and n%2==1:
            try:
                if S[-1]<B[-1] and S[-1]!='sour':
                    B.append(S.pop())
                    przenies(S[0], B[0])

                elif B[-1]<S[-1] and B[-1]!='buff':
                    S.append(B.pop())
                    przenies(B[0], S[0])
            except:
                if B[0]=='buff' and S[-1]!='sour':
                    B.append(S.pop())
                    przenies(S[0], B[0])

                elif S[0]=='sour' and B[-1]!='buff':
                    S.append(B.pop())
                    przenies(B[0], S[0])
        if i%3==0:
            try:
                if B[-1]<D[-1] and B[-1]!='buff':
                    D.append(B.pop())
                    przenies(B[0], D[0])

                elif D[-1]<B[-1] and D[-1]!='dest':
                    B.append(D.pop())
                    przenies(D[0], B[0])
            except:
                if D[0]=='dest' and B[-1]!='buff':
                    D.append(B.pop())
                    przenies(B[0], D[0])

                elif B[0]=='buff' and D[-1]!='dest':
                    B.append(D.pop())
                    przenies(D[0], B[0])
        i=i+1

print('Hanoi iteracyjnie')
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

