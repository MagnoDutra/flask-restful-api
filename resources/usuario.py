from flask_restful import Resource
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
