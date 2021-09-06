#!/usr/bin/env python

# color, color dark, bgcolor, bgcolor dark
COLORS = {
    'white': ['97', '97', '107', '107'],
    'black': ['30', '30', '40', '40'],
    'gray': ['37', '90', '47', '100'],
    'red': ['91', '31', '101', '41'],
    'green': ['92', '32', '102', '42'],
    'yellow': ['93', '33', '103', '43'],
    'blue': ['94', '34', '104', '44'],
    'magenta': ['95', '35', '105', '45'],
    'cyan': ['96', '36', '106', '46']
}

END = '0'
DECORATIONS = {
    'bold': '1',
    'italic': '3',
    'underline': '4',
    'blink': '5',
    'striketrough': '9',
    'double_underline': '21',
    'overline': '53'
}

def style(text, color=None, bgcolor=None,
        bold=False, italic=False, underline=False, striketrough=False,
        decorations=None):

    codes = []

    # Append color code
    codes.append(get_color_code(color))

    # Append bgcolor code
    codes.append(get_color_code(bgcolor, True))

    #Combine decorations parameter with standard parameters
    std_deco = list(filter(None,[
        'bold' if bold else None,
        'italic' if italic else None,
        'underline' if underline else None,
        'striketrough' if striketrough else None
    ]))

    if not decorations == None:
        if type(decorations) is str:
            decorations = [decorations]

        decorations += std_deco
        decorations = list(set(decorations))

    elif not len(std_deco) == 0:
        decorations = std_deco

    # Append decorations codes
    if not decorations == None:
        if type(decorations) is str:
            if decorations in DECORATIONS:
                codes.append(DECORATIONS[decorations])

        elif type(decorations) is list:
            for deco in decorations:
                if deco in DECORATIONS:
                    codes.append(DECORATIONS[deco])

    # Create output string
    res = None
    code_list = ';'.join(filter(None,codes))

    if not code_list == '':
        res = '\033[' + code_list + 'm' + text + '\033[0m'
    else:
        res = text

    return res

def get_color_code(color, isbgcolor=False):
    code = None

    if not color == None:
        if _is_numeric(color):
            code = _get_8bit_color_code(color, isbgcolor)
        else:
            code = _get_4bit_color_code(color, isbgcolor)

    return code

def _get_4bit_color_code(color, isbgcolor=False):
    c = None

    if type(color) is str and color in COLORS:
        c = COLORS[color][2 if isbgcolor else 0]

    elif type(color) is list:
        if len(color) == 1 and color[0] in COLORS:
            c = COLORS[color[0]][2 if isbgcolor else 0]
        elif len(color) >= 2 and color[0] in COLORS:
            if type(color[1]) is str and color[1] == 'dark':
                c = COLORS[color[0]][3 if isbgcolor else 1]
            else:
                c = COLORS[color[0]][2 if isbgcolor else 0]

    return c

def _get_8bit_color_code(color, isbgcolor=False):
    c = None

    if color >= 0 and color <= 255:
        c = ('48' if isbgcolor else '38') + ';5;' + str(int(color))

    return c

def _is_numeric(c):
    return isinstance(c, (int, float)) and not isinstance(c, bool)
