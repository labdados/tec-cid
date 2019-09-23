from flask import Flask
from settings import *
from py2neo import Graph

db = Graph(host=NEO4J_CFG["host"] , port=NEO4J_CFG["port"],
                           user=NEO4J_CFG["user"], password=NEO4J_CFG["passwd"])

def create_app():
    app = Flask(__name__)
    return app