# coding:utf-8

'''
---------------------------PyME(python message encryption)---------------------------
This is a mock java MD5 encryption, python information encryption module.
        Please correct the inadequacies. Thank you.
1.Please enter a string of at least 6 characters and a salt value.
2.The string and salt value must meet the following rules [a-zA-Z0-9].
3.This is the first version and will continue to be updated and optimized.
---------------------------Made in China---------------------------
'''


def me(data, salt):
    lower = {
        'a': 'A0SEC', 'b': 'DA3DA', 'c': 'FA5AD', 'd': 'GD6DS', 'e': 'HD9SS', 'f': 'DA3SA', 'g': 'DA6AS',
        'h': 'FA8DF', 'i': 'DA10A', 'j': 'J0T0D', 'k': 'D172J', 'l': 'DS24F', 'm': 'JH0GT', 'n': 'DAS90',
        'o': 'Y36dE', 'p': 'TR2Qe', 'q': 'JR6dA', 'r': 'FA4gE', 's': 'FaWY2', 't': 'KG6TW',
        'u': 'FA2qA', 'v': 'tA7KG', 'w': 'RE8hE', 'x': 'EWfED', 'y': 'AS2yT', 'z': 'M5GZ1'
    }

    capit = {
        'A': 'ew3EF', 'B': 'UT6sd', 'C': 'ds8KD', 'D': 'j24GS', 'E': 'uyf2K', 'F': '2y6SA', 'G': 'QEW3D',
        'H': 'TeT9K', 'I': 'JT2Cz', 'J': 'SdG6F', 'K': 'DA2DI', 'L': '2IIOe', 'M': 'JG8u7', 'N': 'DA2Sd',
        'O': 'AeCSD', 'P': 'CsGO3', 'Q': '9G2t6', 'R': '1eW8E', 'S': 'L4yIO', 'T': 'TDmYK',
        'U': 'MlK35', 'V': 'War6A', 'W': 'daU9Q', 'X': 'DA0DV', 'Y': 'K7YAS', 'Z': 'R5G0C'
    }

    numbers = {
        '0': 'wsr5H', '1': 'JD67k', '2': 'YMH7s', '3': 'LL9ac', '4': 'ge4i7',
        '5': 'bsd3K', '6': 'saGA0', '7': 'wQeSD', '8': 'GSa2iV', '9': 'SV2Sa',
    }

    lens = 0
    data = list(data)
    len(data)
    for i in data:
        if i == 'a':
            data[lens] = lower.get('a')
            lens += 1
        elif i == 'b':
            data[lens] = lower.get('b')
            lens += 1
        elif i == 'c':
            data[lens] = lower.get('c')
            lens += 1
        elif i == 'd':
            data[lens] = lower.get('d')
            lens += 1
        elif i == 'e':
            data[lens] = lower.get('e')
            lens += 1
        elif i == 'f':
            data[lens] = lower.get('f')
            lens += 1
        elif i == 'g':
            data[lens] = lower.get('g')
            lens += 1
        elif i == 'h':
            data[lens] = lower.get('h')
            lens += 1
        elif i == 'i':
            data[lens] = lower.get('i')
            lens += 1
        elif i == 'j':
            data[lens] = lower.get('j')
            lens += 1
        elif i == 'k':
            data[lens] = lower.get('k')
            lens += 1
        elif i == 'l':
            data[lens] = lower.get('l')
            lens += 1
        elif i == 'm':
            data[lens] = lower.get('m')
            lens += 1
        elif i == 'n':
            data[lens] = lower.get('n')
            lens += 1
        elif i == 'o':
            data[lens] = lower.get('o')
            lens += 1
        elif i == 'p':
            data[lens] = lower.get('p')
            lens += 1
        elif i == 'q':
            data[lens] = lower.get('q')
            lens += 1
        elif i == 'r':
            data[lens] = lower.get('r')
            lens += 1
        elif i == 's':
            data[lens] = lower.get('s')
            lens += 1
        elif i == 't':
            data[lens] = lower.get('t')
            lens += 1
        elif i == 'u':
            data[lens] = lower.get('u')
            lens += 1
        elif i == 'v':
            data[lens] = lower.get('v')
            lens += 1
        elif i == 'w':
            data[lens] = lower.get('w')
            lens += 1
        elif i == 'x':
            data[lens] = lower.get('x')
            lens += 1
        elif i == 'y':
            data[lens] = lower.get('y')
            lens += 1
        elif i == 'z':
            data[lens] = lower.get('z')
            lens += 1
        elif i == 'A':
            data[lens] = capit.get('A')
            lens += 1
        elif i == 'B':
            data[lens] = capit.get('B')
            lens += 1
        elif i == 'C':
            data[lens] = capit.get('C')
            lens += 1
        elif i == 'D':
            data[lens] = capit.get('D')
            lens += 1
        elif i == 'E':
            data[lens] = capit.get('E')
            lens += 1
        elif i == 'F':
            data[lens] = capit.get('F')
            lens += 1
        elif i == 'G':
            data[lens] = capit.get('G')
            lens += 1
        elif i == 'H':
            data[lens] = capit.get('H')
            lens += 1
        elif i == 'I':
            data[lens] = capit.get('I')
            lens += 1
        elif i == 'J':
            data[lens] = capit.get('J')
            lens += 1
        elif i == 'K':
            data[lens] = capit.get('K')
            lens += 1
        elif i == 'L':
            data[lens] = capit.get('L')
            lens += 1
        elif i == 'M':
            data[lens] = capit.get('M')
            lens += 1
        elif i == 'N':
            data[lens] = capit.get('N')
            lens += 1
        elif i == 'O':
            data[lens] = capit.get('O')
            lens += 1
        elif i == 'P':
            data[lens] = capit.get('P')
            lens += 1
        elif i == 'Q':
            data[lens] = capit.get('Q')
            lens += 1
        elif i == 'R':
            data[lens] = capit.get('R')
            lens += 1
        elif i == 'S':
            data[lens] = capit.get('S')
            lens += 1
        elif i == 'T':
            data[lens] = capit.get('T')
            lens += 1
        elif i == 'U':
            data[lens] = capit.get('U')
            lens += 1
        elif i == 'V':
            data[lens] = capit.get('V')
            lens += 1
        elif i == 'W':
            data[lens] = capit.get('W')
            lens += 1
        elif i == 'X':
            data[lens] = capit.get('X')
            lens += 1
        elif i == 'Y':
            data[lens] = capit.get('Y')
            lens += 1
        elif i == 'Z':
            data[lens] = capit.get('Z')
            lens += 1
        elif i == '0':
            data[lens] = numbers.get('0')
            lens += 1
        elif i == '1':
            data[lens] = numbers.get('1')
            lens += 1
        elif i == '2':
            data[lens] = numbers.get('2')
            lens += 1
        elif i == '3':
            data[lens] = numbers.get('3')
            lens += 1
        elif i == '4':
            data[lens] = numbers.get('4')
            lens += 1
        elif i == '5':
            data[lens] = numbers.get('5')
            lens += 1
        elif i == '6':
            data[lens] = numbers.get('6')
            lens += 1
        elif i == '7':
            data[lens] = numbers.get('7')
            lens += 1
        elif i == '8':
            data[lens] = numbers.get('8')
            lens += 1
        elif i == '9':
            data[lens] = numbers.get('9')
            lens += 1

    lens = 0
    salt = list(salt)
    for num in salt:
        if num == 'a':
            salt[lens] = lower.get('a')
            lens += 1
        elif num == 'b':
            salt[lens] = lower.get('b')
            lens += 1
        elif num == 'c':
            salt[lens] = lower.get('c')
            lens += 1
        elif num == 'd':
            salt[lens] = lower.get('d')
            lens += 1 
        elif num == 'e':
            salt[lens] = lower.get('e')
            lens += 1
        elif num == 'f':
            salt[lens] = lower.get('f')
            lens += 1
        elif num == 'g':
            salt[lens] = lower.get('g')
            lens += 1
        elif num == 'h':
            salt[lens] = lower.get('h')
            lens += 1
        elif num == 'i':
            salt[lens] = lower.get('i')
            lens += 1
        elif num == 'j':
            salt[lens] = lower.get('j')
            lens += 1
        elif num == 'k':
            salt[lens] = lower.get('k')
            lens += 1
        elif num == 'l':
            salt[lens] = lower.get('l')
            lens += 1
        elif num == 'm':
            salt[lens] = lower.get('m')
            lens += 1
        elif num == 'n':
            salt[lens] = lower.get('n')
            lens += 1
        elif num == 'o':
            salt[lens] = lower.get('o')
            lens += 1
        elif num == 'p':
            salt[lens] = lower.get('p')
            lens += 1
        elif num == 'q':
            salt[lens] = lower.get('q')
            lens += 1
        elif num == 'r':
            salt[lens] = lower.get('r')
            lens += 1
        elif num == 's':
            salt[lens] = lower.get('s')
            lens += 1
        elif num == 't':
            salt[lens] = lower.get('t')
            lens += 1
        elif num == 'u':
            salt[lens] = lower.get('u')
            lens += 1
        elif num == 'v':
            salt[lens] = lower.get('v')
            lens += 1
        elif num == 'w':
            salt[lens] = lower.get('w')
            lens += 1
        elif num == 'x':
            salt[lens] = lower.get('x')
            lens += 1
        elif num == 'y':
            salt[lens] = lower.get('y')
            lens += 1
        elif num == 'z':
            salt[lens] = lower.get('z')
            lens += 1
        elif num == 'A':
            salt[lens] = capit.get('A')
            lens += 1
        elif num == 'B':
            salt[lens] = capit.get('B')
            lens += 1
        elif num == 'C':
            salt[lens] = capit.get('C')
            lens += 1
        elif num == 'D':
            salt[lens] = capit.get('D')
            lens += 1
        elif num == 'E':
            salt[lens] = capit.get('E')
            lens += 1
        elif num == 'F':
            salt[lens] = capit.get('F')
            lens += 1
        elif num == 'G':
            salt[lens] = capit.get('G')
            lens += 1
        elif num == 'H':
            salt[lens] = capit.get('H')
            lens += 1
        elif num == 'I':
            salt[lens] = capit.get('I')
            lens += 1
        elif num == 'J':
            salt[lens] = capit.get('J')
            lens += 1
        elif num == 'K':
            salt[lens] = capit.get('K')
            lens += 1
        elif num == 'L':
            salt[lens] = capit.get('L')
            lens += 1
        elif num == 'M':
            salt[lens] = capit.get('M')
            lens += 1
        elif num == 'N':
            salt[lens] = capit.get('N')
            lens += 1
        elif num == 'O':
            salt[lens] = capit.get('O')
            lens += 1
        elif num == 'P':
            salt[lens] = capit.get('P')
            lens += 1
        elif num == 'Q':
            salt[lens] = capit.get('Q')
            lens += 1
        elif num == 'R':
            salt[lens] = capit.get('R')
            lens += 1
        elif num == 'S':
            salt[lens] = capit.get('S')
            lens += 1
        elif num == 'T':
            salt[lens] = capit.get('T')
            lens += 1
        elif num == 'U':
            salt[lens] = capit.get('U')
            lens += 1
        elif num == 'V':
            salt[lens] = capit.get('V')
            lens += 1
        elif num == 'W':
            salt[lens] = capit.get('W')
            lens += 1
        elif num == 'X':
            salt[lens] = capit.get('X')
            lens += 1
        elif num == 'Y':
            salt[lens] = capit.get('Y')
            lens += 1
        elif num == 'Z':
            salt[lens] = capit.get('Z')
            lens += 1
        elif num == '0':
            salt[lens] = numbers.get('0')
            lens += 1
        elif num == '1':
            salt[lens] = numbers.get('1')
            lens += 1
        elif num == '2':
            salt[lens] = numbers.get('2')
            lens += 1
        elif num == '3':
            salt[lens] = numbers.get('3')
            lens += 1
        elif num == '4':
            salt[lens] = numbers.get('4')
            lens += 1
        elif num == '5':
            salt[lens] = numbers.get('5')
            lens += 1
        elif num == '6':
            salt[lens] = numbers.get('6')
            lens += 1
        elif num == '7':
            salt[lens] = numbers.get('7')
            lens += 1
        elif num == '8':
            salt[lens] = numbers.get('8')
            lens += 1
        elif num == '9':
            salt[lens] = numbers.get('9')
            lens += 1

    data.insert(5, salt[5])
    data.insert(2, salt[2])
    data.insert(0, salt[0])

    data = ''.join(data)
    return data
