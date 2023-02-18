from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from modelos import db
from vistas import \
    VistaOrden

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cpp_db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

cors = CORS(app)

api = Api(app)
api.add_resource(VistaOrden, '/orden')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
