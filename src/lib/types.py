# external imports
from pydantic import BaseModel

# internal imports


# define the request body
class RequestBody(BaseModel):
    prompt: str


# define the response body
class ResponseBody(BaseModel):
    content: str
