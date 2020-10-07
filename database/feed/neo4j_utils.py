import sys
import os
from decouple import config
from py2neo import Graph


class Neo4jUtils():

    def __init__(self):
        self.user = sys.argv[1] if len(sys.argv) > 1 else config('NEO4J_USER', default='neo4j')
        self.password = sys.argv[2] if len(sys.argv) > 2 else config('NEO4J_PASSWORD', default='password')
        self.neo4j = Graph("localhost", user=self.user, password=self.password)

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password

    def get_neo4j(self):
        return self.neo4j

    def get_query_response(self, query):
        return self.neo4j.run(query).data()