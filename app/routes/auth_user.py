from sqlite3 import IntegrityError
from flask_login import login_user, logout_user, login_required, current_user
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
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

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash('Erro: Nome de usuário ou email já existe.', 'error')
            return render_template('register.html')
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao registrar usuário: Usuário já existe.', 'error')
            return render_template('register.html')
        flash('Usuário registrado com sucesso!', 'success')
        return redirect(url_for('bp_user.login'))
    return render_template('register.html')


@bp_user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                login_user(user)
                flash('Login realizado com sucesso!', 'success')
                return redirect(url_for('bp_main.dashboard')) # Adicione a rota para a página do seu sistema aqui!
        except Exception as e:
            flash(f'Erro ao fazer login: {str(e)}', 'error')

    return render_template('login.html')


@bp_user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('bp_user.login'))



