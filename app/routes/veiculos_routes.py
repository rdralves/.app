from flask import Blueprint, request, flash, redirect, url_for, render_template
from flask_login import login_required
from app.models.veiculos import Veiculo, VeiculoStatus
from app import db

veiculos_bp = Blueprint('veiculos', __name__, url_prefix='/veiculos')

@veiculos_bp.route('/')
@login_required
def listar_veiculos():
    veiculos = Veiculo.query.all()
    return render_template('veiculos/listar.html', veiculos=veiculos)