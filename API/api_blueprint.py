from flask import Blueprint, jsonify
from dao.posts_dao import PostsDAO
import logging

api_blueprint = Blueprint('api_blueprint', __name__)

logger_api = logging.getLogger("api")
logger_api.setLevel(logging.INFO)
file_handler_api = logging.FileHandler("logs/api.log", mode='w')
formatter_api = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler_api.setFormatter(formatter_api)
logger_api.addHandler(file_handler_api)


@api_blueprint.route('/api/posts', methods=['GET'])
def api_posts():
    posts = []
    for post in PostsDAO().get_all():
        posts.append(post.__dict__)
    logger_api.info("Запрос /api/posts")
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_id>', methods=['GET'])
def api_post(post_id):
    logger_api.info(f"Запрос /api/posts/{post_id}")
    return jsonify(PostsDAO().get_by_pk(post_id).__dict__)
