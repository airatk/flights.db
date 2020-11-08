from flask import Flask
from flask import render_template


app: Flask = Flask(import_name=__name__)


@app.route("/")
def show_base_page():
    return render_template("base.html")


@app.route("/airline")
def show_airline_page():
    # TODO: Implement fetching all available airlines data.
    # TODO: Implement fetching all available planes data.
    
    airlines = [ i for i in range(2) ]
    planes = [ i for i in range(2) ]
    
    return render_template("airline.html", airlines=airlines, planes=planes)

@app.route("/airline")
def response_to_form_on_airline_page():
    # TODO: Handle received post requests.
    
    return render_template("airline.html")


@app.route("/airport")
def show_airport_page():
    # TODO: Implement fetching airports data.
    # TODO: Implement fetching flights data.
    
    airports = [ i for i in range(2) ]
    flights = [ i for i in range(2) ]
    
    return render_template("airport.html", airports=airports, flights=flights)

@app.route("/airport")
def response_to_form_on_airport_page():
    # TODO: Handle received post requests.
    
    return render_template("airport.html")


@app.route("/client")
def show_client_page():
    # TODO: Implement fetching clients data.
    # TODO: Implement fetching tickets data.
    
    clients = [ i for i in range(2) ]
    tickets = [ i for i in range(2) ]
    
    return render_template("client.html", clients=clients, tickets=tickets)

@app.route("/client")
def response_to_form_on_client_page():
    # TODO: Handle received post requests.
    
    return render_template("client.html")
