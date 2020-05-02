from flask_restful import Resource, reqparse

hotels = [
    {
        'hotel_id': 'alpha',
        'name': 'alpha Hotel',
        'stars': 4.3,
        'price': 420,
        'city': 'Floripa'
    },
    {
        'hotel_id': 'bravo',
        'name': 'Bravo Hotel',
        'stars': 5,
        'price': 220,
        'city': 'Floripa'
    },
    {
        'hotel_id': 'charlie',
        'name': 'Charlie Hotel',
        'stars': 3,
        'price': 550,
        'city': 'Floripa'
    }
]

class Hotels(Resource):
    def get(self):
       return { 'hotels': hotels}

class Hotel(Resource):
    args = reqparse.RequestParser()
    args.add_argument('name')
    args.add_argument('stars')
    args.add_argument('price')
    args.add_argument('city')

    def find_hotel(hotel_id):
        for hotel in hotels:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):

        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return { 'message': 'Hotel not found'}, 404

    def post(self, hotel_id):

        data = Hotel.args.parse_args()

        new_hotel = { 'hotel_id': hotel_id, **data}

        hotels.append(new_hotel)
        return new_hotel, 200

    def put(self, hotel_id):

        data = Hotel.args.parse_args()
        new_hotel = { 'hotel_id': hotel_id, **data}

        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(new_hotel)
            return new_hotel, 200
        hotels.append(new_hotel)
        return new_hotel, 201

    def delete(self, hotel_id):
        pass