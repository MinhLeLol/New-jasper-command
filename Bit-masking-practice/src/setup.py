from setuptools import setup, Extension

module = Extension(
    'bitbox',  #Name of the python module
    sources=['bit_manipulation.c'] # C source file
)

setup(
    name='bitbox',
    version='1.0', #First stable release
    description='Bit manipulation functions to print binary',
    ext_modules=[module]
)