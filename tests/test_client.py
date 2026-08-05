from github_api.client import GitHubClient
from github_api.exceptions import UserNotFoundError

import pytest

def test_get_user():

    client = GitHubClient("fake_token")

    client._request = lambda *args, **kwargs: {
        "login": "torvalds",
        "followers": 12324,
        "following": 0,
        "public_repos": 50,
        "avatar_url": "https://example.com/avatar.png",
        "html_url": "https://github.com/torvalds"
    }

    user = client.get_user("torvalds")

    assert user.login == "torvalds"
    assert user.followers == 12324
    assert user.following == 0
    assert user.public_repos == 50
    assert user.avatar_url == "https://example.com/avatar.png"
    assert user.html_url == "https://github.com/torvalds"


def test_no_user():

    client = GitHubClient("fake_token")

    client._request = fake_request

    with pytest.raises(UserNotFoundError):
        client.get_user("this_is_not_a_user")



def fake_request(*args, **kwargs):
    
    raise UserNotFoundError("User not found")