from flask import Blueprint
from flask import render_template


client: Blueprint = Blueprint("client", __name__)


@client.route("/client")
def show_page():
    # TODO: Implement fetching clients' data.
    # TODO: Implement fetching tickets' data.
    
    clients = [ i for i in range(2) ]
    tickets = [ i for i in range(2) ]
    
    return render_template("client.html", clients=clients, tickets=tickets)


# Actions on client

@client.route("/client-add", methods=[ "POST" ])
def add_client():
    # TODO: Handle received post request.
    
    return render_template("client.html")

@client.route("/client-search", methods=[ "POST" ])
def search_client():
    # TODO: Handle received post request.
    
    return render_template("client.html")

@client.route("/client-delete")
def delete_client():
    # TODO: Handle received get request.
    
    return render_template("client.html")


# Actions on tickets

@client.route("/ticket-add", methods=[ "POST" ])
def add_ticket():
    # TODO: Handle received post request.
    
    return render_template("client.html")

@client.route("/ticket-search", methods=[ "POST" ])
def search_ticket():
    # TODO: Handle received post request.
    
    return render_template("client.html")

@client.route("/ticket-search-by-client-personal-id", methods=[ "POST" ])
def search_ticket_by_client_personal_id():
    # TODO: Handle received post request.
    
    return render_template("client.html")

@client.route("/ticket-search-by-flight-code", methods=[ "POST" ])
def search_ticket_by_flight_code():
    # TODO: Handle received post request.
    
    return render_template("client.html")

@client.route("/ticket-edit", methods=[ "POST" ])
def edit_ticket():
    # TODO: Handle received post request.
    
    return render_template("client.html")

@client.route("/ticket-delete")
def delete_ticket():
    # TODO: Handle received get request.
    
    return render_template("client.html")
