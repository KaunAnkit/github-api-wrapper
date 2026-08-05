# GitHub API Wrapper
[![PyPI version](https://img.shields.io/pypi/v/github-api-wrapper-py.svg)](https://pypi.org/project/github-api-wrapper-py/)
[![Python](https://img.shields.io/pypi/pyversions/github-api-wrapper-py.svg)](https://pypi.org/project/github-api-wrapper-py/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
A lightweight, typed Python SDK for interacting with the GitHub REST API.

## Features

- Typed Pydantic models
- User API
- Repository API
- Repository search
- Automatic pagination
- Custom exceptions
- Built on httpx

## Installation

```bash
pip install github-api-wrapper
```

## Quick Start

```python
from github_api import GitHubClient

client = GitHubClient("YOUR_GITHUB_TOKEN")

user = client.get_user("torvalds")
print(user.login)

repo = client.get_repo("openai", "openai-python")
print(repo.stars)
```

## Available Methods

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

## Project Structure

```
github_api/
├── client.py
├── models.py
├── exceptions.py
└── __init__.py
```

## Roadmap

- [ ] Async client
- [ ] More GitHub endpoints
- [ ] Comprehensive test suite
- [ ] GitHub Actions CI

## License

MIT