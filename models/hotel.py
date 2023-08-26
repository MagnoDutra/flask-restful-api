from sql_alchemy import banco


class HotelModel(banco.Model):
    __tablename__ = "hoteis"
    id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision=1))
    diaria = banco.Column(banco.Float(precision=2))
    cidade = banco.Column(banco.String(40))

    def __init__(self, id, nome, estrelas, diaria, cidade):
        self.id = id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "estrelas": self.estrelas,
            "diaria": self.diaria,
            "cidade": self.cidade,
        }

    @classmethod
    def find_hotel(cls, id):
        hotel = cls.query.filter_by(id=id).first()
        if hotel:
            return hotel
        return None

    def save_hotel(self):
        banco.session.add(self)
        banco.session.commit()
