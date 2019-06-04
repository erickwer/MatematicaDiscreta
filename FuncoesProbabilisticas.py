from fractions import Fraction
import itertools
import random
from math import factorial
from dict import dict
import csv 

class ProbDist(dict):
    "Uma distribuicao de probabilidade um mapeamento {resultado: probabilidade}"
    def __init__(self , mapping=(), **kwargs):
        self.update(mapping , **kwargs)
        total = sum(self.values())
        for outcome in self:
            self[outcome] = self[outcome]/total
            assert self[outcome] >= 0
#-----------------------------------------------------------------#
def P(evento, espaco):
    "A probabilidade de um `evento `, dado o `espaco ` amostral evento pode ser um conjunto ou predicado"
    if callable(evento):
        evento=tal_que(evento, espaco)
    if isinstance(espaco , ProbDist):
        return sum(espaco[o] for o in espaco if o in evento)
    else:
        return Fraction(len(evento & espaco), len(espaco))
#-----------------------------------------------------------------#
def tal_que(predicado,espaco):
    "O subconjunto de elementos da colecao para os quais o predicado  é verdadeiro"
    if isinstance(espaco , ProbDist):
        return ProbDist({o:espaco[o] for o in espaco if predicado(o)})
    else:
        return {o for o in espaco if predicado(o)}

#-----------------------------------------------------------------#
def eh_par(n):
    return n% 2==0
#print(P(eh_par,A))
#print(P(par,A))

#len(evento & espaço) pega o tamanho da interseção entre evento e espaço
#-----------------------------------------------------------------#
def cross(A, B):
    "O conjunto de formas de concatenar os itens de A e B (produto cartesiano)"
    return {a + b
        for a in A for b in B
        }

compra = cross('A', '12345') | cross('B', '12345') | cross('C', '12345')
# O pipe | representa a união entre os elementos
#-----------------------------------------------------------------#
def combos(items, n):
    "Todas as combinações de n itens; cada combinação concatenada em uma string"
    return{' '.join(combo)
            for combo in itertools.combinations(items, n)
           }

i =0
while i<5:
    U6 = combos(compra,i)
    i+=1

#print(U6)
#-----------------------------------------------------------------#
def escolha(n,c):
    "Número de formas de escolher c itens de uma lista com n itens"
    return factorial(n)//(factorial(c)*factorial(n-c))

## o // é divisão inteira
#-----------------------------------------------------------------#
def joint(A, B, sep=''):
    "A probabilidade conjunta de duas distribuiçoes de probabilidade independentes"
    return ProbDist({a + sep + b: A[a]*B[b]
                     for a in A
                     for b in B})


def primeiro_menina(r): return r[0] == 'G'
def primeiro_menino(r): return r[0] == 'B'
def segundo_menina(r): return r[0] == 'G'
def segundo_menino(r): return r[0] == 'B'
def duas_meninas(r): return r[0] == 'GG'
def dois_meninos(r): return r[0] == 'BB'


'''
red6 = {s for s in U6 if s.count('R')==6}
prob_red6 = P(red6, U6)
b3w2r1={s for s in U6 if s.count('B')==3 and s.count('W')==2 and s.count('R')==1}
prob_b3w2r1 = P(b3w2r1, U6)

P(b3w2r1 , U6) == Fraction(escolha(6, 3) * escolha(8, 2) * escolha(9, 1),
len(U6))

Espaco = {(1,2,3),(1),(2),(3),(4),(1,3),(2,3), (1,4), (2,4)}
ev = {(1,2,3),(1,3)}
print(P(ev,Espaco))

def clicou3ou4(a):
    print(a)
    return a[0]==(1) and a[-1]==(3)
#print(P(clicou3ou4,A))
'''
PDSexo = ProbDist(
Sexo_M=4,
Sexo_F=1
)
PDRenda = ProbDist(
    A =0,
    B =5,
    C =0,
    D =0
    )

def sexo_m(r):
    return 'Sexo_M' in r

def sexo_f(r):
    return 'Sexo_F' in r

def A(r):
    return 'A' in r
def B(r):
    return 'B' in r
def C(r):
    return 'C' in r
def D(r):
    return 'D' in r


P(sexo_f,PDSexo)
P(B,PDRenda)
# Ordem, primeiro a hipótese depois a evidencia
PDSexoRenda = joint(PDRenda ,PDSexo, ' ')
# Probabilidade de a pessoa estar no grupo B tal que o sexo
# seja feminino no PDSexo renda 
print(P(B, tal_que(sexo_f, PDSexoRenda)))


PDFaixa =  ProbDist(
    Idade_A =4,
    Idade_B =1,
    Idade_C =0,
    Idade_D =0
    )

def idade_A(r):
    return 'Idade_A' in r
def idade_B(r):
    return 'Idade_B' in r
def idade_C(r):
    return 'Idade_C' in r
def idade_D(r):
    return 'Idade_D' in r



PDFaixaRenda = joint(idade_A, B, ' ')

print(P(idade_B, tal_que(A, PDFaixaRenda)))


probComp = {s for s in U6 if s.count('A1')==1 and s.count('B1')==1 and s.count('C1')==1}
#print(P(probComp, U6))




