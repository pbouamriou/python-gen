# CI/CD Setup Documentation

## Overview
This project uses GitHub Actions for continuous integration and deployment, ensuring code quality and automated testing across multiple Python versions.

## Workflows

### 1. CI Workflow (`ci.yml`)
**Triggers:** Push to main/develop, Pull requests to main

**Features:**
- **Multi-Python Testing**: Tests on Python 3.9, 3.10, 3.11, 3.12, 3.13
- **Code Quality Checks**: Linting with Ruff, type checking with MyPy
- **Test Coverage**: Generates coverage reports with pytest-cov
- **Caching**: Optimized dependency caching for faster builds
- **Artifacts**: Builds wheel packages on main branch

**Matrix Strategy:**
```yaml
strategy:
  matrix:
    python-version: ["3.9", "3.10", "3.11", "3.12", "3.13"]
```

### 2. Release Workflow (`release.yml`)
**Triggers:** Push of version tags (v*)

**Features:**
- **Automated PyPI Publishing**: Publishes packages to PyPI
- **Version Management**: Uses semantic versioning with tags
- **Security**: Uses GitHub secrets for PyPI credentials

**Usage:**
```bash
git tag v1.0.0
git push origin v1.0.0
```

### 3. Security Workflow (`security.yml`)
**Triggers:** Weekly schedule, push to main, pull requests

**Features:**
- **Bandit Security**: Static analysis for security vulnerabilities
- **Safety Checks**: Dependency vulnerability scanning
- **Scheduled Runs**: Weekly automated security audits
- **Report Generation**: JSON reports for analysis

### 4. Performance Workflow (`performance.yml`)
**Triggers:** Push to main, pull requests

**Features:**
- **Benchmark Testing**: Performance regression detection
- **pytest-benchmark**: Automated performance testing
- **Result Storage**: Benchmark artifacts for comparison

## Configuration Files

### Dependabot (`dependabot.yml`)
- **Weekly Updates**: Automatically updates dependencies
- **Python & Actions**: Monitors both pip and GitHub Actions
- **Review Process**: Assigns reviewers for manual approval

### Cache Strategy
```yaml
- name: Cache pip dependencies
  uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ matrix.python-version }}-${{ hashFiles('**/pyproject.toml') }}
```

## Environment Variables

### Required Secrets
- `PYPI_API_TOKEN`: PyPI authentication token for releases

### Setup Instructions
1. Go to GitHub repository settings
2. Navigate to Secrets and variables → Actions
3. Add `PYPI_API_TOKEN` with your PyPI token

## Local Development

### Pre-commit Checks
Before pushing, run local checks:
```bash
make check-all  # Linting + type checking
make test       # Run tests
make wheel      # Build wheel
```

### CI Simulation
To simulate CI locally:
```bash
# Install CI dependencies
pip install -e ".[dev]" build

# Run CI steps
python -m ruff check src/ main.py
PYTHONPATH=src python -m mypy main.py
python -m pytest tests/ -v --cov=src/python_gen
python -m build --wheel
```

## Badges

Add these badges to your README:
```markdown
[![CI](https://github.com/username/repo/actions/workflows/ci.yml/badge.svg)](https://github.com/username/repo/actions/workflows/ci.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
```

## Troubleshooting

### Common Issues

1. **Cache Misses**
   - Clear cache by updating pyproject.toml
   - Check cache key configuration

2. **Type Checking Failures**
   - Ensure PYTHONPATH is set correctly
   - Check mypy configuration in pyproject.toml

3. **Test Failures**
   - Run tests locally first
   - Check Python version compatibility

4. **Build Failures**
   - Verify build dependencies
   - Check wheel compatibility

### Debugging
- Check GitHub Actions logs for detailed error messages
- Use `actions/upload-artifact` to preserve build artifacts
- Enable debug logging in workflows if needed

## Best Practices

1. **Branch Protection**: Enable branch protection on main
2. **Required Checks**: Make CI checks required for merging
3. **Review Process**: Require code reviews for pull requests
4. **Semantic Versioning**: Use proper version tags for releases
5. **Security Scanning**: Regular security audits with automated tools

## Performance Optimization

1. **Caching**: Efficient dependency caching
2. **Parallel Jobs**: Matrix strategy for parallel testing
3. **Artifact Management**: Proper artifact cleanup
4. **Resource Usage**: Optimize runner resource usage

## Monitoring

- **Workflow Status**: Monitor workflow success rates
- **Build Times**: Track build performance over time
- **Coverage Trends**: Monitor test coverage changes
- **Security Alerts**: Regular security vulnerability reports 