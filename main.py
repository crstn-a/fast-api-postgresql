from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post (BaseModel):                 #BaseModel is the schema that you want to force the user that the title and content only the data you expect to receive
    title: str                          #It validates the data that the user sent
    content: str
    published: bool = True              #Assign a property that is optional for our schema, default is True if the user doesn't provide a value.
    rating: Optional[int] = None        #An optional property that is equal to integer but the default value will be none if the user doesn't provide.


#path operations / routes
@app.get("/")                           #decorator - the path of this function when the http calls it.
def root():                             #def - function / root() = function name
    return {"message": "Hello Word!"}   #async is used only if you want to have an asynchronous task (api call, communicating with the db)


@app.get("/posts")                      #Get - Getting Data from the API server
def get_post():
    return {"data": "Your post."}

##@app.post("/createpost")                                                              #Post - Send Data to the API server
#def create_post(payload: dict = Body(...)):                                            #It extracts all of the fields in the Body(...) converted into python dictionary and it's going to store in the variable name 'payload
    #print(payload)                                                                     #It prints what contains in the body. - Import `fastapi.params`
    #return {"new_post": f"title: {payload['title']} content: {payload['content']}"}

@app.post("/createpost") 
def create_post(post: Post):        #It creates a Parameter base on the class Post (BaseModel) and assign it to var `post`
    print(post.rating)              #Filter using: print(post.title) if you want to print the specific data body.
    print(post.dict())              #Convert pydantic model to a dictionary
    return {"data": post}           #prints the pydantic model dictionary that assigns to the var  `post`


#1:22:45 ctd