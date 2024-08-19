from flask import Flask
from blueprints.user import user

from settings import set_app

app = Flask(__name__)
set_app(app)


@app.route("/", methods=["GET"])
def hello_world():
    return {"message": "Hello, World!"}


app.register_blueprint(user, url_prefix="/users")

if __name__ == "__main__":
    from db import db

    db.init_app(app)
    # push context manually to app
    with app.app_context():
        db.create_all()

    app.run(debug=True)
