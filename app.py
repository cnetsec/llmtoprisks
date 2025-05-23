# app.py

import os
from flask import Flask
from ask import ask_blueprint
from train import train_blueprint

app = Flask(__name__, template_folder='app/templates')
app.secret_key = os.urandom(24)  # Chave secreta para a sessão

# Registrar blueprints
app.register_blueprint(ask_blueprint, url_prefix='/ask')
app.register_blueprint(train_blueprint, url_prefix='/train')

# Inicialização do banco de dados (se necessário)
from app import model
model.init_db()

if __name__ == "__main__":
    app.run(debug=True)

