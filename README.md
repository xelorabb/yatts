## YATTS - Yet Another Terminal Text Styler

![PyPI](https://img.shields.io/pypi/v/yatts)
![PyPI - Downloads](https://img.shields.io/pypi/dm/yatts)
![GitHub](https://img.shields.io/github/license/xelorabb/yatts)

Styles terminal text

#### Examples
```python
# Prints yatts with dark green text color
print(style("yatts", ['green', 'dark']))

# Prints yatts with red text color and dark yellow background
print(style("yatts", 'red', ['yellow', 'dark']))

# Prints yatts with white text color, blue background and italic text style
print(style("yatts", bgcolor='blue', italic=True))
```

#### Function Arguments
```python
def style(
  text,
  color='white',
  bgcolor=None,
  bold=False,
  italic=False,
  underline=False,
  striketrough=False
):
```
#### Color Palette
![color palette](https://raw.githubusercontent.com/xelorabb/yatts/master/color_palette.png)
