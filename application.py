from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def home():
    return render_template('home.html')

@application.route('/contact')
def contact():
    return render_template('contact.html')

@application.route('/data_work')
def data_work():
    return render_template('data_work.html')

@application.route('/products')
def products():
    return render_template('products.html')

@application.route('/insights')
def insights():
    return render_template('insights.html')

if __name__ == "__main__":
    application.run(host='0.0.0.0',debug=True)
