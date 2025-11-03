from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from datetime import datetime
from app import db
from app.models.viagem import Viagem
from app.models.motorista import Motorista
from app.models.veiculos import Veiculo

viagens_bp = Blueprint('viagens', __name__, url_prefix='/viagens')


@viagens_bp.route('/')
@login_required
def listar_viagens():
    viagens = Viagem.query.order_by(Viagem.data_saida.desc()).all()
    return render_template('viagens/listar.html', viagens=viagens)


@viagens_bp.route('/nova', methods=['GET', 'POST'])
@login_required
def nova_viagem():
    motoristas = Motorista.query.filter_by(ativo=True).all()
    veiculos = Veiculo.query.filter_by(status='ATIVO').all()
    if request.method == 'POST':
        nova = Viagem(
            motorista_id=request.form['motorista_id'],
            veiculo_id=request.form['veiculo_id'],
            origem=request.form['origem'],
            destino=request.form['destino'],
            data_saida=datetime.strptime(
                request.form['data_saida'], '%Y-%m-%dT%H:%M'),
            data_retorno_prevista=datetime.strptime(
                request.form['data_retorno_prevista'], '%Y-%m-%dT%H:%M') if request.form['data_retorno_prevista'] else None,
            km_saida=request.form['km_saida'],
            observacoes=request.form['observacoes'],
            status='PENDENTE'
        )
        db.session.add(nova)
        db.session.commit()
        flash('Viagem agendada com sucesso!', 'success')
        return redirect(url_for('viagens.listar_viagens'))
    return render_template('viagens/form.html', motoristas=motoristas, veiculos=veiculos)


@viagens_bp.route('/<int:id>')
@login_required
def detalhes_viagem(id):
    viagem = Viagem.query.get_or_404(id)
    return render_template('viagens/detalhes.html', viagem=viagem)


@viagens_bp.route('/iniciar/<int:id>')
@login_required
def iniciar_viagem(id):
    viagem = Viagem.query.get_or_404(id)
    viagem.status = 'EM_ANDAMENTO'
    db.session.commit()
    flash('Viagem iniciada!', 'info')
    return redirect(url_for('viagens.listar_viagens'))


@viagens_bp.route('/finalizar/<int:id>', methods=['POST'])
@login_required
def finalizar_viagem(id):
    viagem = Viagem.query.get_or_404(id)
    viagem.status = 'CONCLUIDA'
    viagem.km_retorno = request.form['km_retorno']
    viagem.data_retorno_real = datetime.strptime(
        request.form['data_retorno_real'], '%Y-%m-%dT%H:%M')
    db.session.commit()
    flash('Viagem finalizada com sucesso!', 'success')
    return redirect(url_for('viagens.listar_viagens'))
