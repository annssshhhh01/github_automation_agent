from __future__ import annotations

from typing import Any

import requests
from tenacity import retry, stop_after_attempt, wait_exponential

from src.config import config
from src.exceptions import GitHubAPIError


class GitHubClient:
    """
    Centralized GitHub REST API client.
    Every native and synthesized capability
    must communicate with GitHub through this class.
    """

    BASE_URL = "https://api.github.com"

    def __init__(self):

        self.owner = config.GITHUB_OWNER
        self.repo = config.GITHUB_REPO

        self.headers = {
            "Authorization": f"Bearer {config.GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        reraise=True,
    )
    def request(
        self,
        method: str,
        endpoint: str,
        **kwargs: Any,
    ):

        url = f"{self.BASE_URL}{endpoint}"

        response = requests.request(
            method=method,
            url=url,
            headers=self.headers,
            timeout=30,
            **kwargs,
        )

        if response.status_code >= 400:
            raise GitHubAPIError(
                f"GitHub API Error {response.status_code}: {response.text}"
            )

        if response.text:
            return response.json()

        return {}
