from src.github.auth import github_client

response = github_client.request(
    "GET",
    "/user",
)

print(response["login"])
