from datetime import datetime
from app import db

class Alerta(db.Model):
    __tablename__ = 'alertas'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    tipo = db.Column(db.String(50), nullable=False)  # 'MANUTENÇÃO', 'DOCUMENTO', etc.
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)  
    data_disparo = db.Column(db.DateTime, nullable=True)
    resolvido = db.Column(db.Boolean, default=False)
    veiculo_id = db.Column(db.Integer, db.ForeignKey('veiculos.id'), nullable=True)

    veiculo = db.relationship("Veiculo", backref="alertas")
