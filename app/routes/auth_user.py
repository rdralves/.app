from flask import Blueprint, render_template, request, jsonify
from app.models.model import User, db

bp_user = Blueprint('bp_user', __name__)


@bp_user.route('/')
def home():
    return "Bem vindo à página de autenticação/cadastro dos usuários!"


@bp_user.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.get('username')
        password = request.get('password')
        email = request.get('email')

        user = User.create_user(name=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        return render_template('register.html')
