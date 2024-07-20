#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

with open("./README.md", "r", encoding="utf-8") as fp:
    long_description = fp.read()

with open("./LICENSE", "r", encoding="utf-8") as fp:
    license = fp.read()

setup(
    name = "aiop",
	version = "0.0.2",
	license = "MIT Licence",
	author = "Kinda Hall",
	author_email = "1142704468@qq.com",
	packages = find_packages(),
	include_package_data = True,
	platforms = "any",
	install_requires = [],
    keywords=["pip", "tools"],
    description="AI toolset",
    entry_points={
        'console_scripts': [
            'aiop = aiop.main:app'
        ]
    },
    python_requires='>=3.10',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=license,
    url="https://github.com/Alndaly/aiop",
    author="Kinda Hall",
    maintainer="Kinda Hall",
    maintainer_email="1142704468@qq.com",
    author_email="1142704468@qq.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=['typer', 'fastapi', 'zipfile', 'httpx']
)
