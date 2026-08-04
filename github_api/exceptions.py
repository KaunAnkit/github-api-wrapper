class GitHubAPIError(Exception):
    """Base exception for all GitHub API errors."""
    pass


class AuthenticationError(GitHubAPIError):
    """Raised when authentication fails."""
    pass


class UserNotFoundError(GitHubAPIError):
    """Raised when a GitHub user does not exist."""
    pass


class RateLimitError(GitHubAPIError):
    """Raised when the GitHub API rate limit is exceeded."""
    pass


class ServerError(GitHubAPIError):
    """Raised when GitHub returns a 5xx error."""
    pass