from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

# Configuração do banco de dados
db = SQLAlchemy()

def init_database(app):
    """Inicializar configuração do banco de dados"""
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///daily_diet.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    
    # Inicializar SQLAlchemy com o app
    db.init_app(app)
    
    # Criar tabelas
    with app.app_context():
        db.create_all()
        print('Banco de dados inicializado')