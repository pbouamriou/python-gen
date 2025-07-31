# Guide d'installation

## Prérequis

- Python 3.9 ou supérieur
- pip

## Installation rapide

1. **Cloner le repository**

   ```bash
   git clone <repository-url>
   cd python-generique
   ```

2. **Créer un environnement virtuel**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Sur macOS/Linux
   # ou
   venv\Scripts\activate     # Sur Windows
   ```

3. **Installer les dépendances de développement**
   ```bash
   make install-dev
   ```

## Installation manuelle

Si vous préférez une installation manuelle :

```bash
# Créer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -e ".[dev]"
pip install build
```

## Vérification de l'installation

Après l'installation, vous pouvez vérifier que tout fonctionne :

```bash
# Lancer le programme principal
make run

# Vérifier le code (lint + type-check)
make check-all

# Lancer les tests
make test

# Construire le wheel
make wheel
```

## Structure du projet

```
python-generique/
├── src/
│   └── python_gen/          # Package principal
│       ├── __init__.py
│       └── generics.py      # Types génériques
├── tests/                   # Tests unitaires
├── main.py                  # Point d'entrée
├── pyproject.toml          # Configuration du projet
├── Makefile                # Commandes automatisées
├── README.md               # Documentation
└── venv/                   # Environnement virtuel
```

## Commandes disponibles

Utilisez `make help` pour voir toutes les commandes disponibles :

- `make run` : Lance le programme principal
- `make test` : Lance les tests unitaires
- `make lint` : Vérifie le style de code
- `make type-check` : Vérifie les types
- `make check-all` : Lance toutes les vérifications
- `make format` : Formate le code
- `make wheel` : Construit le wheel
- `make clean` : Nettoie les fichiers de build

## Dépannage

### Erreur "externally-managed-environment"

Si vous obtenez cette erreur lors de l'installation, utilisez un environnement virtuel :

```bash
python3 -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
```

### Erreur de module non trouvé

Assurez-vous que l'environnement virtuel est activé et que le PYTHONPATH est correctement configuré pour les commandes `make run` et `make type-check`.

### Problèmes de type checking

Si mypy ne trouve pas les modules, vérifiez que le PYTHONPATH est correctement configuré dans le Makefile.
