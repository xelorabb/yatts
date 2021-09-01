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

END             = '0'
BOLD            = '1'
ITALIC          = '3'
UNDERLINE       = '4'
STRIKETROUGH    = '9'

def style(text, color='white', bgcolor=None,
        bold=False, italic=False, underline=False, striketrough=False):

    codes = [
        BOLD if bold else None,
        ITALIC if italic else None,
        UNDERLINE if underline else None,
        STRIKETROUGH if striketrough else None,
        get_color_code(color),
        get_color_code(bgcolor, True) if not bgcolor is None else None
    ]

    return '\033[' + ';'.join(filter(None,codes)) + 'm' + text + '\033[0m'

def get_color_code(color, isbgcolor=False):
    c = None

    if type(color) is str and color in COLORS:
        c = COLORS[color][2 if isbgcolor else 0]

    elif type(color) is list:
        if len(color) >= 2 and color[0] in COLORS:
            if type(color[1]) is str and color[1] == 'dark':
                c = COLORS[color[0]][3 if isbgcolor else 1]
            else:
                c = COLORS[color[0]][2 if isbgcolor else 0]

    return c
