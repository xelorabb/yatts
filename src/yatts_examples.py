from yatts import style

def print_8bit_palette():
    print('\n### 8-Bit Palette')
    _8bit = ''

    for i, n in enumerate(range(0,255)):
        _8bit += '\n' if i % 16 == 0 else ''
        _8bit += style(' ' + str(n) + ' ', 236, bgcolor=n)

    print(_8bit)
    print('')

def print_8bit_gray_scale():
    print('\n### 8-Bit Gray Scale\n')
    gray_scale = ''
    for i, n in enumerate(range(232,256)):
        gray_scale += style(' ~ ', 255-i, n)

    print(gray_scale)

def print_8bit_examples():
    yatts = ' yatts '*10

    print(style(yatts, 2) + '\n')
    print(style(yatts, 196, 223) + '\n')
    print(style(yatts, 'white', 238, bold=True,
                decorations=['underline','overline']))

if __name__ == '__main__':
    print_8bit_examples()
    print_8bit_palette()
    print_8bit_gray_scale()
