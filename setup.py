#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "0.4.0"

if sys.argv[-1] == 'publish':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

readme = open('README.rst').read()

def get_requirements(filename):
    f = open(filename).read()
    reqs = [
            # loop through list of requirements
            x.strip() for x in f.splitlines()
                # filter out comments and empty lines
                if not x.strip().startswith('#')
            ]
    return reqs

setup(
    name='sqlalchemy-pretty-sql',
    version=version,
    description="""given a sqlalchemy query, display a well formatted and highlighted sql code.""",
    long_description=readme,
    author='Martín Gaitán',
    author_email='gaitan@gmail.com',
    url='https://github.com/mgaitan/sqlalchemy-pretty-sql',
    include_package_data=True,
    py_modules=['sqlalchemy_pretty_sql'],
    install_requires=get_requirements('requirements.txt'),
    license="BSD",
    zip_safe=False,
    keywords='sqlalchemy-pretty-sql, sqlalchemy, sql, jupyter notebook',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Framework :: Jupyter',
        'Framework :: IPython',
        'Programming Language :: SQL',
    ],

)
