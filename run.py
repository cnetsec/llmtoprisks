from flask import Flask
from ask import ask_blueprint
from train import train_blueprint
from model import init_db

app = Flask(__name__, template_folder='app/templates')
app.secret_key = 'your_secret_key'

# Registrar blueprints
app.register_blueprint(ask_blueprint, url_prefix='/ask')
app.register_blueprint(train_blueprint, url_prefix='/train')

# Inicializar o banco de dados
with app.app_context():
    init_db()

if __name__ == '__main__':
    app.run(debug=True)

