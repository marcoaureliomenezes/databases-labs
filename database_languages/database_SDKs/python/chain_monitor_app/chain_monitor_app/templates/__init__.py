from flask import Flask, request, jsonify


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chain_monitor.db'
    return app