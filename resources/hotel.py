from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
    {
        "id": "alpha",
        "nome": "Alpha Hotel",
        "estrelas": 4.3,
        "diaria": 420.34,
        "cidade": "Rio de Janeiro",
    },
    {
        "id": "bravo",
        "nome": "Bravo Hotel",
        "estrelas": 4.5,
        "diaria": 380.90,
        "cidade": "Curitiba",
    },
    {
        "id": "charlie",
        "nome": "Charlie Hotel",
        "estrelas": 3.9,
        "diaria": 320.20,
        "cidade": "Curitiba",
    },
]


class Hoteis(Resource):
    def get(self):
        return {"hoteis": [hotel.json() for hotel in HotelModel.query.all()]}


class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome")
    argumentos.add_argument("estrelas")
    argumentos.add_argument("diaria")
    argumentos.add_argument("cidade")

    def get(self, id):
        hotel = HotelModel.find_hotel(id)
        if hotel:
            return hotel.json(), 200
        return {"message": "hotel not found."}, 404

    def post(self, id):
        if HotelModel.find_hotel(id):
            return {"message": f"Hotel id '{id}' already exists."}, 400

        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(id, **dados)
        hotel.save_hotel()
        return hotel.json(), 201

    def put(self, id):
        dados = Hotel.argumentos.parse_args()
        hotel_encontrado = HotelModel.find_hotel(id)

        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200

        hotel = HotelModel(id, **dados)
        hotel.save()
        return hotel.json(), 201

    def delete(self, id):
        hotel = HotelModel.find_hotel(id)
        if hotel:
            hotel.delete_hotel()
            return {"message": "Hotel deleted."}
        return {"message": "Not a valid hotel."}, 404
