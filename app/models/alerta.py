from datetime import datetime
from app import db


class Alerta(db.Model):
    __tablename__ = 'alertas'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.String(255))
    tipo = db.Column(db.String(50))  # Ex: "MANUTENÇÃO", "DOCUMENTO"
    data_alerta = db.Column(db.DateTime, default=datetime.utcnow)
    resolvido = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Alerta {self.titulo}>'
