from fastapi import Depends,FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import Product

from database import SessionLocal, engine

import database_models

from sqlalchemy.orm import Session

app = FastAPI()
app.add_middleware(

    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
)

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    """
    Root greeting endpoint.

    Returns a simple welcome string used to verify the server is running.
    """
    return "Welcome to Sushi's Web"

products = [
  
   Product(id=1, name="Sushi Roll", description="Delicious sushi roll", price=12.99, quantity=50),
    Product(id=2, name="Tempura", description="Crispy tempura", price=8.99, quantity=30),
    Product(id=3, name="Miso Soup", description="Traditional miso soup", price=4.99, quantity=100),
    Product(id=4, name="Green Tea", description="Refreshing green tea", price=2.99, quantity=200)
    

]

def get_db():
    """
    Dependency that provides a SQLAlchemy `Session` for request handlers.

    Usage: include `db: Session = Depends(get_db)` in endpoint signatures.
    The function yields a database session and ensures it is closed after
    the request completes (context-managed lifecycle).
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def initialize_database():
    """
    Seed the database with a small set of sample products.

    This helper checks whether any `Product` rows exist; if none are
    present it inserts the in-memory `products` list into the database.
    It is safe to call on startup and avoids duplicating rows.
    """
    db = SessionLocal()

    count = db.query(database_models.Product).count()
    if count > 0:
        db.close()
        return
    for product in products:
        db_product = database_models.Product(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            quantity=product.quantity
        )
        db.add(db_product)
    db.commit()
    db.close()

initialize_database()

@app.get("/products")
def list_products(db: Session = Depends(get_db)):
    """
    Return all products.

    Returns a list of `Product` ORM objects (FastAPI will use Pydantic
    models to serialize the response when appropriate).
    """
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/products/{product_id}")
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single product by its `product_id`.

    Returns the product object if found, otherwise returns a small JSON
    error message. The endpoint uses the provided DB session dependency.
    """
    db_product = db.query(database_models.Product).filter(database_models.Product.id == product_id).filter(database_models.Product.id == product_id).first()
    if db_product:
        return db_product
    return {"error": "Product not found"}

@app.post("/products")
def add_product(new_product: Product, db: Session = Depends(get_db)):
    """
    Create a new product.

    Accepts a `Product` payload (validated by Pydantic `Product` model from
    `models.py`), constructs an ORM `Product`, persists it to the database,
    and returns the newly created record.
    """
    db_product = database_models.Product(
        id=new_product.id,
        name=new_product.name,
        description=new_product.description,
        price=new_product.price,
        quantity=new_product.quantity
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.put("/products")
def update_product(product_id: int, updated_product: Product, db: Session = Depends(get_db)):
    """
    Update an existing product identified by `product_id`.

    If the product exists, update its fields with values from the
    `updated_product` payload and persist the changes. Returns the updated
    ORM object or an error message if the product does not exist.
    """
    db_product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    if not db_product:
        return {"error": "Product not found"}
    db_product.name = updated_product.name
    db_product.description = updated_product.description
    db_product.price = updated_product.price
    db_product.quantity = updated_product.quantity
    db.commit()
    return db_product

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """
    Delete a product by `product_id`.

    Removes the product row from the database if it exists and returns a
    confirmation message. If the product cannot be found, returns an error
    JSON object.
    """
    db_product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    if not db_product:
        return {"error": "Product not found"}
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}

