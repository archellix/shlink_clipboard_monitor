.DEFAULT_GOAL := build

APPLICATION=nda-clip-detector
BIN=venv/bin/

venv:
	virtualenv venv

build:
	$(BIN)pip install -e .
	$(BIN)python setup.py py2app