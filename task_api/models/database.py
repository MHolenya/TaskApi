# Import necessary libraries
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get database credentials from environment variables
DB_USER = os.environ['DB_USER']
DB_PASSW = os.environ['DB_PASSW']
DB_HOST = os.environ['DB_HOST']
DB_NAME = os.environ['DB_NAME']

# Construct MySQL connection string
mysql_route = f'mysql+mysqlconnector://{
    DB_USER}:{DB_PASSW}@{DB_HOST}/{DB_NAME}'

# Create database engine
engine = create_engine(mysql_route)

# Create scoped session for database interactions
db_session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

# Create base class for declarative models
Base = declarative_base()
Base.query = db_session.query_property()

# Function to initialize the database


def init_db() -> None:
    # Create all tables defined in the Base class
    Base.metadata.create_all(bind=engine)
