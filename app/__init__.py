from flask import Flask

def create_app():
	app = Flask(__name__)

	from routes.auth_user import bp_user
	app.register_blueprint(bp_user, url_prefix='/auth')
	return app