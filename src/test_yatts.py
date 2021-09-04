from yatts import style

def test_style_color_red():
    assert style('yatts', 'red') == '\33[91myatts\33[0m'

def test_style_color_dark_magenta():
    assert style('yatts', ['magenta', 'dark']) == '\33[35myatts\33[0m'

def test_style_color_list_without_second_entry():
    assert style('yatts', ['yellow']) == '\33[93myatts\33[0m'

def test_style_color_list_empty():
    assert style('yatts', []) == 'yatts'

def test_style_color_list_empty_and_bgcolor_list_without_second_entry():
    assert style('yatts', [], ['green']) == '\33[102myatts\33[0m'

def test_style_color_and_bgcolor_list_empty():
    assert style('yatts', [], []) == 'yatts'

def test_style_bgcolor_dark_gray():
    assert style('yatts', bgcolor=['gray', 'dark']) == '\33[97;100myatts\33[0m'

def test_style_bold_italic():
    assert style('yatts', bold=True, italic=True) == '\33[1;3;97myatts\33[0m'

def test_style_underline():
    assert style('yatts', underline=True) == '\33[4;97myatts\33[0m'

def test_style_striketrough():
    assert style('yatts', striketrough=True) == '\33[9;97myatts\33[0m'
