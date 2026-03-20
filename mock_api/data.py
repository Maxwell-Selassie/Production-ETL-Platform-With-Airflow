"""
Product catalogue and dynamic pricing logic.
Prices fluctuate realistically throughout the day —
simulating a real pricing service that updates based on demand/supply.
"""

from datetime import datetime
from random import uniform, seed as random_seed

# Our 25 grocery products — matches exactly what's in the orders DB
PRODUCTS = [
    {"product_id": 1,  "name": "Organic Bananas 1kg",          "category": "Fruits & Vegetables",    "base_price": 1.49},
    {"product_id": 2,  "name": "Baby Spinach 200g",             "category": "Fruits & Vegetables",    "base_price": 2.29},
    {"product_id": 3,  "name": "Whole Milk 2L",                 "category": "Dairy & Eggs",           "base_price": 1.79},
    {"product_id": 4,  "name": "Free Range Eggs 12pk",          "category": "Dairy & Eggs",           "base_price": 3.49},
    {"product_id": 5,  "name": "Cheddar Cheese 400g",           "category": "Dairy & Eggs",           "base_price": 4.29},
    {"product_id": 6,  "name": "Chicken Breast 500g",           "category": "Meat & Seafood",         "base_price": 5.99},
    {"product_id": 7,  "name": "Atlantic Salmon Fillet 300g",   "category": "Meat & Seafood",         "base_price": 8.49},
    {"product_id": 8,  "name": "Sourdough Bread 800g",          "category": "Bakery",                 "base_price": 3.29},
    {"product_id": 9,  "name": "Croissants 4pk",                "category": "Bakery",                 "base_price": 3.49},
    {"product_id": 10, "name": "Orange Juice 1L",               "category": "Beverages",              "base_price": 2.99},
    {"product_id": 11, "name": "Sparkling Water 6pk",           "category": "Beverages",              "base_price": 3.99},
    {"product_id": 12, "name": "Greek Yogurt 500g",             "category": "Dairy & Eggs",           "base_price": 2.79},
    {"product_id": 13, "name": "Pasta 500g",                    "category": "Pantry & Dry Goods",     "base_price": 1.49},
    {"product_id": 14, "name": "Olive Oil 750ml",               "category": "Pantry & Dry Goods",     "base_price": 7.49},
    {"product_id": 15, "name": "Tomato Sauce 400g",             "category": "Pantry & Dry Goods",     "base_price": 1.29},
    {"product_id": 16, "name": "Dark Chocolate 100g",           "category": "Snacks & Confectionery", "base_price": 2.49},
    {"product_id": 17, "name": "Potato Chips 150g",             "category": "Snacks & Confectionery", "base_price": 1.79},
    {"product_id": 18, "name": "Frozen Pizza Margherita",       "category": "Frozen Foods",           "base_price": 4.49},
    {"product_id": 19, "name": "Ice Cream 500ml",               "category": "Frozen Foods",           "base_price": 3.99},
    {"product_id": 20, "name": "Shampoo 400ml",                 "category": "Personal Care",          "base_price": 4.99},
    {"product_id": 21, "name": "Dish Soap 500ml",               "category": "Household",              "base_price": 2.49},
    {"product_id": 22, "name": "Paper Towels 3pk",              "category": "Household",              "base_price": 3.29},
    {"product_id": 23, "name": "Brown Rice 1kg",                "category": "Pantry & Dry Goods",     "base_price": 2.29},
    {"product_id": 24, "name": "Almond Milk 1L",                "category": "Dairy & Eggs",           "base_price": 2.49},
    {"product_id": 25, "name": "Blueberries 125g",              "category": "Fruits & Vegetables",    "base_price": 3.29},
]


def get_current_price(product_id: int, base_price: float) -> float:
    """
    Simulate realistic price fluctuation.
    Uses date + product_id as seed so price is consistent
    within the same day but changes day to day.
    This mimics a real pricing engine.
    """
    today = datetime.now().strftime("%Y%m%d")
    random_seed(f"{today}{product_id}")
    fluctuation = uniform(-0.10, 0.15)  # -10% to +15%
    price = base_price * (1 + fluctuation)
    return round(price, 2)


def get_all_products_with_prices() -> list[dict]:
    return [
        {
            **product,
            "current_price": get_current_price(product["product_id"], product["base_price"]),
            "snapshotted_at": datetime.now().isoformat(),
        }
        for product in PRODUCTS
    ]


def get_product_by_id(product_id: int) -> dict | None:
    product = next((p for p in PRODUCTS if p["product_id"] == product_id), None)
    if not product:
        return None
    return {
        **product,
        "current_price": get_current_price(product["product_id"], product["base_price"]),
        "snapshotted_at": datetime.now().isoformat(),
    }