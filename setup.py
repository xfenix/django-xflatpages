# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from xflatpages import __version__


# readme
descr = 'Simple flatpages app'

setup(
    name='django-xflatpages',
    version=__version__,
    description=descr,
    long_description=descr,
    author='Xfenix',
    author_email='ad@xfenix.ru',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django-cache-utils',
    ]
)
