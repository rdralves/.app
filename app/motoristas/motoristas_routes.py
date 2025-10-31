from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app import db
from app.models.motorista import Motorista
from app.models.veiculos import Veiculo
from app.models.uso_veiculo import UsoVeiculo
from datetime import datetime

motoristas_bp = Blueprint('motoristas', __name__, url_prefix='/motoristas')


@motoristas_bp.route('/')
@login_required
def listar_motoristas():
    motoristas = Motorista.query.order_by(Motorista.nome).all()
    return render_template('motoristas/listar.html', motoristas=motoristas)


@motoristas_bp.route('/adicionar', methods=['GET', 'POST'])
@login_required
def adicionar_motorista():
    if request.method == 'POST':
        motorista = Motorista(
            nome=request.form['nome'],
            cpf=request.form['cpf'],
            cnh=request.form['cnh'],
            categoria_cnh=request.form['categoria_cnh'],
            telefone=request.form['telefone']
        )
        db.session.add(motorista)
        db.session.commit()
        flash('Motorista adicionado com sucesso!', 'success')
        return redirect(url_for('motoristas.listar_motoristas'))
    return render_template('motoristas/form.html')


@motoristas_bp.route('/<int:id>')
@login_required
def detalhes_motorista(id):
    motorista = Motorista.query.get_or_404(id)
    return render_template('motoristas/detalhes.html', motorista=motorista)


@motoristas_bp.route('/atribuir', methods=['GET', 'POST'])
@login_required
def atribuir_veiculo():
    motoristas = Motorista.query.filter_by(ativo=True).all()
    veiculos = Veiculo.query.filter_by(status='ATIVO').all()
    if request.method == 'POST':
        uso = UsoVeiculo(
            motorista_id=request.form['motorista_id'],
            veiculo_id=request.form['veiculo_id'],
            data_inicio=datetime.strptime(
                request.form['data_inicio'], '%Y-%m-%d'),
            observacoes=request.form.get('observacoes', '')
        )
        db.session.add(uso)
        db.session.commit()
        flash('Veículo atribuído ao motorista!', 'success')
        return redirect(url_for('motoristas.listar_motoristas'))
    return render_template('motoristas/atribuir.html', motoristas=motoristas, veiculos=veiculos)
