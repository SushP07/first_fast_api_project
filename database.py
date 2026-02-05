import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Read DB connection from environment so the container can connect to host Postgres
# Fallback default uses host.docker.internal (resolves to Windows host from container)
DATABASE_URL = os.getenv(
	"DATABASE_URL",
	"postgresql://postgres:1234@host.docker.internal:5432/food_delivery",
)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

