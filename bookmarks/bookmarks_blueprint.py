from flask import Blueprint, redirect, render_template

from bookmarks.utils import Bookmarks

bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__)
"""
Отдельный блюпринт под работу с закладками
Работа реализована через сохранение id поста в списке
в json файле, поэтому отличается от DAO
"""


@bookmarks_blueprint.route("/bookmarks")
def bookmarks_page():
    """Вьюшка страницы с добавленными в закладки постами"""
    return render_template("bookmarks.html", posts=Bookmarks().get_bookmarks())


@bookmarks_blueprint.route("/bookmarks/add/<int:pk>")
def bookmarks_add(pk):
    """Вьюшка добавления поста в закладки с редиректом на главную"""
    Bookmarks().append(pk)
    return redirect("/", code=302)


@bookmarks_blueprint.route("/bookmarks/remove/<int:pk>")
def bookmarks_remove(pk):
    """Вьюшка удаления поста из закладок с редиректом на главную"""
    Bookmarks().delete(pk)
    return redirect("/", code=302)
