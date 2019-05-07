from flask import Flask
from app.config import settings
# import blue prints
from blueprints.user import user

app=Flask(__name__,instance_relative_config=True,static_folder="image")
app.config.from_object(settings)

# configure blueprints
app.register_blueprint(user)

print(app.config['DEBUG'])

def create_app():
    app.run()