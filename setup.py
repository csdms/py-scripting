#! /usr/bin/env python
from setuptools import setup, find_packages


setup(
    name="py-scripting",
    version="0.2.5",
    description="Python utilities for scripting",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    author="Eric Hutton",
    author_email="huttone@colorado.edu",
    url="http://csdms.colorado.edu",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    install_requires=["six"],
    setup_requires=["setuptools"],
    packages=find_packages(),
)
