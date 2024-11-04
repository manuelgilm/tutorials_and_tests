from pydantic import BaseModel 
from typing import List
from typing import Union 


class User(BaseModel):
    first_name: str 
    last_name: str
    username: Union[str, None] = None
    email: str


    
class UserList(BaseModel):
    users: List[User]
