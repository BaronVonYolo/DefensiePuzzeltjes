code1 = 'npzpvnpmXoi&xbtzxAhgzihzgfhyymMfdbckct&ecck2odlbeskApbh&&kgkoD&x1kzggdrOxVgyax2&hhbD&xIdlxIodti1xyBvtt&Odhaoeqhhni2rtId&sSpffzScp1chAnpXexbAyym2of1fpmTkzfX&xEobp2accaXddk2cqqrIxl1sgxPeetPaiiOooe2btfToaXzdEd&oz1vocSaiC&lz2bverhV&ebgLqryLyry1&xIxakNzf2o&kkhiGvxoSakg1hfLxeeOgk1ibrTkXg'
code2 = 'rsslmyaDghOg&pbhpmasoRhbvivpAxzmar2nrNbbtDnbflO&b1imrPpeemlmrIkmk&lx2qokqfizoiEfsyi&qTbldgRkcmnb1hg&pIzmlMsbbAlmya2frRcAlnTmemriXty1vmObgNg&iDsmhdOqglRdvpAqm2cmyyrxNm&D&ttaOqocs1gyParkIhg&p2qokdEr&lTblhRkyvd1&l'

def rot(word, slide):
    buiten11 = word[slide:]
    buiten12 = word[0:slide]
    return '{}{}'.format(buiten11, buiten12)

def solveer(code, binnen1, binnen2, buiten1, buiten2):
    result1 = ''

    

    wiel = 1
    if wiel == 1:

        binnen = binnen1
        buiten = buiten1
    else:
        binnen = binnen2
        buiten = buiten2

    for letter in code:

        if letter == '1':
            binnen = binnen1
            buiten = buiten1
            wiel = 1
        elif letter == '2':
            binnen = binnen2
            buiten = buiten2
            wiel = 2

        elif letter >= 'a' or letter == '&':
            result1 += buiten[binnen.index(letter)]
        
        elif letter >= 'A' and letter >= '0':
            slide = buiten.index(letter)
            if wiel == 1:
                buiten1 = rot(buiten, slide)
                buiten = buiten1
            elif wiel == 2:
                buiten2 = rot(buiten, slide)
                buiten = buiten2


    print(result1)


if __name__ == '__main__':

    binnen1 = 'gklnprtvz&xysomqihfdbace'
    binnen2 = '&xysomqihfdbacegklnprtvz'
    buiten1 = 'ABCDEFGILMNOPQRSTVXZ1234'
    buiten2 = 'ABCDEFGILMNOPQRSTVXZ1234'

    #solveer(code1, binnen1, binnen2, buiten1, buiten2)

    # reset
    buiten1 = 'ABCDEFGILMNOPQRSTVXZ1234'
    buiten2 = 'ABCDEFGILMNOPQRSTVXZ1234'

    poging_binnen1 = 'gklnprtvz&xysomqihfdbace'
    poging_binnen2 = '&xysomqihfdbacegklnprtvz'

    for i in range(1, len(binnen1)):
        poging_binnen1 = rot(binnen1, i)
        #poging_binnen1 = poging_binnen1[::-1]
        print(i)
        print(buiten1)
        print(poging_binnen1)
        solveer(code2, poging_binnen1, poging_binnen2, buiten1, buiten2)





