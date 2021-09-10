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

# Styles a text
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
    return _create_output_string(text, codes)

# Adds a specific style to a text
def add(text, style, value=None):
    start, end = _check_escape_sequence(text)
    codes = []

    if not start or not end:
        text = '\033[m' + remove_all(text) + '\033[0m'
        start = True; end = True

    if start and end:
        codes = _get_all_style_codes(text, codes)

        if type(style) is str:
            codes = _add_style_code(style, value, codes)

    return _create_output_string(text, codes)

# Removes one or more specific style from a styled text
def remove(text, style):
    start, end = _check_escape_sequence(text)
    codes = []

    if start and end:
        codes = _get_all_style_codes(text, codes)

        if type(style) is str:
            codes = _remove_style_codes(style, codes)
        elif type(style) is list:
            for s in style:
                codes = _remove_style_codes(s, codes)

    return _create_output_string(text, codes)

# Removes all styles from a styled text
def remove_all(text):
    start, end = _check_escape_sequence(text)

    if start:
        text = text[text.find('m')+1:]

    if end:
        text = text[:-4]

    return text

# Returns 4-Bit or 8-Bit color or bgcolor code
def get_color_code(color, isbgcolor=False):
    code = None

    if not color == None:
        if _is_numeric(color):
            code = _get_8bit_color_code(color, isbgcolor)
        else:
            code = _get_4bit_color_code(color, isbgcolor)

    return code

# Creates the full styled output string
def _create_output_string(text, codes):
    res = None
    code_list = ';'.join(filter(None,codes))

    if not code_list == '':
        res = '\033[' + code_list + 'm' + remove_all(text) + '\033[0m'
    else:
        res = remove_all(text)

    return res

# Return 4-Bit color or bgcolor code
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

# Return 8-Bit color or bgcolor code
def _get_8bit_color_code(color, isbgcolor=False):
    c = None

    if color >= 0 and color <= 255:
        c = ('48' if isbgcolor else '38') + ';5;' + str(int(color))

    return c

# Combines the 8-Bit color or bgcolor values to one string
def _combine_8bit_color_to_str(codes, n):
    if n in codes:
        n = codes.index(n)
        temp = ';'.join(codes[n:n+3])
        del codes[n:n+3]
        codes.append(temp)

    return codes

# Finds color or bgcolor code in code list
def _find_color_code(codes, isbgcolor=False):
    color_range = list(range(30,38)) + list(range(90,98))
    color_code_8bit = '38'

    if isbgcolor:
        color_range = list(range(40,48)) + list(range(100,108))
        color_code_8bit = '48'

    color_code = [x for x in codes if x.startswith(color_code_8bit)]

    return color_code, color_range

# Returns all style codes in a list
def _get_all_style_codes(text, codes):
    m = text.find('m')
    codes = text[2:m].split(';')
    codes = _combine_8bit_color_to_str(codes, '38')
    codes = _combine_8bit_color_to_str(codes, '48')

    return codes

# Removes any style from code list
def _remove_style_codes(style, codes):
    if style in DECORATIONS and DECORATIONS[style] in codes:
        codes.remove(DECORATIONS[style])
    elif style == 'color':
        codes = _remove_color_codes(codes)
    elif style == 'bgcolor':
        codes = _remove_color_codes(codes, True)

    return codes

# Removes 4-Bit or 8-Bit color or bgcolor from code list
def _remove_color_codes(codes, isbgcolor=False):
    color_code, color_range = _find_color_code(codes, isbgcolor)

    if not color_code == []:
        codes.remove(''.join(color_code))
    else:
        dup = map(str, codes + color_range)
        seen = set()
        uniq = [x for x in dup if x in seen or seen.add(x)]
        codes = [x for x in codes if x not in uniq]

    return codes

# Adds any style to code list
def _add_style_code(style, value, codes):
    if style in DECORATIONS and not DECORATIONS[style] in codes:
        codes.append(DECORATIONS[style])
    elif style == 'color':
        codes = _update_color_code(codes, value)
    elif style == 'bgcolor':
        codes = _update_color_code(codes, value, True)

    return codes

# Adds or updates 4-Bit or 8-Bit color or bgcolor to code list
def _update_color_code(codes, value, isbgcolor=False):
    color_code = _find_color_code(codes, isbgcolor)

    if not color_code == []:
        codes = _remove_color_codes(codes, isbgcolor)
        codes.append(get_color_code(value, isbgcolor))
    else:
        codes = _remove_color_codes(codes, isbgcolor)
        codes.append(get_color_code(value, isbgcolor))

    return codes

# Checks if parameter c is numeric
def _is_numeric(c):
    return isinstance(c, (int, float)) and not isinstance(c, bool)

# Checks if the text parameter starts and ends with a escape sequence
def _check_escape_sequence(text):
    return text.startswith('\33['), text.endswith('\33[0m')
