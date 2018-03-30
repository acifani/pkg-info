import io
from setuptools import setup


with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='pkg-info',
    version='0.1.1',
    url='https://github.com/acifani/pkg-info',
    license='BSD',
    author='Alessandro Cifani',
    author_email='alessandro.cifani@gmail.com',
    description='Tiny library to fetch package info from PyPI.',
    long_description=readme,
    py_modules=["pkg_info"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python'
    ]
)
