import os

from flask import Flask

def create_app(test_config=None):
    #create and configure the app
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path,'flaskr.sqlite'),
    )
    if test_config is None:
       # load the instance config ,if it 