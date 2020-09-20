from setuptools import setup

setup(
    name            = 'pystocklib',
    version         = '0.0.3',
    description     = 'python stock library',
    url             = 'https://github.com/sharebook-kr/pystocklib',
    author          = 'Lukas Yoo, Brayden Jo',
    author_email    = 'jonghun.yoo@outlook.com, brayden.jo@outlook.com, pystock@outlook.com',
    install_requires= ['pandas', 'requests', 'beautifulsoup4', 'html5lib'],
    license         = 'MIT',
    packages        = ['pystocklib'],
    zip_safe        = False
)