#!/usr/bin/env python3

from setuptools import setup, find_packages

with open('requiremenst.txt')as f:
    requirements = f.read().splitlines()
    
version = '0.4'

setup = (
    name = 'Pybot',
    version = version, 
    install_requirements = requirements,
    Author = 'Spcktr',
    packages = find_packages(),
    include_package_data = True,
    url = 'https://github.com/Spcktr/PyBot/',
    license = 'GPLv3.0',
    description = 'Gives your discord server a simple multifunction bot'
    )
