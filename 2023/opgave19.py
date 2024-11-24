pi = [1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]

opgaveA = 'OETLMEKVIES0TEEDSS2AEPNSTA1AENRCAELWTKBTSEETKEHAHTLEXLSNTRDONE?GEW2BUMO'
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?'

opl = ''

for i, num in enumerate(pi):
    opl += f'{chr(ord(opgaveA[i]) - num**2)}'

print(opl)