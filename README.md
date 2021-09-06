## YATTS - Yet Another Terminal Text Styler

[![PyPI](https://img.shields.io/pypi/v/yatts)](https://pypi.org/project/yatts/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/yatts)](https://pypi.org/project/yatts/)
[![GitHub](https://img.shields.io/github/license/xelorabb/yatts)](https://github.com/xelorabb/yatts/blob/master/LICENSE)

Styles terminal text

#### Install
`pip install yatts`

#### 4-Bit Color Examples
```python
from yatts import style

# Prints yatts with dark green text color
print(style('yatts', ['green', 'dark']))

# Prints yatts with red text color and dark yellow background
print(style('yatts', 'red', ['yellow', 'dark']))

# Prints yatts with white text color, blue background and italic text style
print(style('yatts', bgcolor='blue', italic=True))

# Prints a bold, italic, overlined yatts
print(style('yatts', decorations=['bold', 'italic', 'overline']))
```

#### 8-Bit Color Examples
```python
from yatts import style

yatts = ' yatts '*10

# Dark green text color
print(style(yatts, 2) + '\n')

# Light red text color with light orange background color
print(style(yatts, 196, 223) + '\n')

# 4-Bit and 8-Bit colors mixed and bold parameter
# combined with decorations parameter
print(style(yatts, 'white', 238, bold=True,
            decorations=['underline','overline']))

```
![8bit examples](https://raw.githubusercontent.com/xelorabb/yatts/master/img/8bit_examples.png)

#### Function Arguments
```python
def style(
  text,
  color=None,
  bgcolor=None,
  bold=False,
  italic=False,
  underline=False,
  striketrough=False,
  decorations=None
):
```
**All valid strings for `decorations`:**
* `'bold'`
* `'blink'`
* `'italic'`
* `'overline'`
* `'underline'`
* `'striketrough'`
* `'double_underline'`

#### 4-Bit Color Palette
![4bit color palette](https://raw.githubusercontent.com/xelorabb/yatts/master/img/4bit_color_palette.png)

#### 8-Bit Color Palette
![8bit color palette](https://raw.githubusercontent.com/xelorabb/yatts/master/img/8bit_color_palette.png)
