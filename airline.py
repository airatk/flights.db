from flask import Blueprint
from flask import render_template


airline: Blueprint = Blueprint("airline", __name__)


@airline.route("/airline")
def show_page():
    # TODO: Implement fetching all available airlines' data.
    # TODO: Implement fetching all available planes' data.
    
    airlines = [ i for i in range(2) ]
    planes = [ i for i in range(2) ]
    
    return render_template("airline.html", airlines=airlines, planes=planes)


# Actions on airline

@airline.route("/airline-add", methods=[ "POST" ])
def add_airline():
    # TODO: Handle received post request.
    
    return render_template("airline.html")

@airline.route("/airline-search", methods=[ "POST" ])
def search_airline():
    # TODO: Handle received post request.
    
    return render_template("airline.html")

@airline.route("/airline-delete")
def delete_airline():
    # TODO: Handle received get request.
    
    return render_template("airline.html")


# Actions on plane

@airline.route("/plane-add", methods=[ "POST" ])
def add_plane():
    # TODO: Handle received post request.
    
    return render_template("airline.html")

@airline.route("/plane-search", methods=[ "POST" ])
def search_plane():
    # TODO: Handle received post request.
    
    return render_template("airline.html")

@airline.route("/plane-search-by-airline-code", methods=[ "POST" ])
def search_plane_by_airline_code():
    # TODO: Handle received post request.
    
    return render_template("airline.html")

@airline.route("/plane-search-by-flight-code", methods=[ "POST" ])
def search_plane_by_flight_code():
    # TODO: Handle received post request.
    
    return render_template("airline.html", methods=[ "POST" ])

@airline.route("/plane-delete")
def delete_plane():
    # TODO: Handle received get request.
    
    return render_template("airline.html")
