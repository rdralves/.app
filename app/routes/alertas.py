from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from app.models.alerta import Alerta
from app import db

alertas_bp = Blueprint('alertas', __name__, url_prefix='/alertas')


@alertas_bp.route('/')
@login_required
def listar_alertas():
    alertas = Alerta.query.order_by(Alerta.data_alerta.desc()).all()
    return render_template('alertas/listar.html', alertas=alertas)


@alertas_bp.route('/resolver/<int:id>')
@login_required
def resolver_alerta(id):
    alerta = Alerta.query.get_or_404(id)
    alerta.resolvido = True
    db.session.commit()
    flash('Alerta marcado como resolvido!', 'success')
    return redirect(url_for('alertas.listar_alertas'))
