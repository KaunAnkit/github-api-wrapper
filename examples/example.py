from github_api.client import GithubClient
from dotenv import load_dotenv
import os

load_dotenv()

client = GithubClient(os.getenv("YOUR_TOKEN_HERE"))

user = client.get_user("torvalds")

print(user.login)
print(user.followers)
print(user.public_repos)
print(user.location)