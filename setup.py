#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = ""
history = ""


requirements = [
    "selenium",
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='citadel',
    version='0.2.0',
    description="Crawl",
    long_description=readme + '\n\n' + history,
    author="Minho Ryang",
    author_email='minhoryang@gmail.com',
    url='https://github.com/minhoryang/citadel',
    packages=[
        'citadel',
    ],
    package_dir={'citadel':
                 'citadel'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=True,
    keywords='citadel',
    classifiers=[
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
