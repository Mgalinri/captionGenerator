from fastapi import Body, FastAPI, UploadFile, File
from typing import Annotated
import os
from ml_model import obtain_caption
from fastapi.middleware.cors import CORSMiddleware
# Initialize FastAPI app
app= FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
If the parameter is also declared in the path, it will be used as a path parameter.
If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter.
If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body."""


@app.post("/caption")
def get_caption_(image_path: UploadFile=File(...)):
    """
    Endpoint to obtain the caption of an image, specifically from a 
    file object.
    
    Args:
        image_path (str): The path or URL of the image.
    
    Returns:
        dict: A dictionary containing the caption of the image.
    """
    # Add the image to a directory named uploads
    with open(os.path.join("uploads",image_path.filename),"wb") as f:
        f.write(image_path.file.read())
    
    # Now use the image to obtain the caption
    caption = obtain_caption(os.path.join("uploads",image_path.filename))
    return {"caption": caption}