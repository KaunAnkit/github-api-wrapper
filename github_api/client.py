import httpx
from github_api.models import User, Repository , SearchRepositoriesResponse

from github_api.exceptions import (
    AuthenticationError,
    UserNotFoundError,
    RateLimitError,
    ServerError,
    GitHubAPIError,
)

from tenacity import retry, stop_after_attempt,wait_exponential,retry_if_exception_type


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


    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1,min=1,max=8),
        retry=retry_if_exception_type((RateLimitError, ServerError)),
        reraise=True
    )
    def _request(self, method :str, endpoint: str, **kwargs):

        response = self.client.request(
            method=method,
            url=endpoint,
            **kwargs
        )

        if response.status_code == 401:
            raise AuthenticationError("Invalid GitHub token.")

        elif response.status_code == 404:
            raise UserNotFoundError(f"Resource '{endpoint}' was not found.")

        elif response.status_code == 429:
            raise RateLimitError("GitHub API rate limit exceeded.")

        elif 500 <= response.status_code < 600:
            raise ServerError("GitHub server error.")

        elif response.is_error:
            raise GitHubAPIError(
                f"GitHub API returned {response.status_code}"
            )

        return response.json()



    def get_user(self,username:str):

        data = self._request(
            "GET",
            f"/users/{username}"
        )

        return User.model_validate(data)

    def get_repo(self,owner : str,repo:str)-> Repository:

        data = self._request(
            "GET",
            f"/repos/{owner}/{repo}"
        )

        return Repository.model_validate(data)


    def list_user_repos(self,username:str,page : int = 1,per_page: int = 30,) -> list[Repository]:
        data = self._request(
            "GET",
            f"/users/{username}/repos",
            params={
                "page": page,
                "per_page": per_page,
            }
        )

        repo_list = [Repository.model_validate(repo_data) for repo_data in data ]

        return repo_list


    def search_repositories(
                self,
                query : str,
                sort: str = "stars",
                page : int = 1,
                per_page: int = 30,
        ):

        data = self._request(
            "GET",
            f"/search/repositories",
            params = {
                "q":query,
                "sort": sort,
                "page": page,
                "per_page": per_page,
            }
        )

        return SearchRepositoriesResponse.model_validate(data)

    def list_all_user_repos(self, username: str):
        page_count = 1
        repo_list = []
        while True:
            data = self.list_user_repos(  
                username,
                page = page_count
            )
            if not data:
                break
            repo_list.extend(data)
            page_count +=1

        return repo_list

        