class GitHubAPIError(Exception):
    """Raised when a GitHub API request fails."""


class CapabilityNotFoundError(Exception):
    """Raised when a requested capability does not exist."""


class CapabilityGenerationError(Exception):
    """Raised when capability synthesis fails."""


class SandboxExecutionError(Exception):
    """Raised when generated code fails inside the sandbox."""
