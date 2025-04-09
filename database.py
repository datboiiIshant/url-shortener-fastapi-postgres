# Importing required functions and classes from SQLAlchemy
from sqlalchemy import create_engine # Used to establish a connection to the database
from sqlalchemy.orm import sessionmaker # Factory for creating new Session objects
from sqlalchemy.ext.declarative import declarative_base # Used for creating ORM base class

# Defining the URL for the PostgreSQL database connection
URL_DATABASE = 'postgresql://postgres:8560229@localhost:5432/URL_Shortener'

# Creating the database engine, which manages the connection pool and communication with the database
engine = create_engine(URL_DATABASE)

# Creating a session factory (SessionLocal) with specific configurations:
# - autocommit=False: we want to manually commit transactions
# - autoflush=False: changes are not automatically flushed to the database
# - bind=engine: associate the session with the previously created engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine )

# Creating a declarative base class to define ORM models from it
Base = declarative_base()