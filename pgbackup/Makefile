.PHONY: default

default: tests

install:
    pipenv install --dev --skip-lock

test:
    PYTHONPATH=./src pytest
