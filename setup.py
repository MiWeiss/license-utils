import os

from setuptools import find_packages, setup

import license_utils

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

_ROOT = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(_ROOT, 'README.md')) as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="license-utils",
    version=license_utils.__version__,
    description="Various utilities for working with SPDX / OSS licenses, including a spdx-based license matcher.",
    long_description=LONG_DESCRIPTION,
    author="SPDX",
    url="https://github.com/miweiss/license-utils",
    packages=find_packages(exclude=['tests*']),
    install_requires=requirements,
    setup_requires=['setuptools>=39.0.1'],
    entry_points={'console_scripts': [
        'spdx-license-matcher = spdx_license_matcher.matcher:matcher']},
    keywords='spdx license license-matcher',
)
