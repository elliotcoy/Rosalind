
s = open('dna\\rosalind_dna.txt', 'r').read()

A = 0
C = 0
G = 0
T = 0

for c in s:
    if c=='A':
        A += 1
    if c=='C':
        C += 1
    if c=='G':
        G += 1
    if c=='T':
        T += 1

print( f'{A} {C} {G} {T}' )
