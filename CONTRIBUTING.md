# Contributing to Virtual Machine Provisioner

Thank you for your interest in contributing to the Virtual Machine Provisioner! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues

Before creating an issue, please:

1. **Search existing issues** to avoid duplicates
2. **Check the documentation** for solutions
3. **Provide detailed information** including:
   - Operating system and version
   - Python version
   - Vagrant and VirtualBox versions
   - Steps to reproduce
   - Expected vs actual behavior
   - Error messages and logs

### Feature Requests

When requesting features:

1. **Describe the use case** clearly
2. **Explain the benefits** to the community
3. **Consider implementation complexity**
4. **Check if it aligns** with project goals

### Code Contributions

#### Development Setup

1. **Fork the repository**
2. **Clone your fork**:
   ```bash
   git clone https://github.com/yourusername/virtualMachineProvisioner.git
   cd virtualMachineProvisioner
   ```

3. **Set up development environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   python -m pip install -r requirements.txt
   python -m pip install -e .
   ```

4. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

#### Development Guidelines

##### Code Style

- **Follow PEP 8** style guidelines
- **Use meaningful variable names**
- **Add type hints** where appropriate
- **Keep functions focused** and small
- **Add docstrings** for all public functions

##### Testing

- **Write tests** for new features
- **Update existing tests** when modifying code
- **Ensure tests pass** before submitting
- **Test on multiple platforms** when possible

```bash
# Run the test suite
python test_provisioner.py

# Run specific tests
python -c "from test_provisioner import test_imports; test_imports()"
```

##### Documentation

- **Update README.md** for user-facing changes
- **Add docstrings** for new functions
- **Update configuration examples** if needed
- **Include usage examples** for new features

#### Commit Guidelines

Use conventional commit messages:

```
type(scope): description

feat: add new feature
fix: bug fix
docs: documentation changes
style: formatting changes
refactor: code refactoring
test: adding or updating tests
chore: maintenance tasks
```

Examples:
- `feat(cli): add new command for VM backup`
- `fix(config): resolve YAML parsing error`
- `docs(readme): update installation instructions`

#### Pull Request Process

1. **Ensure your code follows** the style guidelines
2. **Add tests** for new functionality
3. **Update documentation** as needed
4. **Test on multiple platforms** (Windows, macOS, Linux)
5. **Update the changelog** if applicable
6. **Submit the pull request** with a clear description

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Test addition/update

## Testing
- [ ] Tests pass locally
- [ ] Tested on Windows
- [ ] Tested on macOS
- [ ] Tested on Linux

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] No breaking changes

## Screenshots (if applicable)
```

## 🏗️ Project Structure

```
virtualMachineProvisioner/
├── main.py                 # CLI entry point
├── provisioner/            # Core package
│   ├── cli.py             # CLI commands
│   ├── vagrant_manager.py # VM management
│   ├── config.py          # Configuration handling
│   └── utils.py           # Utilities
├── examples/              # Configuration examples
├── tests/                 # Test files
└── docs/                  # Documentation
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python test_provisioner.py

# Run specific test modules
python -c "from test_provisioner import test_imports; test_imports()"
```

### Test Coverage

- **Unit tests** for individual functions
- **Integration tests** for CLI commands
- **Configuration tests** for YAML parsing
- **Cross-platform tests** for compatibility

### Adding Tests

When adding new features, include:

1. **Unit tests** for core functionality
2. **Integration tests** for CLI commands
3. **Error case tests** for edge cases
4. **Platform-specific tests** if needed

## 📝 Documentation

### Documentation Standards

- **Clear and concise** writing
- **Code examples** for all features
- **Configuration examples** for common use cases
- **Troubleshooting guides** for common issues

### Documentation Structure

- **README.md** - Project overview and quick start
- **INSTALL.md** - Detailed installation instructions
- **USAGE.md** - Comprehensive usage guide
- **CONTRIBUTING.md** - This file
- **examples/** - Configuration examples

## 🔧 Development Tools

### Recommended Tools

- **VS Code** with Python extension
- **PyLint** for code quality
- **Black** for code formatting
- **MyPy** for type checking

### Development Commands

```bash
# Format code
black provisioner/ tests/

# Lint code
pylint provisioner/

# Type checking
mypy provisioner/

# Run tests
python test_provisioner.py
```

## 🚀 Release Process

### Versioning

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR** - Breaking changes
- **MINOR** - New features (backward compatible)
- **PATCH** - Bug fixes (backward compatible)

### Release Checklist

- [ ] All tests pass
- [ ] Documentation updated
- [ ] Changelog updated
- [ ] Version bumped
- [ ] Release notes written
- [ ] Tagged and pushed

## 🤝 Community Guidelines

### Code of Conduct

- **Be respectful** and inclusive
- **Help others** learn and grow
- **Provide constructive feedback**
- **Follow project conventions**

### Communication

- **Use clear language** in issues and PRs
- **Provide context** for suggestions
- **Be patient** with responses
- **Ask questions** when unsure

## 📞 Getting Help

- **GitHub Issues** - For bugs and feature requests
- **GitHub Discussions** - For questions and ideas
- **Documentation** - For usage questions
- **Wiki** - For detailed guides

## 🙏 Recognition

Contributors will be recognized in:

- **README.md** contributors section
- **Release notes** for significant contributions
- **GitHub contributors** page

Thank you for contributing to the Virtual Machine Provisioner! 🚀 