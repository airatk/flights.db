from flask import Blueprint
from flask import render_template


airport: Blueprint = Blueprint("airport", __name__)


@airport.route("/airport")
def show_page():
    # TODO: Implement fetching airports' data.
    # TODO: Implement fetching flights' data.
    
    airports = [ i for i in range(2) ]
    flights = [ i for i in range(2) ]
    
    return render_template("airport.html", airports=airports, flights=flights)


# Action on airport

@airport.route("/airport-add", methods=[ "POST" ])
def add_airport():
    # TODO: Handle received post request.
    
    return render_template("airport.html")

@airport.route("/airport-search", methods=[ "POST" ])
def search_airport():
    # TODO: Handle received post request.
    
    return render_template("airport.html")

@airport.route("/airport-delete")
def delete_airport():
    # TODO: Handle received get request.
    
    return render_template("airport.html")


# Actions on flights

@airport.route("/flight-add", methods=[ "POST" ])
def add_flight():
    # TODO: Handle received post request.
    
    return render_template("airport.html")

@airport.route("/flight-search", methods=[ "POST" ])
def search_flight():
    # TODO: Handle received post request.
    
    return render_template("airport.html")

@airport.route("/flight-search-by-airport-code", methods=[ "POST" ])
def search_flight_by_airport_code():
    # TODO: Handle received post request.
    
    return render_template("airport.html")

@airport.route("/flight-edit", methods=[ "POST" ])
def edit_flight():
    # TODO: Handle received post request.
    
    return render_template("airport.html")

@airport.route("/flight-delete")
def delete_flight():
    # TODO: Handle received get requests.
    
    return render_template("airport.html")
