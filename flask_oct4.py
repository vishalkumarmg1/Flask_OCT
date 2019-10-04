from flask import (Flask,render_template)
app = Flask(__name__)

app.config.update(
    dict(SECRET_KEY='vishal')
)

@app.route('/')

def home():
    return render_template('home.html', hello="Hello Vishal")

if __name__ == '__main__':
    app.run(debug=True)
