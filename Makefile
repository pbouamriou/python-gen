.PHONY: help install install-dev clean build wheel test lint type-check format check-all run

# Variables
PYTHON := python3
PACKAGE_NAME := python-gen
VERSION := 0.1.0

help: ## Affiche l'aide
	@echo "Commandes disponibles:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Installe le package en mode développement
	$(PYTHON) -m pip install -e .

install-dev: ## Installe le package avec les dépendances de développement
	$(PYTHON) -m pip install -e ".[dev]"

clean: ## Nettoie les fichiers de build
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean ## Construit le package
	$(PYTHON) -m build

wheel: clean ## Construit le wheel
	$(PYTHON) -m build --wheel

test: ## Lance les tests avec pytest
	$(PYTHON) -m pytest tests/ -v --cov=src/python_gen --cov-report=term-missing

lint: ## Lance ruff pour vérifier le style de code
	$(PYTHON) -m ruff check src/ main.py

type-check: ## Lance mypy pour vérifier les types
	PYTHONPATH=src $(PYTHON) -m mypy main.py

format: ## Formate le code avec ruff
	$(PYTHON) -m ruff format src/ main.py

check-all: lint type-check ## Lance toutes les vérifications (lint + type-check)

run: ## Lance le programme principal
	PYTHONPATH=src $(PYTHON) main.py

dev-setup: install-dev ## Configure l'environnement de développement complet
	@echo "✅ Environnement de développement configuré!"

build-and-test: build test ## Construit le package et lance les tests

# Commande par défaut
.DEFAULT_GOAL := help 