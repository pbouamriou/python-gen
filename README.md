# Python-Gen

Test project for Python generic types with strict type checking configuration.

## 🚀 Features

- **Advanced generic types**: Generic classes and functions with constraints
- **Strict type checking**: Mypy configuration for rigorous type verification
- **Modern linting**: Ruff for formatting and style checking
- **Automated build**: Makefile to simplify development tasks

## 📋 Prerequisites

- Python 3.9 or higher
- pip

## 🛠️ Installation

### Quick installation

```bash
# Clone the repository
git clone <repository-url>
cd python-generique

# Install in development mode
make install-dev
```

### Manual installation

```bash
# Install the package with development dependencies
pip install -e ".[dev]"
```

## 🎯 Usage

### Build the wheel

```bash
make wheel
```

### Check the code

```bash
# Complete verification (lint + type-check)
make check-all

# Style verification only
make lint

# Type verification only
make type-check
```

### Format the code

```bash
make format
```

### Run tests

```bash
make test
```

## 📁 Project Structure

```
python-generique/
├── src/
│   └── python_gen/
│       ├── __init__.py
│       └── generics.py          # Generic types examples
├── pyproject.toml              # Project configuration
├── Makefile                    # Automated commands
└── README.md                   # This file
```

## 🔧 Implemented Generic Types

### Generic Classes

- **`Container[T]`** : Simple container to store a typed value
- **`Pair[T, U]`** : Pair of values with different types
- **`Stack[T]`** : Generic stack with push/pop operations
- **`SortedList[Comparable]`** : Sorted list for comparable types

### Generic Functions

- **`identity(value: T) -> T`** : Generic identity function
- **`swap_pair(pair: Pair[T, U]) -> Pair[U, T]`** : Swap pair elements
- **`merge_containers(container1: Container[T], container2: Container[U]) -> Pair[T, U]`** : Merge containers

### Type Aliases

- **`NumberContainer`** : Alias for `Container[Union[int, float]]`
- **`StringContainer`** : Alias for `Container[str]`

## 🧪 Usage Examples

```python
from src.python_gen.generics import Container, Pair, Stack

# Generic container
int_container = Container(42)
str_container = Container("Hello")

# Generic pair
pair = Pair("key", 123)
swapped = pair.swap()

# Generic stack
stack = Stack[int]()
stack.push(1)
stack.push(2)
value = stack.pop()  # 2
```

## 🔍 Configuration

### Strict Type Checking

The project uses mypy with strict configuration:

- `disallow_untyped_defs = true`
- `disallow_incomplete_defs = true`
- `check_untyped_defs = true`
- `disallow_untyped_decorators = true`
- `no_implicit_optional = true`

### Linting with Ruff

Ruff configuration for:

- Automatic formatting
- Style checking
- Import sorting
- Bug detection

## 📦 Build

To create a distributable wheel:

```bash
make wheel
```

The wheel will be created in the `dist/` folder.

## 🤝 Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🆘 Help

To see all available commands:

```bash
make help
```

## 🚀 CI/CD

### GitHub Actions
The project uses GitHub Actions for continuous integration:

- **Automated tests**: Execution on Python 3.9, 3.10, 3.11, 3.12, 3.13
- **Linting and type checking**: Automatic code verification
- **Code coverage**: Coverage report with Codecov
- **Automatic build**: Wheel construction on main branch
- **Releases**: Automatic publication on PyPI on tags

### Available Workflows
- `ci.yml`: Tests, linting and type checking on all Python versions
- `release.yml`: Automatic publication on PyPI
- `dependabot.yml`: Automatic dependency updates

### Status Badges
[![CI](https://github.com/pbouamriou/python-gen/actions/workflows/ci.yml/badge.svg)](https://github.com/pbouamriou/python-gen/actions/workflows/ci.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Linting: Ruff](https://img.shields.io/badge/linting-ruff-red.svg)](https://github.com/astral-sh/ruff)
[![Type checking: mypy](https://img.shields.io/badge/type%20checking-mypy-blue.svg)](https://mypy-lang.org/)

## 🖥️ Cursor/VS Code Configuration

The project includes a complete configuration for Cursor and VS Code:

### Recommended Extensions
- **Python**: Complete Python support
- **Ruff**: Fast linting and formatting
- **Mypy Type Checker**: Type verification
- **Pylance**: Advanced IntelliSense
- **Pytest**: Test execution

### Automatic Features
- **Auto-formatting**: Ruff automatically formats on save
- **Import organization**: Automatic import sorting
- **Type checking**: Real-time mypy verification
- **Linting**: Error detection with Ruff

### Keyboard Shortcuts
- `Ctrl+Shift+R`: Run the main program
- `Ctrl+Shift+T`: Run tests
- `Ctrl+Shift+C`: Complete verifications
- `Ctrl+Shift+F`: Format code
- `Ctrl+Shift+B`: Build wheel
- `Ctrl+Shift+L`: Linting
- `Ctrl+Shift+Y`: Type checking

### Debug Configuration
Three debug configurations are available:
- **Python: Main**: Debug the main program
- **Python: Current File**: Debug the current file
- **Python: Pytest**: Debug tests

### Available Tasks
All Makefile commands are available in the Tasks menu:
- Terminal → Run Task → [Select task]
