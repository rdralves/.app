from flask import Flask, app
from flask_login import LoginManager
from .models.model import db, User
from .models.veiculos import Veiculo
from flask_migrate import Migrate
from dotenv import load_dotenv
import os 

def create_app():
    load_dotenv()
    app = Flask(__name__)
    
    # Configurações vindas do .env
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "chave-padrao")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        "SQLALCHEMY_DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'bp_user.login'  # Endpoint de login

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints/endpoints
    from app.routes.main import bp_main
    from app.routes.auth_user import bp_user
    from app.routes.veiculos_routes import veiculos_bp
    from app.manutencoes.routes import manutencoes_bp
    from app.motoristas.motoristas_routes import motoristas_bp
    from app.routes.viagem import viagens_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.alertas import alertas_bp

    app.register_blueprint(alertas_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(viagens_bp)
    app.register_blueprint(motoristas_bp)
    app.register_blueprint(manutencoes_bp)
    app.register_blueprint(bp_main)
    app.register_blueprint(bp_user)
    app.register_blueprint(veiculos_bp)

    # from app.tasks.scheduler import iniciar_scheduler #temporariamente suspenso, para atualização.

    # iniciar_scheduler(app)

# Criaçao do banco de dados
    with app.app_context():
        db.create_all()
    return app
