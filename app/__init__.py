from flask import Flask, app
from .models.model import db


def create_app():
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
	db.init_app(app)

    # Register blueprints/endpoints
	from app.routes.auth_user import bp_user
	app.register_blueprint(bp_user)

	# Criaçao do banco de dados    
	with app.app_context():
		db.create_all()
	return app



