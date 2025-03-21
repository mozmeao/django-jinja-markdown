#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from setuptools import find_packages, setup

base_dir = os.path.dirname(__file__)

with codecs.open(os.path.join(base_dir, "README.rst"), "r", encoding="utf8") as f:
    long_description = f.read()

about = {}
with open(os.path.join(base_dir, "django_jinja_markdown", "__about__.py")) as f:
    exec(f.read(), about)


setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__summary__"],
    long_description=long_description,
    license=about["__license__"],
    url=about["__uri__"],
    author=about["__author__"],
    author_email=about["__email__"],
    platforms=["any"],
    packages=find_packages(exclude=["ez_setup", "tests"]),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "Markdown",
        "django-jinja",
        "markupsafe",
        "jinja2",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Text Processing :: Markup",
    ],
)
