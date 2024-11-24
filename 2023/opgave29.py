def find_matches(text, line):
    for i in range(len(text)):
        match = True
        match_start_index = i
        for text_letter, letter in zip(text[i:], line):
            if not (letter == text_letter or letter == 'X' or text_letter == 'X'):
                match = False
                break
        
        if match:
            yield match_start_index

def merge_lines(line_a, line_b, from_index=0):
    new_line = line_a[:from_index]

    for i, char in enumerate(line_a[from_index:]):
        if i < len(line_b):
            new_line += line_b[i] if char == 'X' else char
            
        else:
            new_line += char

    if len(line_b) > len(line_a) - from_index:
        new_line += line_b[len(line_a) - from_index:]

    return new_line


def main():
    done = False
    text = 'Het construeren van een betegeling van hoeden is een flinke legpuzzel. ook het reconstrueren en het ontcijferen van de vraag in de volgende substitutieversleuteling is uitdagend. we gebruiken als sleutel een wezen dat geen spiegelbeeld heeft en de naam van dit probleem dat niets met albert te maken heeftwsi gfopiboi ngfpikpusteifziuifosr tvvk ricipif pvo'

    lijnen = [
        ' XX XXXXXXqXXXXXXXtXXpXXXXXXXi',
        'qXXXhXXrXXXiXXX?',
        'sXXXvXXXnXX ',
        'fXXcXXXXXXXtXXvXXXXXXf',
        'bXXtXXX XXXeXXhXXXtXXX XXoXXXo',
        'iXXfXXX XXXkXXiXXXiXXXvXXi',
        'sXXXfXXuXXXsXXtXXX XXXiXXfXXXo',
        'aXXXrXXtXXXaXXX XXeXXXsXXgXXXi',
        'bXXsXXXXXXfXXXXXXXhXXr',
        'dXXXXXXXiXXzXXXXXXXsXXXXXXXcXXb',
        'uXXXnXXXsXXlXXXeXXXeXXwXXXnXXa',
        '.XXeXXXbXXiXXX XXX XXeXXXlXXn',
        'sXXiXXXi',
        'hXXfXXXiXXfXXXbXXXnXXpXXXuXXXi',
        'rXXvXXXrXXXpXX XXX ',
        ' XXX XXXiXXt',
        ' XXXpXXXuXXeXXXiXXXoXX XXkXXi',
        ' XXtXXXXXXXgXXiXXXXXXzXXXXXXXf',
        'pXX XXXXXXsXXXXXXXfXXv',
        'gXXrXXXeXXXlXXsXXXtXX XXX XXXe',
        'pXXXeXXXeXX XXXfXXeXXXeXXXaXXv',
        'rXXXvXXrXXXXXXfXXXoXXX XXc',
        'cXXXXXXpXXXiXXXgXXm',
        'iXXaXXcp',
        ' XXXfXXXiXXfXXXsXX ',
        'eXXXwXX XXXpXXoXXXgXXXkXXs',
        'gXXXXXXtXXXXXXX XXfXXXXXXl',
        'pXX XXXXXXkXXXXXXXqXXfXXXXXX ',
        'aXXnXXXeXXXsXXgXXXiXXXfXXXpXXtXXXzXXi',
        'aXXnXXXsXXeXXXlXXXtXXeXXXkXX XXXfXXXiXXf',
        'tXXXXXXXoXXbXXXnXXXiXXuXXXXXXz',
        'fXXvXXXXXX XXXXXXXc',
        'iXXcXXXXXX?',
        'iXXXrXXXtXXz',
        'fXXhXXXi',
        ' nqXXl',
        'aiicp',
        ' XXcimq'
    ]

    for line in lijnen:
        changed = line.replace('X', '.')
        print(changed)

    while len(lijnen) > 0 and not done:
        restart = False
        for line in lijnen:
            print(f'Matches for line {line}')
            for matcherino in find_matches(text, line):
                print(text)
                print(f'{' '*matcherino}{line}\r\r')

                user_input = input()

                if user_input == 'n':
                    continue
                if user_input == 'f':
                    break

                if user_input == 'a':
                    text = merge_lines(text, line, matcherino)
                    lijnen.remove(line)

                    print(text)
                    restart = True
                    break

                if user_input == 'stop':
                    done = True
                    break

            print('done')
            inp = input()
            if restart:
                break
            if done:
                break
main()

