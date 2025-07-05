from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
# from sqlalchemy.pool import NullPool
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# Construct the SQLAlchemy connection string
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"


def connect_to_supabase():
    """
    Connect to the Supabase PostgreSQL database.
    """
    try:
        engine = create_engine(DATABASE_URL, poolclass=NullPool)
        with engine.connect() as connection:
            print("Connection to Supabase successful!")
        return engine
    except Exception as e:
        print(f"Failed to connect to Supabase: {e}")
        return None

  

