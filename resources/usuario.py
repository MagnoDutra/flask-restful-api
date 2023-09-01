from flask_restful import Resource, reqparse
from models.usuario import UsuarioModel


class Usuario(Resource):
    def get(self, id):
        usuario = UsuarioModel.find_user(id)
        if usuario:
            return usuario.json(), 200
        return {"message": "user not found"}

    def delete(self, id):
        usuario = UsuarioModel.find_user(id)
        if usuario:
            try:
                usuario.delete_user()
            except:
                return {"message": "An error ocurred trying to delete user"}, 500
            return {"message": "User deleted"}, 200
        return {"message": "Not a valid user id"}, 404


class RegistroUsuario(Resource):
    def post(self):
        atributos = reqparse.RequestParser()
        atributos.add_arguments(
            "login",
            type=str,
            required=True,
            help="The field 'login' cannot be left blank.",
        )
        atributos.add_arguments(
            "senha",
            type=str,
            required=True,
            help="The field 'senha' cannot be left blank.",
        )
        dados = atributos.parse_args()

        if UsuarioModel.find_user_by_login(dados["login"]):
            return {"message": f"The login '{dados['login']}' already exists."}, 400

        user = UsuarioModel(**dados)
        user.save_user
        return {"message": "User created successfully!"}, 201
