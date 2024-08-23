from flask import Blueprint, render_template, request, redirect, url_for
from app.ToWatchList.models import User, ToWatchList, ToDo, Notes
from app.app import db
from app.config import Config


to_watch_list = Blueprint("to_watch_list", __name__, template_folder="templates")


@to_watch_list.route("/", methods=["GET"])
def index():
    to_watch_items = ToWatchList.query.all()
    to_do_items = ToDo.query.all()
    notes_items = Notes.query.all()

    return render_template("index.html", to_watch_items=to_watch_items, to_do_items=to_do_items, notes_items=notes_items)


@to_watch_list.route("/delete/<int:item_id>", methods=["POST"])
def delete_to_watch_item(item_id):
    item = ToWatchList.query.get(item_id)
    db.session.delete(item)
    db.session.commit()

    return redirect(url_for("to_watch_list.index"))

@to_watch_list.route("/create", methods=["POST"])
def create_to_watch_item():
    title = request.form["title"]
    link = request.form["link"]

    new_item = ToWatchList(title=title, link=link)
    db.session.add(new_item)
    db.session.commit()

    return redirect(url_for("to_watch_list.index"))

@to_watch_list.route("/delete_todo/<int:item_id>", methods=["POST"])
def delete_to_do_item(item_id):
    item = ToDo.query.get(item_id)
    db.session.delete(item)
    db.session.commit()

    return redirect(url_for("to_watch_list.index"))

@to_watch_list.route("/create_todo", methods=["POST"])
def create_to_do_item():
    content = request.form["content"]

    new_item = ToDo(content=content)
    db.session.add(new_item)
    db.session.commit()

    return redirect(url_for("to_watch_list.index"))


@to_watch_list.route("/delete_notes/<int:item_id>", methods=["POST"])
def delete_notes_item(item_id):
    item = Notes.query.get(item_id)
    db.session.delete(item)
    db.session.commit()

    return redirect(url_for("to_watch_list.index"))

@to_watch_list.route("/create_notes", methods=["POST"])
def create_notes_item():
    content = request.form["content"]

    new_item = Notes(content=content)
    db.session.add(new_item)
    db.session.commit()

    return redirect(url_for("to_watch_list.index"))