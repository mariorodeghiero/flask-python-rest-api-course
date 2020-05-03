
class HotelModel:
    def __init__(self, hotel_id, name, stars, price, city):
        self.hotel_id = hotel_id
        self.name = name
        self.stars = stars
        self.price = price
        self.city = city

    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'name': self.name,
            'stars': self.stars,
            'price': self.price,
            'city': self.city
        }