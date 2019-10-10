from flask_script import Manager
from app.main import create_app
from app import blueprint

app = create_app()
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

@manager.command
def run():
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    manager.run()
