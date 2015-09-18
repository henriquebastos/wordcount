#from distutils.core import setup
from setuptools import setup


setup(
    name='wordcount',
    version='0.1',
    packages=['wordcount'],
    url='',
    license='MIT',
    author='Henrique Bastos e Galera',
    author_email='henrique@bastos.net',
    description='Conta as palavras',
    entry_points={
        'console_scripts': ['wordcount=wordcount.__main__:main'],
    },
)
