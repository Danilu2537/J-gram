from flask import Flask
from config import Config
from dao.posts_dao import PostsDAO

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

