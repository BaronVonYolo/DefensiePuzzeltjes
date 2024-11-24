class Side:
    def __init__(self, letters, f, r, b, l, tf, tr, tb, tl, sol=(0, 0)):
        self.letters = letters
        self.R = r
        self.F = f
        self.B = b
        self.L = l

        # tuples containing neighboring points
        self.tr = tr
        self.tf = tf
        self.tb = tb
        self.tl = tl

        self.sol = sol

    def get_letter(self):
        return self.letters[self.sol[0]][self.sol[1]]


    def rot(self, num):
        while num > 0:
            m1 = self.letters[0][0]
            self.letters[0][0] = self.letters[1][0]
            self.letters[1][0] = self.letters[1][1]
            self.letters[1][1] = self.letters[0][1]
            self.letters[0][1] = m1

            n11, n12 = self.tl[0] 
            n21, n22 = self.tl[1] 

            k11, k12 = self.tf[0] 
            k21, k22 = self.tf[1] 

            m1 = self.L[n11][n12]
            m2 = self.L[n21][n22]

            self.L[n11][n12] = self.F[k11][k12]
            self.L[n21][n22] = self.F[k21][k22]

            n11, n12 = self.tr[0] 
            n21, n22 = self.tr[1] 

            self.F[k11][k12] = self.R[n11][n12]
            self.F[k21][k22] = self.R[n21][n22]

            k11, k12 = self.tb[0] 
            k21, k22 = self.tb[1] 

            self.R[n11][n12] = self.B[k11][k12]
            self.R[n21][n22] = self.B[k21][k22]

            self.B[k11][k12] = m1
            self.B[k21][k22] = m2

            num -= 1
        return self.get_letter()

class Cube:

    def __init__(self):
        self.U = [['A', 'D'], ['B', 'C']]
        self.F = [['N', 'E'], ['O', 'F']]
        self.R = [['G', 'H'], ['P', 'Q']]
        self.L = [['U', 'T'], ['M', 'L']]
        self.B = [['K', 'S'], ['I', 'R']]
        self.D = [['Z', 'W'], ['Y', 'X']]

        self.sides_dict = {
            'U': Side(self.U, self.F, self.R, self.B, self.L, ((1, 1), (0, 1)), ((0, 1), (0, 0)), ((0, 0), (1, 0)), ((1, 0), (1, 1)), sol=(0, 0)),
            'F': Side(self.F, self.D, self.R, self.U, self.L, ((1, 1), (0, 1)), ((0, 0), (1, 0)), ((0, 0), (1, 0)), ((0, 0), (1, 0)), sol=(0, 1)),
            'B': Side(self.B, self.U, self.R, self.D, self.L, ((1, 1), (0, 1)), ((1, 1), (0, 1)), ((0, 0), (1, 0)), ((1, 1), (0, 1)), sol=(0, 0)),
            'L': Side(self.L, self.F, self.U, self.B, self.D, ((0, 1), (0, 0)), ((0, 1), (0, 0)), ((0, 1), (0, 0)), ((0, 1), (0, 0)), sol=(1, 0)),
            'R': Side(self.R, self.F, self.D, self.B, self.U, ((1, 0), (1, 1)), ((1, 0), (1, 1)), ((1, 0), (1, 1)), ((1, 0), (1, 1)), sol=(0, 0)),
            'D': Side(self.D, self.B, self.R, self.F, self.L, ((1, 1), (0, 1)), ((1, 0), (1, 1)), ((0, 0), (1, 0)), ((0, 1), (0, 0)), sol=(0, 1)),
        }

    def show_exp(self):
        print('      +-----+')
        print('      | {} {} |'.format(self.L[0][0], self.L[0][1]))
        print('      | {} {} |'.format(self.L[1][0], self.L[1][1]))
        print('+-----+-----+-----+-----+')
        print('| {} {} | {} {} | {} {} | {} {} |'.format(self.F[0][0], self.F[0][1], self.U[0][0], self.U[0][1], self.B[0][0], self.B[0][1], self.D[0][0], self.D[0][1]))
        print('| {} {} | {} {} | {} {} | {} {} |'.format(self.F[1][0], self.F[1][1], self.U[1][0], self.U[1][1], self.B[1][0], self.B[1][1], self.D[1][0], self.D[1][1]))
        print('+-----+-----+-----+-----+')
        print('      | {} {} |'.format(self.R[0][0], self.R[0][1]))
        print('      | {} {} |'.format(self.R[1][0], self.R[1][1]))
        print('      +-----+')


    def turn(self, char, num):
        side = self.sides_dict[char]

        return side.rot(num)

def main():

    opgave = 'F2F3U3R3U2 D3L1B1U3F3 R2U0U0L0 U3F0U1U0L1 D1D3 L0D0L2U3B1U2F2L1B1B1D1L2D3U3 U2L0F1D2U2D3 F0U3B2F1L0R1L2B3 R3R1U3B1F3 B3B1B2B2F2D2'

    cube = Cube()
    cube.show_exp()

    sol = ''

    for letters in opgave.split(' '):

        for i in range(0, len(letters)-1, 2):
            print('{}{}'.format(letters[i], letters[i+1]))

            letter = letters[i]
            num = int(letters[i+1])

            sol += cube.turn(letter, num)
            cube.show_exp()
            print(sol)
            print('----------------------------')

        sol += ' '

if __name__=='__main__':
    main()