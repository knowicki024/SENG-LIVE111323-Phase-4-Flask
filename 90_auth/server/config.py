from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from key import secret_k
from flask_cors import CORS


# create instances of Flask class
app = Flask(__name__)#for Flask to know where to look for 
print(secret_k)
app.secret_key = secret_k

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

migrate = Migrate(app, db)

# connect the db to the app
db.init_app(app)

bcrypt = Bcrypt(app)

api = Api(app)

#configure CORS
CORS(app)

