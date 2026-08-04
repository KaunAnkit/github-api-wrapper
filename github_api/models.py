from pydantic import BaseModel


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