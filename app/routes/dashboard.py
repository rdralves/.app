from flask import Blueprint, render_template, jsonify
from flask_login import login_required
from app.models.veiculos import Veiculo
from app.models.motorista import Motorista
from app.models.manutencao import Manutencao
from app.models.uso_veiculo import UsoVeiculo
from app import db
from sqlalchemy import func

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@dashboard_bp.route('/')
@login_required
def index():
    total_veiculos = Veiculo.query.count()
    motoristas_ativos = Motorista.query.filter_by(ativo=True).count()
    manutencoes_pendentes = Manutencao.query.filter(
        Manutencao.status == 'PENDENTE').count()
    usos_ativos = UsoVeiculo.query.filter(UsoVeiculo.data_fim == None).count()

    # Top 5 veículos mais usados
    top_veiculos = (
        db.session.query(Veiculo.modelo, func.count(
            UsoVeiculo.id).label('vezes_usado'))
        .join(UsoVeiculo)
        .group_by(Veiculo.id)
        .order_by(func.count(UsoVeiculo.id).desc())
        .limit(5)
        .all()
    )

    top_veiculos_labels = [v[0] for v in top_veiculos]
    top_veiculos_data = [v[1] for v in top_veiculos]

    return render_template(
        'dashboard/index.html',
        total_veiculos=total_veiculos,
        motoristas_ativos=motoristas_ativos,
        manutencoes_pendentes=manutencoes_pendentes,
        usos_ativos=usos_ativos,
        top_veiculos_labels=top_veiculos_labels,
        top_veiculos_data=top_veiculos_data
    )
