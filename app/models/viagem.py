from datetime import datetime
from app import db

class Viagem(db.Model):
    __tablename__ = 'viagens'

    id = db.Column(db.Integer, primary_key=True)
    motorista_id = db.Column(db.Integer, db.ForeignKey('motoristas.id'), nullable=False)
    veiculo_id = db.Column(db.Integer, db.ForeignKey('veiculos.id'), nullable=False)
    origem = db.Column(db.String(100), nullable=False)
    destino = db.Column(db.String(100), nullable=False)
    data_saida = db.Column(db.DateTime, nullable=False)
    data_retorno_prevista = db.Column(db.DateTime)
    data_retorno_real = db.Column(db.DateTime)
    km_saida = db.Column(db.Integer)
    km_retorno = db.Column(db.Integer)
    observacoes = db.Column(db.String(255))
    status = db.Column(db.String(20), default='PENDENTE')  # PENDENTE, EM_ANDAMENTO, CONCLUIDA, CANCELADA

    motorista = db.relationship('Motorista', backref='viagens', lazy=True)
    veiculo = db.relationship('Veiculo', backref='viagens', lazy=True)

    def __repr__(self):
        return f'<Viagem {self.id} - {self.origem} → {self.destino}>'
