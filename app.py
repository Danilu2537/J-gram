import logging

from flask import Flask, render_template, request

from API.api_blueprint import api_blueprint
from bookmarks.bookmarks_blueprint import bookmarks_blueprint
from bookmarks.utils import Bookmarks
from config import Config
from dao.comments_dao import CommentsDAO
from dao.posts_dao import PostsDAO

"""Настройки логера визуальной части программы"""
logger_app = logging.getLogger("app")
logger_app.setLevel(logging.INFO)
file_handler_app = logging.FileHandler("logs/app.log", mode="w")
formatter_app = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler_app.setFormatter(formatter_app)
logger_app.addHandler(file_handler_app)

app = Flask(__name__)
app.register_blueprint(api_blueprint)  # отдельный блюпринт для API
app.register_blueprint(bookmarks_blueprint)  # отдельный блюпринт для закладок
app.config.from_object(Config)  # настройки хранятся в конфиг файле config.py
app.json.ensure_ascii = False


@app.route("/")
def index_page():
    """
    Вьюшка главной страницы
    """
    logger_app.info("Запрос страницы index")
    return render_template(
        "index.html", posts=PostsDAO().get_all(), count=Bookmarks().get_count()
    )


@app.route("/posts/<int:pk>")
def post_page(pk):
    """
    Вьюшка страницы с отедльным постом
    """
    logger_app.info(f"Запрос поста {pk}")
    comments = CommentsDAO().get_by_post_id(pk)
    return render_template(
        "post.html",
        post=PostsDAO().get_by_pk(pk),
        comments=comments,
        count=len(comments),
    )


@app.route("/search/")
def search_page():
    """
    Вьюшка страницы поиска по ключевому слову
    """
    posts = PostsDAO().search(request.args.get("s"))
    logger_app.info(f"Запрос постов по слову {request.args.get('s')}")
    return render_template("search.html", posts=posts, count=len(posts))


@app.route("/users/<username>")
def user_page(username):
    """
    Вьюшка страницы со всеми постами оперделенног опользователя
    """
    logger_app.info(f"Запрос постов пользователя {username}")
    return render_template("user-feed.html", posts=PostsDAO().get_by_user(username))


@app.route("/tag/<tagname>")
def tag_page(tagname):
    """
    Вьюшка страницы со всеми постами, содержащими определенный тэг
    """
    logger_app.info(f"Запрос постов по тэгу {tagname}")
    return render_template(
        "tag.html", posts=PostsDAO().search(tagname), tagname=tagname
    )


@app.route("/meow")
def meow_page():
    """
    Мяу вьюшка :3
    """
    logger_app.info("Запрос странички meow(")
    return "Такой странички пока нет(", 400


@app.errorhandler(Exception)
def error_page(exception):
    """
    Обработчик ошибок
    """
    logger_app.error(f"Что то случилось: {exception}")
    return f"Сайт сломался( \n" f"{exception}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
