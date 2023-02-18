from flask import Flask, render_template, redirect, request
from controllers.country_controller import countries_blueprrnt

app = Flask(__name__)

app.register_blueprint(countries_blueprrnt)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debu=True)