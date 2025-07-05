#Create models here
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import Depends, FastAPI, HTTPException, Query
from typing import Optional, List
from database.supabase import connect_to_supabase

class captions(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(default=None)
    file_url: str = Field(index=True, nullable=False)
    caption_text: str = Field(index=True, nullable=False)
    created_at: str = Field(default=None, nullable=False)
    updated_at: str = Field(default=None, nullable=False)   

# Create the database engine (Holds the connection to the database)
engine = connect_to_supabase()

# Now work on the caption generator
# Add to the db table
with Session(engine) as session:
        session.add(captions(
            user_id=1,
            file_url="https://example.com/image.jpg",
            caption_text="A beautiful sunset over the mountains.",
            created_at="2023-10-01T12:00:00Z",
            updated_at="2023-10-01T12:00:00Z"))
        session.commit()
        