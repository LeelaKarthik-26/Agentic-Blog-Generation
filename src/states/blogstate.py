from typing import TypedDict
from pydantic import BaseModel, Field

# will genrerete structure out of the topic when called in BlogState
class Blog(BaseModel):
    title: str=Field(description="The title of the blog post")
    content: str=Field(description="The main content of the blog post")

# will store the state of the blog
class BlogState(TypedDict):
    topic: str
    blog: Blog
    current_language: str
