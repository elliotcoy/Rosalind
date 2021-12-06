
s = open('revc\input.txt', 'r').read() [::-1]

out = ''

for c in s:
    if c=='A':  out += 'T'
    if c=='C':  out += 'G'
    if c=='G':  out += 'C'
    if c=='T':  out += 'A'

print(out)
