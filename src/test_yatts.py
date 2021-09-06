from yatts import style

def test_style_color_red():
    assert style('yatts', 'red') == '\033[91myatts\033[0m'

def test_style_color_dark_magenta():
    assert style('yatts', ['magenta', 'dark']) == '\033[35myatts\033[0m'

def test_style_color_list_without_second_entry():
    assert style('yatts', ['yellow']) == '\033[93myatts\033[0m'

def test_style_color_list_empty():
    assert style('yatts', []) == 'yatts'

def test_style_color_list_empty_and_bgcolor_list_without_second_entry():
    assert style('yatts', [], ['green']) == '\033[102myatts\033[0m'

def test_style_color_and_bgcolor_list_empty():
    assert style('yatts', [], []) == 'yatts'

def test_style_bgcolor_dark_gray():
    assert style('yatts', bgcolor=['gray', 'dark']) == '\033[100myatts\033[0m'

def test_style_bold_italic():
    assert style('yatts', bold=True, italic=True) == '\033[1;3myatts\033[0m'

def test_style_underline():
    assert style('yatts', underline=True) == '\033[4myatts\033[0m'

def test_style_striketrough():
    assert style('yatts', striketrough=True) == '\033[9myatts\033[0m'

def test_style_8bit_dark_green():
    assert style('yatts', 2) == '\033[38;5;2myatts\033[0m'

def test_style_8bit_color_light_red_bgcolor_light_orange():
    assert style('yatts', 196, 223) == '\033[38;5;196;48;5;223myatts\033[0m'

def test_style_decorations_list_empty():
    assert style('yatts', decorations=[]) == 'yatts'
