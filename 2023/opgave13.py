cypher = 'OJNIXOPHFWUUJBEXXCD'

cypher_alph = 'ABCDEFGHIJKLMNOPQRSTUVWX'
real_alph =   'nt--- --ie----o-------ga'

result = ''

if len(cypher_alph) != len(real_alph):
    print('YOOOO KLOPT IETS NIE MET DE LENGTES!!')

for char in cypher:
    index = cypher_alph.find(char)
    result += real_alph[index]

print(result)
