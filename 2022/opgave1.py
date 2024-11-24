alph = 'abcdefghijklmnopqrstuvwxyz'

green_subs = 'groenabcdfhijklmpqstuvwxyz'

class Data:
    def __init__(self):
        self.piI = 0

data = Data()

def red(str, start=0, l=0):
    if start > 0 or l > 0:
        partial = str[start:start+l]
        opl = red(partial)
        ret = str[0:start] + opl + str[start+l:]
        return ret
    opl = ''
    for letter in str:
        if letter in alph:
            opl += alph[(alph.find(letter)+13)%len(alph)]
        else:
            opl += letter
    return opl

def orange(str, start=0, l=0):
    if start > 0 or l > 0:
        partial = str[start:start+l]
        opl = orange(partial)
        ret = str[0:start] + opl + str[start+l:]
        return ret
    opl = ''
    for letter in str:
        if letter in alph:
            new_index = len(alph) - 1 - alph.find(letter)
            opl += alph[new_index]
        else:
            opl += letter
    return opl

def yellow(str, start=0, l=0):
    if start > 0 or l > 0:
        partial = str[start:start+l]
        opl = yellow(partial)
        ret = str[0:start] + opl + str[start+l:]
        return ret
    return str[::-1]

def green(str, start=0, l=0):
    if start > 0 or l > 0:
        partial = str[start:start+l]
        opl = green(partial)
        ret = str[0:start] + opl + str[start+l:]
        return ret

    opl = ''
    for letter in str:
        if letter in alph:
            opl += alph[(green_subs.find(letter))]
        else:
            opl += letter
    return opl

def blue(str, start=0, l=0):
    if start > 0 or l > 0:
        partial = str[start:start+l]
        opl = blue(partial)
        ret = str[0:start] + opl + str[start+l:]
        return ret

    key = 'blauw'
    opl = ''
    i = 0
    for letter in str:
        if letter in alph:
            num = alph.find(letter)
            knum = alph.find(key[i%len(key)])
            opl += alph[(num-knum+len(alph))%len(alph)]
            i += 1
        else:
            opl += letter
    return opl

def violet(str, start=0, l=0):
    if start > 0 or l > 0:
        partial = str[start:start+l]
        opl = violet(partial)
        ret = str[0:start] + opl + str[start+l:]
        return ret

    opl = ''
    pi = [3, 1,4,1,5,9, 2,6,5,3,5, 8,9,7,9,3, 2,3,8,4,6, 2,6,4,3,3, 8,3,2,7,9, 5,0,2,8,8, 4,1,9,7,1, 6,9,3,9,9, 3,7,5,1,0,5,8,2,0,9, 7,4,9,4,4, 5,9,2,3,0, 7,8,1,6,4, 0,6,2,8,6, 2,0,8,9,9, 8,6,2,8,0, 3,4,8,2,5, 3,4,2,1,1, 7,0,6,7,9]
    for letter in str:
        if letter in alph:
            num = alph.find(letter)
            opl+= alph[(num-pi[data.piI]+len(alph))%len(alph)]
            data.piI+=1
            print(data.piI)
        else:
            opl+=letter
    
    return opl
        

def indigo(str, start=0, l=0):
    if start > 0 or l > 0:
        partial = str[start:start+l]
        opl = indigo(partial)
        ret = str[0:start] + opl + str[start+l:]
        return ret
    
    opl=''
    
    key = 'indigo'
    i = 0
    for letter in str:
        if letter in alph:
            num = alph.find(letter)
            numk = alph.find(key[i])

            opl += alph[(num-numk+len(alph))%len(alph)]
            key += alph[(num-numk+len(alph))%len(alph)]

            i+=1
        else:
            opl += letter

    return opl

def main():
    string1 = 'ontcijfer en geef ' + red('nagjbbeq') + 'op de ' + orange('eiztvm')
    string2 = red('n') + ') '+red('nyf ebbq') + orange('kofh') + ' ' + yellow('leeg') + ' '+ orange('rh lizmqv')+',' +yellow(red('anq fv gnj'))
    string3 = orange(yellow('dfzoy')) + ' ' + red(orange('xbsu')) + ' ' + yellow(orange(red('?biig')))
    string4 = green('r') + ') ' + green('bqlnk') + ' ' + yellow(green('qunih ne sd')) + ' ' + orange(green('nzj')) + ' ' + red(green('tqycx')) + ' ' + green('jggq')
    string5 = blue(green(blue('pa wyhlp duc wlln ou aineopvmahj efg klal?'), 19, 12), 21, 7)

    string6 = indigo('k') + ') ' + indigo(green(yellow(orange(red(red(blue('fpn trbbry xfvehzf hstag ts kwhbmw'), 4, 6), 19, 5), 19, 5), 19, 5), 19, 5),28,6)
    string7 = violet(orange(red(yellow(indigo('endz bwjd jrvzylsks up ?ppjrro paiidhuawsn icgi'), 23, 24), 23, 4), 40, 6), 28, 11)
    string8 = violet('l') + ') ' + yellow(violet(violet(yellow(blue('i fifviri hlg')), 0, 3), 4, 7), 4, 7) + violet(indigo(blue(green(yellow(indigo(violet(orange(red(orange(red(indigo('qg ujtm ffkb') + 'w', 0, 2), 0, 2), 12, 1), 12, 1), 3, 9), 3, 4), 7, 6), 12, 1), 12, 1), 12, 1), 7, 6)
    string8 += red(violet(indigo(blue(green(yellow(orange('b')))))))
    string8 += orange(red(violet(indigo(blue(green(yellow('l')))))))
    string8 += yellow(orange(red(violet(indigo(blue(green('o')))))))
    string8 += green(yellow(orange(red(violet(indigo(blue('w')))))))
    string8 += blue(green(yellow(orange(red(violet(indigo('k')))))))
    string8 += indigo(blue(green(yellow(orange(red(violet('h')))))))
    string8 += violet(indigo(blue(green(yellow(orange(red('p')))))))
    string8 += red(violet(indigo(blue(green(yellow(orange('z')))))))
    string8 += orange(red(violet(indigo(blue(green(yellow('?')))))))



    print(string1)
    print(string2)
    print(string3)
    print(string4)
    print(string5)
    print(string6)
    print(string7)
    print(string8)


if __name__=='__main__':
    main()