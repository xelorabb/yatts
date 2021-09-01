from setuptools import setup, find_packages

NAME = 'yatts'
VERSION = '0.0.1'
INSTALL_REQUIRES = []
DESCRIPTION = 'Styles terminal text'
LONG_DESCRIPTION = 'Styles terminal text'
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'
KEYWORDS = ['python', 'color', 'text', 'style', 'terminal', 'console']
CLASSIFIERS = [
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "Operating System :: Unix",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
]

AUTHOR = 'xelorabb'
EMAIL = 'xelorabb@gmail.com'

# Setting up
setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS
)
