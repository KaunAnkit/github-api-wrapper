# GitHub API Wrapper

[![PyPI version](https://img.shields.io/pypi/v/github-api-wrapper-py.svg)](https://pypi.org/project/github-api-wrapper-py/)
[![Python Versions](https://img.shields.io/pypi/pyversions/github-api-wrapper-py.svg)](https://pypi.org/project/github-api-wrapper-py/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A lightweight, type-safe Python SDK for interacting with the GitHub REST API. Built with **httpx**, **Pydantic**, and **Tenacity**, it provides a clean interface with automatic retries, pagination, and custom exception handling.

---

## Installation

```bash
pip install github-api-wrapper-py
```

---

## Features

- Type-safe Pydantic models
- GitHub User API
- Repository API
- Repository search
- Automatic pagination
- Custom exceptions
- Built on httpx

## Installation

```bash
pip install github-rest-sdk
```

## Quick Start

```python
from github_api import GitHubClient

client = GitHubClient("YOUR_GITHUB_TOKEN")

user = client.get_user("torvalds")

print(user.login)
print(user.followers)
```

Retrieve repository information:

```python
repo = client.get_repo("openai", "openai-python")

print(repo.name)
print(repo.stars)
print(repo.forks)
```

Search repositories:

```python
results = client.search_repositories("machine learning")

print(results.total_count)

for repo in results.items[:5]:
    print(repo.name)
```

---

## API Reference

### Users

```python
client.get_user(username)

client.list_user_repos(username)

client.list_all_user_repos(username)
```

### Repositories

```python
client.get_repo(owner, repo)

client.search_repositories(query)
```

---

## Project Structure

```
github-api-wrapper/
│
├── github_api/
│   ├── client.py
│   ├── models.py
│   ├── exceptions.py
│   └── __init__.py
│
├── examples/
├── tests/
├── README.md
├── pyproject.toml
└── LICENSE
```

---

## Why This Project?

This project was built to understand how production-quality Python SDKs are designed.

It demonstrates:

- HTTP client abstraction
- Type-safe models using Pydantic
- Automatic retry handling with Tenacity
- Pagination helpers
- Custom exception hierarchy
- Python packaging using `pyproject.toml`
- Publishing packages to PyPI

---

## Roadmap

- [ ] Async client
- [ ] Additional GitHub REST API endpoints
- [ ] GitHub Actions CI
- [ ] Improved test coverage
- [ ] OAuth authentication support

---

## License

This project is licensed under the MIT License.

---

## Contributing

Contributions, suggestions, and bug reports are welcome. Feel free to open an issue or submit a pull request.

---

## Links

- **PyPI:** https://pypi.org/project/github-api-wrapper-py/
- **GitHub:** https://github.com/KaunAnkit/github-api-wrapper
