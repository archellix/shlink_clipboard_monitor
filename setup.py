import os, io, sys

from setuptools import find_packages, setup

NAME="ClipboardDetector"
DESCRIPTION="NOPE"
AUTHOR="Arrr"
AUTHOR_EMAIL="arrr@test.ru"
REQUIRES_PYTHON=">=3.10.0"
VERSION="0.1.3"
MAINSCRIPT = 'nda_clip_detector/service.py'

pwd=os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(pwd, "README.md"), encoding="utf-8") as f:
        L_DESCIRPTION= "\n" + f.read()
except FileNotFoundError:
    L_DESCIRPTION=DESCRIPTION

if sys.platform == 'darwin':
    extra_options = dict(
        setup_requires=['py2app'],
        app=[MAINSCRIPT],
        options=dict(py2app=dict(
            argv_emulation=True,
            resources=["./nda_clip_detector/config.yaml"]
        )),
    )
elif sys.platform == 'win32':
    extra_options = dict(
        setup_requires=['py2exe'],
        app=[MAINSCRIPT],
    )
else:
    extra_options = dict(
        scripts=[MAINSCRIPT],
    )

setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=L_DESCIRPTION,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url="my secret site",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    include_package_data=True,
    **extra_options
)