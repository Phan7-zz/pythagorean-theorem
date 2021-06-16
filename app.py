# To make this code works, you have to give just two values of the triangle
# The value that you don't know, you have to input "x"

def get_values():
    print('Input the values that you know. If you do not know a velue, input"x"')
    values = []
    letter = False
    for a in ('Side 1: ', 'Side 2: ', 'hypotenuse: '):
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
                print('Input a valid value!')
    
    return values

def calc(values):
    c_1 = values[0]
    c_2 = values[1]
    h = values[2]

    letter = values.index('x')

    if letter == 0:
        a = h ** 2 - c_2 ** 2
        b = f'The value of the Side 1 is: {a ** 0.5}'
        return b

    elif letter == 1:
        a = h ** 2 - c_1 ** 2
        b = f'The value of the Side 2 is: {a ** 0.5}'
        return b
    
    elif letter == 2:
        a = c_1 ** 2 + c_2 ** 2
        b = f'The value the Hypotenuse is: {a ** 0.5}'
        return b

values = get_values()
result = calc(values)
print(result)
    
