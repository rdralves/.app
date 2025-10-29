from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app import db
from app.models.manutencao import Manutencao
from app.models.veiculos import Veiculo
from datetime import datetime

manutencoes_bp = Blueprint('manutencoes', __name__, url_prefix='/manutencoes')


@manutencoes_bp.route('/')
@login_required
def listar_manutencoes():
    manutencoes = Manutencao.query.order_by(Manutencao.data.desc()).all()
    return render_template('manutencoes/listar.html', manutencoes=manutencoes)


@manutencoes_bp.route('/nova', methods=['GET', 'POST'])
@login_required
def nova_manutencao():
    veiculos = Veiculo.query.all()
    if request.method == 'POST':
        nova = Manutencao(
            veiculo_id=request.form['veiculo_id'],
            tipo=request.form['tipo'],
            descricao=request.form['descricao'],
            data=datetime.strptime(request.form['data'], '%Y-%m-%d'),
            km_realizada=request.form['km_realizada'],
            custo=request.form['custo'],
            proxima_manutencao_km=request.form['proxima_km'],
            proxima_manutencao_data=datetime.strptime(
                request.form['proxima_data'], '%Y-%m-%d') if request.form['proxima_data'] else None
        )
        db.session.add(nova)
        db.session.commit()
        flash('Manutenção registrada com sucesso!', 'success')
        return redirect(url_for('manutencoes.listar_manutencoes'))
    return render_template('manutencoes/form.html', veiculos=veiculos)


@manutencoes_bp.route('/<int:id>')
@login_required
def detalhe_manutencao(id):
    manutencao = Manutencao.query.get_or_404(id)
    return render_template('manutencoes/detalhe.html', manutencao=manutencao)
