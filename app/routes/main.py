from flask import Blueprint, abort, render_template
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound


bp_main = Blueprint('bp_main', __name__)


@bp_main.route('/')
def index():
    return render_template('index.html', user=current_user)


@bp_main.route('/dashboard')
@login_required
def dashboard():
    try:
        return render_template('dashboard.html')
    except TemplateNotFound:
        abort(404)
