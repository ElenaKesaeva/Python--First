from os import getenv

from flask import Flask, render_template
from flask_migrate import Migrate

from homework_06.models import db
from homework_06.views.poems import poems_app

app = Flask(__name__)


CONFIG_OBJECT = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_OBJECT}")
db.app = app
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)

app.register_blueprint(poems_app, url_prefix="/poems")


@app.route("/")
def index_view():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
