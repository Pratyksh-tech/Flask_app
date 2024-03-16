from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy shopping cart (you may replace this with a proper shopping cart implementation)
shopping_cart = []

@app.route('/')
def home():
    products = [
        {'name': 'Product 1', 'price': 10, 'image': 'product1.jpg'},
        {'name': 'Product 2', 'price': 20, 'image': 'product2.jpg'},
        # Add more products here
    ]
    categories = ['Category 1', 'Category 2', 'Category 3']  # Example categories

    return render_template('home.html', products=products, categories=categories)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Custom error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if request.method == 'POST':
        # Get product details from the form data
        product_id = request.form['product_id']
        product_name = request.form['product_name']
        quantity = int(request.form['quantity'])

        # Add product to shopping cart
        shopping_cart.append({'product_id': product_id, 'product_name': product_name, 'quantity': quantity})

        print("Shopping Cart Contents:")
        for item in shopping_cart:
            print(item)
        # Redirect to home page or any other page
        return redirect(url_for('home'))
    

if __name__ == '__main__':
    app.run(debug=True)
