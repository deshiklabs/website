from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/services')
def services_page():
    return render_template('services.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/careers')
def careers_page():
    return render_template('careers.html')

@app.route('/products')
def products_page():
    return render_template('products.html')




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, threaded=True ,debug=True)
