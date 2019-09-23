from setuptools import setup
import os

try:
   import pypandoc
   long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   long_description = open('README.md').read()

setup(name='MrMap',
      version='0.0.1',
      description = 'Extract Countries, Regions and Cities from a string',
      long_description = long_description,
      url='https://github.com/dhamodharanrk/MrMap',
      download_url ='https://github.com/dhamodharanrk/MrMap',
      author='Dhamodharan',
      author_email='dhamodharanrk@gmail.com',
      license='MIT',
      packages=['MrMap'],
      install_requires=[
            'numpy',
            'nltk',
            'newspaper3k',
            'jellyfish',
            'pycountry'
      ],
      scripts=['geograpy/bin/geograpy-nltk'],
      package_data = {
            'MrMap': ['data/*.csv'],
      },
      zip_safe=False)