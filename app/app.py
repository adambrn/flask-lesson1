from flask import Flask, render_template

app = Flask(__name__)

class Product:
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

class Category:
    def __init__(self, name, slug, products):
        self.name = name
        self.slug = slug
        self.products = products

categories_data = [
    Category('Одежда', 'clothing', [Product(1, 'Куртка', 'Теплая зимняя куртка', 100), Product(2, 'Джинсы', 'Стильные джинсы', 50)]),
    Category('Обувь', 'shoes', [Product(3, 'Кроссовки', 'Удобные кроссовки', 80), Product(4, 'Сапоги', 'Стильные сапоги', 120)]),
    # Другие категории
]

@app.route('/')
def home():
    return render_template('base.html', title='Главная', categories=categories_data)

@app.route('/category/<category_slug>')
def category(category_slug):
    category = next((c for c in categories_data if c.slug == category_slug), None)
    if category:
        return render_template('category.html', title=category.name, category=category, categories=categories_data)
    return "Категория не найдена"

@app.route('/product/<int:product_id>')
def product(product_id):
    for category in categories_data:
        for product in category.products:
            if product.id == product_id:
                return render_template('product.html', title=product.name, product=product, categories=categories_data)
    return "Товар не найден"

if __name__ == '__main__':
    app.run(debug=True)
