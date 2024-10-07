from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/models')
def models():
    # Here you can integrate your ML models
    return render_template('models.html')

if __name__ == '__main__':
    app.run(debug=True)
