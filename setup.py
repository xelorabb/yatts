from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

NAME = 'yatts'
VERSION = '1.0.0'
INSTALL_REQUIRES = []
DESCRIPTION = 'Styles terminal text'
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'
KEYWORDS = ['python', 'color', 'text', 'style', 'terminal', 'console']
CLASSIFIERS = [
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3.9",
    "Operating System :: OS Independent",
]

PY_MODULES = ['yatts']
PACKAGE_DIR = {'': 'src'}

AUTHOR = 'xelorabb'
EMAIL = 'xelorabb@gmail.com'
URL = 'https://github.com/xelorabb/yatts'
LICENSE = 'MIT'

# Setting up
setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    install_requires=INSTALL_REQUIRES,
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    py_modules=PY_MODULES,
    package_dir=PACKAGE_DIR,
    license=LICENSE
)
