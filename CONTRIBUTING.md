# Contributing

We welcome contributions to the Nano-Banana Autonomous Image Creation Bot! This document outlines the process for contributing to the project.

## Code of Conduct

This project follows a code of conduct to ensure a welcoming environment for all contributors. By participating, you agree to:

- Be respectful and inclusive
- Focus on constructive feedback
- Accept responsibility for mistakes
- Show empathy towards other contributors

## Getting Started

### Prerequisites
- Python 3.8+
- Git
- Google Gemini API key

### Setup
1. Fork the repository on GitHub
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/nano-banana-autonomous-img-bot.git
   cd nano-banana-autonomous-img-bot
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up your `.env` file (see SETUP.md)

## Development Process

### 1. Choose an Issue
- Check the [Issues](https://github.com/your-repo/nano-banana-autonomous-img-bot/issues) page
- Look for "good first issue" or "help wanted" labels
- Comment on the issue to indicate you're working on it

### 2. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-number-description
```

### 3. Make Changes
- Follow the existing code style
- Write clear, concise commit messages
- Test your changes thoroughly
- Update documentation if needed

### 4. Testing
Run the existing tests:
```bash
python -m pytest
```

Add tests for new features:
- Unit tests for core functions
- Integration tests for API calls
- End-to-end tests for image generation

### 5. Commit Changes
```bash
git add .
git commit -m "feat: add new feature description"
```

Follow conventional commit format:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation
- `style:` for formatting
- `refactor:` for code restructuring
- `test:` for testing
- `chore:` for maintenance

### 6. Push and Create Pull Request
```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:
- Clear title and description
- Reference to related issues
- Screenshots for UI changes
- Test results

## Development Guidelines

### Code Style
- Follow PEP 8 Python style guide
- Use type hints where possible
- Write docstrings for all functions
- Keep functions focused and modular

### File Structure
```
scripts/
├── new_edit_image.py    # Main script
├── utils.py             # Helper functions
└── tests/
    ├── test_generation.py
    └── test_api.py
```

### Error Handling
- Use try-except blocks for API calls
- Log errors with appropriate levels
- Provide meaningful error messages
- Handle rate limits gracefully

### Documentation
- Update README.md for new features
- Add docstrings to new functions
- Update usage examples
- Maintain API documentation

## Types of Contributions

### Bug Reports
- Use the issue template
- Include steps to reproduce
- Provide system information
- Attach relevant logs

### Feature Requests
- Clearly describe the proposed feature
- Explain the use case
- Consider implementation complexity

### Code Contributions
- Performance improvements
- New features
- Bug fixes
- Documentation improvements

### Documentation
- README updates
- Tutorial creation
- API documentation
- Translation contributions

## Review Process

### Pull Request Reviews
1. Automated checks (linting, tests)
2. Code review by maintainers
3. Discussion and feedback
4. Approval and merge

### Review Criteria
- Code quality and style
- Test coverage
- Documentation updates
- Performance impact
- Security considerations

## Community

### Communication
- Use GitHub Issues for bugs/features
- Join discussions in Pull Request comments
- Be responsive to feedback

### Recognition
Contributors are recognized through:
- GitHub contributor statistics
- Mention in release notes
- Attribution in documentation

## License

By contributing to this project, you agree that your contributions will be licensed under the same MIT License that covers the project.

## Questions?

If you have questions about contributing:
- Check existing issues and documentation
- Open a discussion issue
- Contact the maintainers

Thank you for contributing to the Nano-Banana Autonomous Image Creation Bot! Your efforts help make professional design accessible to businesses worldwide.
