from setuptools import setup


def text(filename):
    with open(filename) as f:
        return f.read()


setup(name='wordcount',
      version='0.1',
      description='Count all the words!',
      long_description=text('README.rst'),
      author='Henrique Bastos',
      author_email='henrique@bastos.net',
      url='https://github.com/henriquebastos/wordcount',
      license='MIT',
      packages=[
          'wordcount',
      ],
      install_requires=text('requirements.txt').split('\n'),
      entry_points={
          'console_scripts': [
              'wordcount = wordcount.__main__',
          ]
      },
      include_package_data=True,
      zip_safe=False,
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Topic :: Utilities',
      ])
