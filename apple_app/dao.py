from apple_app.models import Category, Product
from apple_app import app

def load_categories():
    with app.app_context():
        return Category.query.all()

def load_products(id=None, kw=None):
    with app.app_context():
        products = Product.query
        if id:
            products = products.filter(Product.category_id.__eq__(id))
        if kw:
            products = products.filter(Product.name.contains(kw))
        return products.all()
