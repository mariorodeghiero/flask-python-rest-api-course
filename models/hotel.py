from sql_alchemy import db
class HotelModel(db.Model):
    __tablename__ = 'hotels'

    hotel_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(80))
    stars = db.Column(db.Float(precision=1))
    price = db.Column(db.Float(precision=2))
    city = db.Column(db.String(40))

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