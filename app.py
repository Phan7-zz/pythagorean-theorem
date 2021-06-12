def get_values():
    print('Digite os valores que você sabe, o lado que você não souber, digite "X"')
    values = []
    letter = False
    for a in ('Cateto 1: ', 'Cateto 2: ', 'Hipotenusa: '):
        while True:
            b = input(a)
            if b.isnumeric():
                values.append(float(b))
                break
            elif b.lower() == 'x' and letter is False:
                values.append(b)
                letter = True
                break
            else:
                print(f'Digite um valor válido!')
    
    return values

def calc(values):
    c_1 = values[0]
    c_2 = values[1]
    h = values[2]

    letter = values.index('x')

    if letter == 0:
        a = h ** 2 - c_2 ** 2
        b = f'O valor do cateto 1 é: {a ** 0.5}'
        return b

    elif letter == 1:
        a = h ** 2 - c_1 ** 2
        b = f'O valor do Cateto 2 é: {a ** 0.5}'
        return b
    
    elif letter == 2:
        a = c_1 ** 2 + c_2 ** 2
        b = f'O valor da Hipotenusa é: {a ** 0.5}'
        return b

values = get_values()
result = calc(values)
print(result)
    