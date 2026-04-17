from fastapi import FastAPI, HTTPException
app = FastAPI()

# sample list of products with categories
products = [
    {"id": 1, "name": "iPhone 15", "category": "electronics", "price": 79999},
    {"id": 2, "name": "Samsung TV", "category": "electronics", "price": 45000},
    {"id": 3, "name": "Nike Shoes", "category": "footwear", "price": 5999},
    {"id": 4, "name": "Levi Jeans", "category": "clothing", "price": 2999},
    {"id": 5, "name": "Boat Headphones", "category": "electronics", "price": 1999},
]

@app.get("/") # GET / - home
def home():
    return {"message": "Welcome to Garima's Product API"}

@app.get("/products") # GET /products - returns all products
def get_products(category: str = None):
    # if category is given, filter by it - this is query parameter, (example: /products?category=electronics)
    if category:
        filtered = [p for p in products if p["category"] == category]
        if not filtered:
            return {"message": f"no products found in '{category}' category"}
        return {"category": category, "products": filtered}

    return {"products": products} # no filter - return everything

# GET /products/{product_id} - return product by id - this is path parameter (example: /products/1)
@app.get("/products/{product_id}")
def get_product(product_id: int):
    # searching for the product
    for p in products:
        if p["id"] == product_id:
            return {"product": p}

    # product not found - raise HTTP error
    raise HTTPException(status_code=404, detail=f"product with id {product_id} not found!") 