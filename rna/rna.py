
s = open('rna\\rosalind_rna.txt', 'r').read()

A = 0
C = 0
G = 0
T = 0

out = ''

for c in s:
    if c=='T':
        out += 'U'
    else:
        out += c

print(out)
