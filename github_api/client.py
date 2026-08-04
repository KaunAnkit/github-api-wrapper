import httpx
from github_api.models import User


class GithubClient:

    BASE_URL = "https://api.github.com/"

    def __init__(self,token : str):

        self.token = token


        self.client = httpx.Client(
            base_url=self.BASE_URL,
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github+json"
            },
            timeout=10.0,
        )

    def _request(self, method :str, endpoint: str, **kwargs):

        response = self.client.request(
            method=method,
            url=endpoint,
            **kwargs
        )

        response.raise_for_status()

        return response.json()



    def get_user(self,username:str):

        data = self._request(
            "GET",
            f"/users/{username}"
        )

        return User.model_validate(data)

    