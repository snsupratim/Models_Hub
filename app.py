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

# @app.route('/advertising')
# def advertising():
#     # Here you can integrate your advertising page
#     return render_template('advertising.html')

# @app.route('/insurance')
# def insurance():
#     # Here you can integrate your advertising page
#     return render_template('insurance.html')



if __name__ == '__main__':
    app.run(debug=True)
