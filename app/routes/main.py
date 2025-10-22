from flask import Blueprint, render_template
from flask_login import current_user


bp_main = Blueprint('bp_main', __name__)


@bp_main.route('/')
def index():
    return render_template('index.html', user=current_user)
