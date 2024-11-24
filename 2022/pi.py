pi = '314159265358979323846264338327950288419716939937510'

rooster = [
    'LWVRERJPAS',
    'RNDPIGIED9',
    'TGKZEAEOKE',
    'EPRRGEAIIE',
    'ADYEDDAE8W',
    'DNIMEKA1LR',
    'IOEAAMDTSV',
    'TVBNDSEAFN',
    'AEERKEEEOI',
    'SDNATE8FDD'
]
opl = ''
for i in range(0, len(pi), 2):

    if i+1 < len(pi) and (i % 4) != 0 :
        num = int(pi[i])
        num2 = int(pi[i+1])
        opl += rooster[num2][num]

    elif i+1 < len(pi):
        num = int(pi[i])
        num2 = int(pi[i+1])
        opl += rooster[num][num2]

print(opl)