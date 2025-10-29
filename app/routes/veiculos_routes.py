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

@veiculos_bp.route('/adicionar', methods=['GET', 'POST'])
@login_required
def adicionar_veiculo():
    if request.method == 'POST':
        # Lógica para adicionar um novo veículo
        novo_veiculo = Veiculo(
            placa=request.form['plate'],
            marca=request.form['brand'],
            modelo=request.form['model'],
            ano=request.form['year'],
            tipo=request.form['vehicle_type'],
            km_atual=request.form['mileage'],
            status=VeiculoStatus[request.form['status']]
        )
        db.session.add(novo_veiculo)
        db.session.commit()
        flash('Veículo adicionado com sucesso!', 'success')
        return redirect(url_for('veiculos.listar_veiculos'))
    return render_template('veiculos/form.html')