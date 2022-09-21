from flask import Blueprint, render_template, request, url_for, redirect, flash

from homework_06.models import Poem, db
from homework_06.views.forms.poems import CreatePoemForm

poems_app = Blueprint("poems_app", __name__)


@poems_app.route("/", endpoint="list")
def get_poems():
    poems = Poem.query.order_by(Poem.id).all()
    return render_template("poems/list.html", poems=poems)


@poems_app.route("/<int:poem_id>/", endpoint="details")
def get_poem_by_id(poem_id: int):
    poem: Poem = Poem.query.get_or_404(
        poem_id,
        f"Product #{poem_id} not found!",
    )

    return render_template(
        "poems/details.html",
        poem=poem,
    )


@poems_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_poem():
    form = CreatePoemForm()

    if request.method == "GET":
        return render_template("poems/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("poems/add.html", form=form), 400

    poem_name = form.name.data
    poem = Poem(name=poem_name)
    db.session.add(poem)
    db.session.commit()

    flash(f"Successfully added poem {poem.name}!")
    url = url_for("poems_app.details", poem_id=poem.id)
    return redirect(url)