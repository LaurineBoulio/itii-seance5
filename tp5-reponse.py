#Exercice 1

import numpy

def tauxdevariation(fn, a, h):
    taux = (fn(a+h)-fn(a))/h
    return taux

def fn(x):
    return 3*pow(x, 3) + 1*pow(x, 2) - 5

tauxdevariation(fn, 10, 3)


#Exercice 3

#iterative
def calcul_suite(n, u0):

    uN = u0 + n + 1

    for i in range(10):
        uN = uN + n + 1
        print(uN)

#recurrence
def calcul_suite_recurrence(n, uN):
    resp = uN + n + 1
    print(resp)
    return calcul_suite_recurrence(n, resp)


#Exercice 4	

def T(n):
    return (n**2-((n-1)**2))

def S(n):
    res = 0
    for i in range(1, n+1):
        res = res + T(i)
    return res

S(3)
	

#Exercice 5
def determiner(e, u0):
    b = 1;
    un = u0
    n = 0;
    while ( b == 1 ):
        un = uN(un)
        print(un)
        if(un < e):
            b = 0
        else:
            n+=1

    return n;

def uN(un):
    return 0.5*un

determiner(5, 2)

#Exercice 6

def val_app(epsilon): 
    elm1=1
    elm2=elm1-1/(3**2)
    signe=1
    val=5
    while abs(elm2-elm1)>epsilon:
       elm1=elm2
       elm2=elm1+signe*(1/(val**2))
       val+=2
       signe*=(-1)
    return elm2
 
print(val_app(0.05))	

#Exercice7

def limite(epsilon):
    U0 = 2
    Un = U0+2/U0
    while abs(Un-U0) > epsilon:
        U0 = Un
        Un = U0+2/U0
    return Un
 
print(limite(0.05))