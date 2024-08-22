from flask import Blueprint, render_template, request, redirect, url_for
from app.ToWatchList.models import User, ToWatchList
from app.app import db
from app.config import Config


to_watch_list = Blueprint("to_watch_list", __name__, template_folder="templates")


@to_watch_list.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        link = request.form.get("link")
        item = ToWatchList(title=title, link=link)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for("to_watch_list.index", items=ToWatchList.query.all()))

    if request.method == "GET":
        db_items = ToWatchList.query.all()
        return render_template("index.html", items=db_items)


@to_watch_list.route("/delete/<int:item_id>", methods=["POST"])
def delete(item_id):
    item = ToWatchList.query.get(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("to_watch_list.index", items=ToWatchList.query.all()))
