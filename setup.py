import os

from setuptools import setup

PACKAGE_DIR = 'unimoddb'


# Extract README.md
readme = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md')
with open(readme, encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='unimoddb',
    version='0.1.0',
    packages=[
        'unimoddb',
    ],
    license='MIT',
    description=(
        'A library for SQLite access to the Unimod modification database'
    ),
    author='Daniel Spencer',
    author_email='danielspencer305@hotmail.co.uk',
    url='https://github.com/ikcgroup/unimoddb',
    keywords=[
        'UNIMOD',
        'PROTEOMICS'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    long_description_content_type='text/markdown',
    long_description=long_description,
)
