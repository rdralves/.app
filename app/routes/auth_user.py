from flask_login import login_user, logout_user, login_required, current_user
from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask_login import LoginManager
from app.models.model import User, db
from werkzeug.security import generate_password_hash, check_password_hash


login_manager = LoginManager()
bp_user = Blueprint('bp_user', __name__, url_prefix='/auth_user')


@bp_user.route('/')
def home():
    return "Bem vindo à página de autenticação/cadastro dos usuários! "


@bp_user.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        print(f"Registrando usuário: {username}, Email: {email}")
        hashed_password = generate_password_hash(
            password, method='pbkdf2:sha256', salt_length=8)

        user = User(name=username, password=hashed_password, email=email)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'Usuário registrado com sucesso!'})
    return render_template('register.html')


@bp_user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return jsonify({'message': 'Login bem-sucedido!'})
        return jsonify({'message': 'Credenciais inválidas!'})

    return render_template('login.html')


@bp_user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('bp_user.login'))
