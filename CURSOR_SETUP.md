# Cursor Setup for python-gen

## 🎯 Overview

This project is now fully configured for Cursor with automatic formatting, linting, and type checking.

## 📁 Configuration Files Created

### `.vscode/settings.json`
Main editor configuration:
- **Auto-formatting**: Ruff automatically formats on save
- **Import organization**: Automatic import sorting
- **Type checking**: Mypy checks types in real-time
- **Linting**: Ruff detects style errors
- **Python environment**: Uses virtual environment `venv/`
- **PYTHONPATH**: Configured to `src/` for imports

### `.vscode/extensions.json`
Recommended extensions:
- `ms-python.python`: Complete Python support
- `charliermarsh.ruff`: Fast linting and formatting
- `ms-python.mypy-type-checker`: Type verification
- `ms-python.pylance`: Advanced IntelliSense
- `ms-python.pytest-adapter`: Test execution

### `.vscode/tasks.json`
Available automated tasks:
- **Run Main**: Launches the main program
- **Run Tests**: Launches unit tests
- **Type Check**: Mypy verification
- **Lint**: Ruff verification
- **Format**: Code formatting
- **Check All**: Complete verifications
- **Build Wheel**: Wheel construction
- **Clean**: File cleanup

### `.vscode/launch.json`
Debug configurations:
- **Python: Main**: Debug `main.py`
- **Python: Current File**: Debug current file
- **Python: Pytest**: Debug tests

### `.vscode/keybindings.json`
Custom keyboard shortcuts:
- `Ctrl+Shift+R`: Launch main program
- `Ctrl+Shift+T`: Launch tests
- `Ctrl+Shift+C`: Complete verifications
- `Ctrl+Shift+F`: Format code
- `Ctrl+Shift+B`: Build wheel
- `Ctrl+Shift+L`: Linting
- `Ctrl+Shift+Y`: Type checking

### `.cursorrules`
Specific rules for Cursor:
- Project context
- Development rules
- Generic types examples
- Best practices

## 🚀 Automatic Features

### Auto-formatting
- **Format on save**: Code is automatically formatted with Ruff
- **Import organization**: Imports are automatically sorted
- **Auto-fix**: Ruff automatically fixes simple errors

### Type checking
- **Real-time verification**: Mypy checks types during editing
- **Visual errors**: Type errors are displayed in the editor
- **IntelliSense**: Type suggestions based on annotations

### Linting
- **Error detection**: Ruff detects style and quality issues
- **Suggestions**: Code improvement proposals
- **Custom rules**: Strict configuration for code quality

## 🛠️ Usage

### First use
1. Open the project in Cursor
2. Install recommended extensions (automatically suggested)
3. Activate virtual environment: `source venv/bin/activate`
4. The project is ready!

### Daily workflow
1. **Edit code**: Auto-formatting applies on save
2. **Check types**: `Ctrl+Shift+Y` or Tasks menu
3. **Run tests**: `Ctrl+Shift+T` or Tasks menu
4. **Complete verifications**: `Ctrl+Shift+C` before commit

### Quick commands
- **Terminal → Run Task**: Access to all Makefile commands
- **F5**: Debug main program
- **Ctrl+Shift+P**: Command palette

## 🔧 Customization

### Modify shortcuts
Edit `.vscode/keybindings.json` to customize keyboard shortcuts.

### Add tasks
Edit `.vscode/tasks.json` to add new automated tasks.

### Configure environment
Modify `.vscode/settings.json` to adjust editor settings.

## 🐛 Troubleshooting

### Auto-formatting issues
1. Check that Ruff extension is installed
2. Check that virtual environment is activated
3. Restart Cursor if necessary

### Type checking issues
1. Check that mypy is installed: `pip install mypy`
2. Check configuration in `pyproject.toml`
3. Check that PYTHONPATH is correct

### Import issues
1. Check that PYTHONPATH points to `src/`
2. Check that virtual environment is activated
3. Restart Python server: `Ctrl+Shift+P` → "Python: Restart Language Server"

## ✅ Verification

To verify everything is working:

```bash
# In Cursor terminal
source venv/bin/activate
make check-all
```

All tests should pass and no type or style errors should be detected. 