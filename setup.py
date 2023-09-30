import os

from setuptools import find_packages, setup

_ROOT = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(_ROOT, 'README.md')) as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="license-utils",
    version="0.0.1",
    description="Various utilities for working with SPDX / OSS licenses, including a spdx-based license matcher.",
    long_description=LONG_DESCRIPTION,
    author="SPDX",
    url="https://github.com/miweiss/license-utils",
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        "aiohttp>=3.8.5",
        "requests>=2.31.0"
    ],
    extras_require={
        "test": [
            "pytest",  
        ],
        "lint": [
            "black==23.3.0",
            "isort==5.12.0",
            "docstr-coverage==2.2.0",
        ],
    },
    entry_points={'console_scripts': [
        'spdx-license-matcher = spdx_license_matcher.matcher:matcher']},
    keywords='spdx license license-matcher',
)
