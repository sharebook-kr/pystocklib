from setuptools import setup

setup(
    name            = 'pystocklib',
    version         = '0.0.1',
    description     = 'python stock library',
    url             = 'https://github.com/sharebook-kr/pystocklib',
    author          = 'Lukas Yoo, Brayden Jo',
    author_email    = 'jonghun.yoo@outlook.com, brayden.jo@outlook.com, pystock@outlook.com',
    install_requires= ['pandas', 'requests'],
    license         = 'MIT',
    packages        = ['pystocklib'],
    zip_safe        = False
)