# Import FastAPI Modules
from fastapi import FastAPI, HTTPException, Depends
# from pydantic import BaseModel
from typing import Annotated # Annotated is used to provide additional typing metadata (for dependency injection)
import models # Import the database models
from database import engine, SessionLocal # Import database engine and session factory from the local database module
from sqlalchemy.orm import Session # SQLAlchemy session class for DB operations
from URL_Shortner import convert # Import custom URL conversion function

app = FastAPI() # Create FastAPI app instance
models.Base.metadata.create_all(bind=engine) # Create all database tables defined in models (if not already created)

# Dependency function to get a database session
def get_db():
    db = SessionLocal() # Create new DB session
    try:
        yield db  # Yield the session to use in the request
    finally:
        db.close() # Close the session after the request is done

db_dependency = Annotated[Session, Depends(get_db)] # Annotate the dependency to inject DB session into path operations

# Route to retrieve URL details by ID
@app.get('/URLs/{id}')
async def read_choices(id, db: db_dependency):
    result = db.query(models.URLs.id, models.URLs.URL).filter(models.URLs.id == id).first()
     # Query to get the ID and original URL from the database
    if not result: # If no result is found, raise a 404 error
        raise HTTPException(status_code=404, detail="Invalid !")
    return dict(result._mapping) # Return the result as a dictionary (id and URL)

# Route to shorten a given URL and store it
@app.post("/URLs/")
async def shorten_urls(URL, db: db_dependency):
    result = convert(URL) # Call the custom conversion function to shorten the URL
    db_URL = models.URLs(URL = result['url'], Shortened_URL=result['shortened_url'])
    # Create a new database record with original and shortened URL
    db.add(db_URL)
    db.commit()
    # Add and commit the new record to the database

    return result['shortened_url'] # Return the shortened URL as the response