from flask import Flask, render_template
from flask_restful import Api
from resources.hotel import Hotels, Hotel

app = Flask(__name__)
api = Api(app)

@app.route("/")
def index():
    return render_template("index.html")

api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotels/<string:hotel_id>')

if __name__ == '__main__':
    app.run(debug=True)