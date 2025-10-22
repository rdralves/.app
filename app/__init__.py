from flask import Flask
from flask_login import LoginManager
from .models.model import db,User


def create_app():
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
	app.config['SECRET_KEY'] = 'your_secret_key'

	db.init_app(app)

	login_manager = LoginManager()
	login_manager.init_app(app)
	login_manager.login_view = 'bp_user.login'  # Endpoint de login

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))


    # Register blueprints/endpoints
	from app.routes.auth_user import bp_user
	app.register_blueprint(bp_user)

	# Criaçao do banco de dados    
	with app.app_context():
		db.create_all()
	return app



