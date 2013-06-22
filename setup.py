#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fadiga

import setuptools

setuptools.setup(
    name='zerin',
    version="V.0.1",
    license='GNU Lesser General Public License (LGPL), Version 3',

    install_requires=['pysqlite', 'desub'],
    provides=['zerin'],
    autor="Fadiga",
    description='Gestion zerin G.U.I',
    long_description=open('README.rst').read(),

    url='http://github.com/yeleman/zerin',

    packages=['zerin'],

    classifiers=[
        'License :: OSI Approved :: GNU Library or '
        'Lesser General Public License (LGPL)',
        'Programming Language :: Python',
    ],
)
