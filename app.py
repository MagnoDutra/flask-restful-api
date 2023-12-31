from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.usuario import Usuario, RegistroUsuario

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)


@app.before_first_request
def criar_banco():
    banco.create_all()


api.add_resource(Hoteis, "/hoteis")
api.add_resource(Hotel, "/hoteis/<string:id>")
api.add_resource(Usuario, "/usuarios/<int:id>")
app.add_resource(RegistroUsuario, "/cadastro")

if __name__ == "__main__":
    from sql_alchemy import banco

    banco.init_app(app)
    app.run(debug=True)
