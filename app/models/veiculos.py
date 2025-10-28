from model import db
import enum

class VeiculoStatus(enum.Enum):
    ATIVO = "Ativo"
    INATIVO = "Desativado"
    MANUTENCAO = "Manutenção"
    
class Veiculo(db.Model):
    __tablename__ = 'veiculos'
    
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(10), unique=True, nullable=False)
    marca = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    tipo_veiculo = db.Column(db.String(30), nullable=False)
    kilometragem = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum(VeiculoStatus), default=VeiculoStatus.ATIVO, nullable=False)
    
    def __repr__(self):
        return f"<Veiculo {self.placa} - {self.modelo} ({self.ano}) - Status: {self.status.value}>"
    
    