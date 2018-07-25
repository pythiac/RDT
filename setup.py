#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

install_requires = [
    'Click>=6.0',
    'boto3==1.4.7',
    'numpy==1.13.1',
    'pandas==0.22.0',
    'scipy==0.19.1'
]

setup_requires = ['pytest-runner', ]

tests_require = [
    'pytest',
    'coverage>=4.5.1',
    'pytest>=3.4.2',
    'pytest-runner>=2.11.1',
    'tox>=2.9.1'
]

setup(
    author="MIT Data To AI Lab",
    author_email='dailabmit@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="A repository with reversible data transforms",
    extras_require={
        'test': tests_require,
    },
    install_requires=install_requires,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='rdt',
    name='rdt',
    packages=find_packages(include=['rdt', 'rdt.*']),
    python_requires='>=3.5',
    setup_requires=setup_requires,
    test_suite='tests',
    tests_require=tests_require,
    url='https://github.com/HDI-Project/RDT',
    version='0.1.0',
    zip_safe=False,
)