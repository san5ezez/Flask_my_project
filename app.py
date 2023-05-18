from flask import Flask, render_template, request, redirect, url_for, flash, render_template, request, redirect

app = Flask(__name__)

#Обратите внимание, что секретный ключ должен быть храниться в секрете и не должен быть раскрытым в открытом коде или публичном репозитории.
app.secret_key = 'pass'

# Модель данных для товара
products = [
    {
        'id': 1,
        'name': 'Product 1',
        'image_url': 'https://justfunfacts.com/wp-content/uploads/2021/02/milka-3.jpg',
        'price': 10.99,
        'description': 'Description for Product 1',
        'category': 'Category 1',
        'quantity': 10
    },
    {
        'id': 2,
        'name': 'Product 2',
        'image_url': 'https://cdn.shopify.com/s/files/1/0658/6076/3887/products/milkaoreowhite_cad7f4f2-97f2-4866-bf05-f71a0e03e607.png',
        'price': 19.99,
        'description': 'Description for Product 2',
        'category': 'Category 2',
        'quantity': 5
    }
]

# Главная страница клиента
@app.route('/')
def index():
    return render_template('index.html')

# Админка
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        # Проверка логина и пароля
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'milk_admin' and password == 'Atmosphere29567':
            return render_template('admin.html', products=products)
        else:
            flash('Invalid login credentials.', 'error')

    return render_template('login.html')

# Обработка формы добавления товара
@app.route('/admin/add_product', methods=['POST'])
def add_product():
    # Получение данных из формы
    name = request.form.get('name')
    image_url = request.form.get('image_url')
    price = float(request.form.get('price'))
    description = request.form.get('description')
    category = request.form.get('category')
    quantity = int(request.form.get('quantity'))

    # Создание нового объекта товара
    new_product = {
        'id': len(products) + 1,
        'name': name,
        'image_url': image_url,
        'price': price,
        'description': description,
        'category': category,
        'quantity': quantity
    }

    # Добавление товара в список products
    products.append(new_product)

    flash('Product added successfully.', 'success')

    # Перенаправление на страницу админки
    return redirect(url_for('admin'))

# Поиск товара по ID в списке products
def find_product_by_id(product_id):
    for product in products:
        if product['id'] == product_id:
            return product
    return None

# Отображение формы редактирования товара с текущими значениями
@app.route('/admin/edit_product/<int:product_id>', methods=['GET'])
def edit_product(product_id):
    # Поиск товара по ID
    product = find_product_by_id(product_id)

    if product:
        return render_template('edit_product.html', product=product)
    else:
        flash('Product not found.', 'error')
        return redirect(url_for('admin'))

# Обработка формы редактирования товара
@app.route('/admin/update_product/<int:product_id>', methods=['POST'])
def update_product(product_id):
    # Получение данных из формы
    name = request.form.get('name')
    image_url = request.form.get('image_url')
    price = float(request.form.get('price'))
    description = request.form.get('description')
    category = request.form.get('category')
    quantity = int(request.form.get('quantity'))

    # Поиск товара по ID
    product = find_product_by_id(product_id)

    if product:
        # Обновление данных товара
        product['name'] = name
        product['image_url'] = image_url
        product['price'] = price
        product['description'] = description
        product['category'] = category
        product['quantity'] = quantity

        flash('Product updated successfully.', 'success')
    else:
        flash('Product not found.', 'error')

    # Перенаправление на страницу админки
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run()
