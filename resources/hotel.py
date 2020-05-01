from flask_restful import Resource

hotels = [
    {
        'hotel_id': 'alpha',
        'name': 'alpha Hotel',
        'stars': 4.3,
        'price': 420
    },
    {
        'hotel_id': 'bravo',
        'name': 'Bravo Hotel',
        'stars': 5,
        'price': 220
    },
    {
        'hotel_id': 'charlie',
        'name': 'Charlie Hotel',
        'stars': 3,
        'price': 550
    }
]

class Hotels(Resource):
    def get(self):
       return { 'hotels': hotels}

class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hotels:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return { 'message': 'Hotel not found'}, 404

    def post(self, hotel_id):
        pass

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass
