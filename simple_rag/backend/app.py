from flask import Flask
from config.mongodb import mongo
from config.settings import set_mongodb_config
from dotenv import load_dotenv

from routes.db_operations import collections
from routes.users import users
load_dotenv()

app = Flask(__name__)
set_mongodb_config(app)
mongo.init_app(app, uri=app.config['MONGO_URI'])

@app.route("/")
def home():
    return "Hello, World!"

app.register_blueprint(collections, url_prefix='/collections')
app.register_blueprint(users, url_prefix='/users')

if __name__ == "__main__":
    app.run(debug=True)
