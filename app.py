from flask import Flask, render_template, request
from config import Config
from dao.posts_dao import PostsDAO
from dao.comments_dao import CommentsDAO
from API.api_blueprint import api_blueprint
from bookmarks.bookmarks_blueprint import bookmarks_blueprint
from bookmarks.utils import Bookmarks
import logging

logger_app = logging.getLogger("app")
logger_app.setLevel(logging.INFO)
file_handler_app = logging.FileHandler("logs/app.log", mode='w')
formatter_app = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler_app.setFormatter(formatter_app)
logger_app.addHandler(file_handler_app)

app = Flask(__name__)
app.register_blueprint(api_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.config.from_object(Config)
app.json.ensure_ascii = False




@app.route('/')
def index_page():
    logger_app.info("Запрос страницы index")
    return render_template("index.html",
                           posts=PostsDAO().get_all(),
                           count=Bookmarks().get_count())


@app.route('/posts/<int:pk>')
def post_page(pk):
    logger_app.info(f"Запрос поста {pk}")
    comments = CommentsDAO().get_by_post_id(pk)
    return render_template("post.html",
                           post=PostsDAO().get_by_pk(pk),
                           comments=comments,
                           count=len(comments))


@app.route('/search/')
def search_page():
    posts = PostsDAO().search(request.args.get('s'))
    logger_app.info(f"Запрос постов по слову {request.args.get('s')}")
    return render_template("search.html",
                           posts=posts,
                           count=len(posts))


@app.route('/users/<username>')
def user_page(username):
    logger_app.info(f"Запрос постов пользователя {username}")
    return render_template('user-feed.html',
                           posts=PostsDAO().get_by_user(username))


@app.route('/tag/<tagname>')
def tag_page(tagname):
    logger_app.info(f"Запрос постов по тэгу {tagname}")
    return render_template('tag.html',
                           posts=PostsDAO().search(tagname),
                           tagname=tagname)


@app.route('/meow')
def meow_page():
    logger_app.info("Запрос странички meow(")
    return "Такой странички пока нет(", 400


@app.errorhandler(Exception)
def error_page(exception):
    logger_app.error(f"Что то случилось: {exception}")
    return f"Сайт сломался( \n" \
           f"{exception}", 500


if __name__ == '__main__':
    app.run()
