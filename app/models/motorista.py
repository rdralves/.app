from datetime import datetime
from app import db


class Motorista(db.Model):
    __tablename__ = 'motoristas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    cnh = db.Column(db.String(20), unique=True, nullable=False)
    categoria_cnh = db.Column(db.String(2))
    telefone = db.Column(db.String(20))
    ativo = db.Column(db.Boolean, default=True)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    usos = db.relationship('UsoVeiculo', backref='motorista', lazy=True)

    def __repr__(self):
        return f'<Motorista {self.nome}>'
