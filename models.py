from sqlalchemy import Column, Integer, String # Importing necessary SQLAlchemy classes for defining columns and data types
from database import Base # Importing the Base class which is used to define ORM models

# Defining the URLs class which maps to the 'urls' table in the database
class URLs(Base):
    __tablename__ = 'urls' # Table Name

    # Defining the 'id' column as an Integer, primary key, and indexed for faster querying
    id = Column(Integer, primary_key=True, index=True)
    # Defining the 'URL' column as a String, with an index for optimized lookups
    URL = Column(String, index=True)
    # Defining the 'Shortened_URL' column as a String, also indexed
    Shortened_URL = Column(String, index=True)
