from flask import Blueprint, request, jsonify

bp_user = Blueprint('bp_user', __name__)

@bp_user.route('/')
def home():
    return "Bem vindo à página de autenticação/cadastro dos usuários!"

