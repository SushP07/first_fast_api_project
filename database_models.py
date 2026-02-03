

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, Integer

Base = declarative_base()


# Product
# ----------
# SQLAlchemy ORM model representing a product row in the `products` table.
# This class is used by the application's database layer to create the table
# (when running migrations or metadata.create_all) and to map query results
# into Python objects that the application can read and modify.
#
# Fields:
# - `id` (Integer): Primary key for the product. `index=True` creates a
#   database index to speed up lookups by id.
# - `name` (String): Product name. Indexed to allow fast searches by name.
# - `description` (String): Free-text description of the product.
# - `price` (Float): Unit price for the product (stored as a float).
# - `quantity` (Integer): Current stock quantity for the product.
#
# Notes:
# - The names here match the JSON fields used by the FastAPI endpoints so
#   Pydantic models can easily convert between request/response payloads
#   and database objects.
# - Add constraints, lengths or nullable flags here if you need stricter
#   validation at the database level (e.g. `String(200)`, `nullable=False`).
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
   