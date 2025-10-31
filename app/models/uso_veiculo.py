from datetime import datetime
from app import db


class UsoVeiculo(db.Model):
    __tablename__ = 'usos_veiculo'

    id = db.Column(db.Integer, primary_key=True)
    motorista_id = db.Column(db.Integer, db.ForeignKey(
        'motoristas.id'), nullable=False)
    veiculo_id = db.Column(db.Integer, db.ForeignKey(
        'veiculos.id'), nullable=False)
    data_inicio = db.Column(db.DateTime, default=datetime.utcnow)
    data_fim = db.Column(db.DateTime)
    observacoes = db.Column(db.String(200))

    veiculo = db.relationship('Veiculo', backref='usos', lazy=True)

    def __repr__(self):
        return f'<UsoVeiculo {self.motorista_id} - {self.veiculo_id}>'
