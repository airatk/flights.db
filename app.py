from flask import Flask
from flask import render_template

from airline import airline
from airport import airport
from client import client


flight_db: Flask = Flask(__name__)

flight_db.register_blueprint(airline)
flight_db.register_blueprint(airport)
flight_db.register_blueprint(client)


@flight_db.route("/")
def show_base_page():
    return render_template("base.html")

@flight_db.route("/drop-database")
def drop_database():
    # TODO: Implement database drop.
    
    return render_template("base.html")
