from pydantic import BaseModel, Field


class User(BaseModel):

    login:str
    id: int
    name: str | None = None
    company: str | None = None
    location: str | None = None
    followers: int
    following: int
    public_repos: int
    avatar_url: str
    html_url: str


class Repository(BaseModel):

    name: str
    description : str | None = None
    stars : int = Field(alias="stargazers_count")
    forks : int = Field(alias="forks_count")
    language : str | None = None


class SearchRepositoriesResponse(BaseModel):

    total_count: int
    incomplete_results: int
    items : list[Repository]

