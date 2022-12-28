from flask import Blueprint, render_template, redirect
from bookmarks.utils import Bookmarks

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__)


@bookmarks_blueprint.route('/bookmarks')
def bookmarks_page():
    return render_template('bookmarks.html',
                           posts=Bookmarks().get_bookmarks())


@bookmarks_blueprint.route('/bookmarks/add/<int:pk>')
def bookmarks_add(pk):
    Bookmarks().append(pk)
    return redirect('/', code=302)


@bookmarks_blueprint.route('/bookmarks/remove/<int:pk>')
def bookmarks_remove(pk):
    Bookmarks().delete(pk)
    return redirect('/', code=302)
