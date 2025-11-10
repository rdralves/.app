from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app import db
from app.models.alerta import Alerta
from app.models.veiculos import Veiculo
from datetime import datetime

alertas_bp = Blueprint('alertas', __name__, url_prefix='/alertas')


@alertas_bp.route('/')
@login_required
def listar_alertas():
    alertas = Alerta.query.order_by(Alerta.data_criacao.desc()).all()
    return render_template('alertas/listar.html', alertas=alertas)


@alertas_bp.route('/adicionar', methods=['GET', 'POST'])
@login_required
def adicionar_alerta():
    veiculos = Veiculo.query.all()

    if request.method == 'POST':
        novo_alerta = Alerta(
            titulo=request.form['titulo'],
            descricao=request.form['descricao'],
            tipo=request.form['tipo'],
            data_disparo=datetime.strptime(
                request.form['data_disparo'], '%Y-%m-%d') if request.form['data_disparo'] else None,
            veiculo_id=request.form.get('veiculo_id') or None
        )
        db.session.add(novo_alerta)
        db.session.commit()
        flash('Alerta criado com sucesso!', 'success')
        return redirect(url_for('alertas.listar_alertas'))

    return render_template('alertas/form.html', veiculos=veiculos)


@alertas_bp.route('/resolver/<int:alerta_id>')
@login_required
def resolver_alerta(alerta_id):
    alerta = Alerta.query.get_or_404(alerta_id)
    alerta.resolvido = True
    db.session.commit()
    flash('Alerta resolvido com sucesso!', 'info')
    return redirect(url_for('alertas.listar_alertas'))
