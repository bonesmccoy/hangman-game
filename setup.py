from setuptools import setup
from setuptools import find_packages

setup(name='hangman',
      version='0.1',
      description='CLI Hangman Game',
      author='Daniele Murroni',
      author_email='daniele.murroni@gmail.com',
      packages=find_packages(exclude=['doc', 'tests*']),
      install_requires=[
          'Click',
      ],
      entry_points='''
        [console_scripts]
        hangman=cli:cli
    ''',
      )
