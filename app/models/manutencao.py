from datetime import datetime
from app import db


class Manutencao(db.Model):
    __tablename__ = 'manutencoes'

    id = db.Column(db.Integer, primary_key=True)
    veiculo_id = db.Column(db.Integer, db.ForeignKey(
        'veiculos.id'), nullable=False)
    tipo = db.Column(db.String(50))  # Preventiva / Corretiva
    descricao = db.Column(db.String(200))
    data = db.Column(db.Date, default=datetime.utcnow)
    km_realizada = db.Column(db.Integer)
    custo = db.Column(db.Float)
    proxima_manutencao_km = db.Column(db.Integer)
    proxima_manutencao_data = db.Column(db.Date)

    veiculo = db.relationship('Veiculo', backref='manutencoes', lazy=True)

    def __repr__(self):
        return f'<Manutenção {self.tipo} - {self.veiculo.placa}>'


