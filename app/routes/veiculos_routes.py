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
            tipo_veiculo=request.form['vehicle_type'],
            kilometragem=request.form['mileage'],
            status=VeiculoStatus[request.form['status']]
        )
        db.session.add(novo_veiculo)
        db.session.commit()
        flash('Veículo adicionado com sucesso!', 'success')
        return redirect(url_for('veiculos.listar_veiculos'))
    return render_template('veiculos/form.html')

@veiculos_bp.route('/editar/<int:veiculo_id>', methods=['GET', 'POST'])
@login_required 
def editar_veiculo(veiculo_id):
    veiculo = Veiculo.query.get_or_404(veiculo_id)
    if request.method == 'POST':
        # Lógica para editar o veículo
        veiculo.placa = request.form['placa']
        veiculo.marca = request.form['marca']
        veiculo.modelo = request.form['modelo']
        veiculo.ano = request.form['ano']
        veiculo.tipo_veiculo = request.form['tipo_veiculo']
        veiculo.kilometragem = request.form['kilometragem']
        veiculo.status = VeiculoStatus[request.form['status']]
        db.session.commit()
        flash('Veículo editado com sucesso!', 'success')
        return redirect(url_for('veiculos.listar_veiculos'))
    return render_template('veiculos/form.html', vehicle=veiculo)