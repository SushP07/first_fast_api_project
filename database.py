from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


DATABASE_URL = "postgresql://postgres:1234@localhost:5432/food_delivery"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

