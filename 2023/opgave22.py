import numpy as np
                    
matrix_list = []

def number_fits(num, x, y, matrix):
    return num not in matrix[:, y] and num not in matrix[x, :] and num not in matrix[3*(x//3):3*(x//3)+3, 3*(y//3):3*(y//3)+3]


def get_sudokus():
    matrix = np.zeros(shape=(9, 9))
    matrix[0, 0] = 1
    matrix[0, 1] = 3
    matrix[0, 2] = 5
    matrix[0, 3] = 8
    matrix[0, 4] = 6
    matrix[0, 5] = 2

    matrix[8, 7] = 1
    matrix[8, 8] = 3

    recursive_sudoku(6, matrix)

MAX = 11

def recursive_sudoku(i, matrix):
    x = i // matrix.shape[0]
    y = i % matrix.shape[1]

    for num in range(1, 10):
        if number_fits(num, x, y, matrix):
            matrix[x, y] = num

            if i == MAX:
                matrix_list.append(np.array(matrix, copy=True))
            else:
                recursive_sudoku(i+1, matrix)
        
    matrix[x, y] = 0

def brute():
    sudokus = get_sudokus()
    text = 'EHMITFTTMITLNWDQRJSNNDGTEHRHEOWDWMJTKBQISIETVUSJGRCLFAWGPNJUJTNGWKLMLTXFVGJPQGAPLFG'

    for sudoku in matrix_list:
        flat = sudoku.flatten()

        result = ''

        for char, num in zip(text, flat):
            result += rot_letter(char, int(num))

        result = f'{result[0:2]} {result[2:MAX+1]}'

        if is_cool(result.split(' ')[1]):
            print(result)

    print(len(matrix_list))

def is_cool(word):
    for klinker in 'AEUIO':
        if klinker in word[0:3]:
            return True
        
    return False


ALPH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def rot_letter(letter, num):
    pos = ALPH.find(letter)
    new_pos = pos - num
    return ALPH[new_pos]

def try_rotations():
    a = 'EH'
    b = 'FG'

    for i in range(1, 10):
        for j in range(1, 10):
            a_p = f'{rot_letter(a[0], i)}{rot_letter(a[1], j)}'
            b_p = f'{rot_letter(b[0], i)}{rot_letter(b[1], j)}'

            print(f'{i} - {j}')

            print(a_p)
            print(b_p)
            print('--------------------')

brute()


