#Flask
from flask import Flask, redirect, url_for, jsonify
#Variables de entorno
from dotenv import load_dotenv
#rutas
from routes import routes

app = Flask(__name__)

load_dotenv()

routes(app)


if __name__ == "__main__":
    app.run()
