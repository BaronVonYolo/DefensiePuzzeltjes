key2 = ''
key1 = 'olympische winterspelen'

alph = 'abcdefghijklmnopqrstuvwxyz '
key  = 'hane dsmtbcfgijklopqruvwxyz'

new_key = 'olympischbrnaedt fgjkquvwxz'

opgave = 'ejjozhff zcortptis izsj ezq za pqre o izs aortczmt oatbze zhfdha qpf rq'

lijn1 = '.......zj........ojipmhi... ....eh....seze....z..zpkhqt '
lijn2 = '..r......g..monba....uh.z e.p. q..iuvf....jriq.ri.......'
lijn3 = 'f .q f....pn.ptmut..z..iim...g..izs qjjj..zcj.z  zu.....z'
lijn4 = '......zjfxgkt.....is...... qz t........oe...o.....tie i.'

def make_key(key1, key2):
    key = ''

    for letter in key1:
        if letter not in key:
            key += letter

    if ' ' not in key:   
        key += ' '

    for letter in key2:
        if letter not in key:
            key += letter
    
    for letter in alph:
        if letter not in key:
            key += letter

    print(key)
    
    return key

def decode(letter):
    num = key.find(letter)
    if num >= 0:
        return alph[num]
    return '.'

def decode_str(str):
    opl = ''
    for letter in str:
        opl += decode(letter)

    return opl


opl = ''
for letter in opgave:
    
    opl += decode(letter)

print(decode_str(lijn1))
print(decode_str(lijn2))
print(decode_str(lijn3))
print(decode_str(lijn4))

print(opgave)
print(opl)

groups = ['vjea']

