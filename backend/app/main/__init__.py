from flask import Flask
from flask_cors import CORS
from settings import *
from py2neo import Graph

db = Graph(host=NEO4J_CFG["host"] , port=NEO4J_CFG["port"],
           user=NEO4J_CFG["user"], password=NEO4J_CFG["passwd"])

def create_app():
    app = Flask(__name__)
    CORS(app)
    return app