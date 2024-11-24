subtriangles = ['abcdefghi', 'dnsekx py', 'jklmnopqr', 'stuvwxyz ', 'fgcrlaoui', 'htqjbmwvz', 'otpaxvzer', 'yuiqsdfgh', 'jklmwcbn ']
o = '58 49 69 19 15 42 99 61 19 15 79 99 14 24 49 53 71 98 72 71 82 79 27 44 74 22 49 24 24 98 49 44 56 33 32 35 82 42 27 74 74 98 99 45 24 93 32 24 27 52 57 14 49 67 71 79 86 42 99 21 24 69 78 49 21 54 19 24 44 36 58 21 59 88 78 27 32 22 71 71 73 49 66 24 15 23 42 74 55 27 42 71 78 17 24 41 53 89 79 78 76 78 98'

trapezes = ['abcdefghijklmnopqrstuvwxyz', 'dnsekxpyhtqjbmwvzfgcrlaoui', 'otpaxvzeryuiqsdfghjklmwcbn']

def main(opgave):
    oplossing = ''

    for num in opgave.split(' '):
        a = int(num[0])
        b = int(num[1])
        
        oplossing += subtriangles[a-1][b-1]
        #print(oplossing)
        l = subtriangles[a-1][b-1]
        print('{} = {}{} = {}'.format(l, a, b, letter_to_nums(l)))
        
def letter_to_nums(letter):
    opl = []
    for i in range(len(subtriangles)):
        id = subtriangles[i].find(letter)
        if id >= 0:
            opl.append((i+1, id+1))
    return opl

def nums_to_letter(num1, num2):
    return subtriangles[num1-1][num2-1]

def solve_c():
    opg = 'TMPWTDPUWJPBTMPTPWTNUDMGTQTBPAWKXTPATDUXMGPGPGPYUPTKPUMPTCQUDBTMTDVMAGXTMAGXBPVPTBMGPGPWTDUAGXJPJQXEMUYKMPGPZJPTPWTMXTMAGXHPWPUMAGXUAHBGWBGBTM'
    count = {}
    for i in range(0, len(opg), 2):
        l1 = opg[i]
        l2 = opg[i+1]
        symb = '{}{}'.format(l1, l2)
        if symb in count.keys():
            count[symb] += 1
        else:
            count[symb] = 1
    print(count)
    print(len(count.keys()))

def plf(c1, c2):
    l1 = ''
    l2 = ''

    nums1 = letter_to_nums(c1)
    nums2 = letter_to_nums(c2)

    new_pairs1 = []
    new_pairs2 = []

    for (n1, n2), (i1, i2) in zip(nums1, nums2):
        c1 = nums_to_letter(n1, i2)
        c2 = nums_to_letter(i1, n2)

        if c1 not in l1:
            l1 += c1
        if c2 not in l2:
            l2 += c2
    
    return l1, l2

def bifid(c1, c2):
    l1 = ''
    l2 = ''

    nums1 = letter_to_nums(c1)
    nums2 = letter_to_nums(c2)

    for n1, n2 in nums1:
        for i1, i2 in nums2:
            c1 = nums_to_letter(n1, i1)
            c2 = nums_to_letter(i2, n2)

            if c1 not in l1:
                l1 += c1
            if c2 not in l2:
                l2 += c2
    
    return l1, l2

def opg_c_print():

    l1, l2 = bifid('t', 't')
    print('{}|{};'.format(l1, l2))

def vigenere(c1, c2, alles=False):

    nums1 = letter_to_nums(c1)
    nums2 = letter_to_nums(c2)

    l = []

    if alles:
        for n1, n2 in nums1:
            for i1, i2 in nums2:
                nn1 = (n1 + i1) % 10
                nn2 = (n2 + i2) % 10

                if nums_to_letter(nn1, nn2) not in l:
                    l.append(nums_to_letter(nn1, nn2))
        return l

    for (n1, n2), (i1, i2) in zip(nums1, nums2):

        nn1 = (n1 + i1) % 10
        nn2 = (n2 + i2) % 10

        l.append(nums_to_letter(nn1, nn2))
    
    return l

def vigenere_alt(c1, c2):
    res = []
    for i in [0, 1, 2]:
        n1 = trapezes[i].find(c1)
        n2 = trapezes[i].find(c2)

        nn = (n1+n2)%len(trapezes[0])
        res.append(trapezes[i][nn])
    
    return res

def opg_c():
    opg = 'TMPWTDPUWJPBTMPTPWTNUDMGTQTBPAWKXTPATDUXMGPGPGPYUPTKPUMPTCQUDBTMTDVMAGXTMAGXBPVPTBMGPGPWTDUAGXJPJQXEMUYKMPGPZJPTPWTMXTMAGXHPWPUMAGXUAHBGWBGBTM'.lower()
    
    opl1 = []
    opl2 = []

    for i in range(0, len(opg), 2):
        letter1 = opg[i]
        letter2 = opg[i+1]

        l1, l2 = plf(letter1, letter2)
        opl1.append('{};'.format(l1))
        opl1.append('{};'.format(l2))

    for o in opl1:
        print(o)
    

def opg_c_vig():
    opg = 'TMPWTDPUWJPBTMPTPWTNUDMGTQTBPAWKXTPATDUXMGPGPGPYUPTKPUMPTCQUDBTMTDVMAGX'.lower()
    key = 'TMAGXBPVPTBMGPGPWTDUAGXJPJQXEMUYKMPGPZJPTPWTMXTMAGXHPWPUMAGXUAHBGWBGBTM'.lower()

    for a, b in zip(opg, key):
        print(vigenere(a, b, True))

        


def opg_b():
    opg = 'CFGFN QOMCYBLMKTRFVFNTVTBV SFMVRYKTVANMUBCMUF MSLWTMVBYAWFNSTTRF HFCMXHEJZQFFLTRFRSTJEBRJYBCDFMTWLBNSMFTFEEMFTN UQGBEKFRWCSTMWRYO'.lower()
    
    for l in opg:
        nums = letter_to_nums(l)
        opl = ''
        for i,j in nums:
            opl += nums_to_letter(j,i)
            opl += ' '
        print(opl)    


if __name__=='__main__':

    opg_c()

    


        





   

