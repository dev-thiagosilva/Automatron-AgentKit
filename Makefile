# Makefile for automating common tasks

.PHONY: help install deps test lint format

help:
	@echo "Available targets:" \
	&& echo "  install   - Install dependencies" \
	&& echo "  deps      - Reinstall dependencies" \
	&& echo "  test      - Run unit tests with pytest" \
	&& echo "  lint      - Run flake8 linter" \
	&& echo "  format    - Format code with black"

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

deps: install

# Run tests and generate coverage report
TESTS ?= tests/
PYTHONPATH = src

run-tests:
	pytest $(TESTS) --cov=$(SRC_DIR) --cov-report=term-missing

lint:
	flake8 src tests

format:
	black src tests
