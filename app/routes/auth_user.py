from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from app.models.model import User, db

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

        user = User(name=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'Usuário registrado com sucesso!'})
    return render_template('register.html')

@bp_user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email, password=password).first()
        if user:
            return jsonify({'message': 'Login bem-sucedido!'})
        return jsonify({'message': 'Credenciais inválidas!'})
    
    return render_template('login.html')


