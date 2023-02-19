from flask import Flask, render_template, redirect, request
from controllers.country_controller import countries_blueprint
from controllers.destination_controller import destinations_blueprint

app = Flask(__name__)

app.register_blueprint(countries_blueprint)
app.register_blueprint(destinations_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debu=True)