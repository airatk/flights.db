from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from db import execute


client: Blueprint = Blueprint("client", __name__)


@client.route("/client")
def show_page():
    clients = execute(query="SELECT * FROM client;", database="flights_db")
    tickets = execute(query="SELECT * FROM ticket;", database="flights_db")
    
    return render_template("client.html", clients=clients, tickets=tickets)


# Actions on client

@client.route("/client-add", methods=[ "POST" ])
def add_client():
    execute(query="""
        INSERT INTO client VALUES (
            '{personal_id}',
            '{name}',
            '{birth_date}',
            '{phone}',
            '{email}'
        );
    """.format(
        personal_id=request.form["personal-id"],
        name=request.form["name"],
        birth_date=request.form["birth-date"],
        phone=request.form["phone"],
        email=request.form["email"]
    ), database="flights_db")
    
    return redirect(url_for("client.show_page"))

@client.route("/client-search", methods=[ "POST" ])
def search_client():
    sorting: str = request.form["sorting"]
    sql_sort_query: str = ""
    
    if sorting != "no-sort":
        if "name" in sorting:
            sql_sort_query += " ORDER BY name"
        
        if "ascending" in sorting:
            sql_sort_query += " ASC"
        elif "descending" in sorting:
            sql_sort_query += " DESC"
    
    clients = execute(query="""
        SELECT * FROM client
        WHERE personal_id ILIKE '%{search_query}%' OR
            name ILIKE '%{search_query}%'
        {sort_query};
    """.format(
        search_query=request.form["search_query"],
        sort_query=sql_sort_query
    ), database="flights_db")
    
    return render_template("client.html", clients=clients)

@client.route("/client-delete-<personal_id>")
def delete_client(personal_id: str):
    execute(query="DELETE FROM client WHERE personal_id = '{personal_id}';".format(personal_id=personal_id), database="flights_db")
    
    return redirect(url_for("client.show_page"))


# Actions on client & on tickets

@client.route("/client-ticket-search", methods=[ "POST" ])
def search_client_ticket():
    clients_tickets = execute(query="""
        SELECT * FROM client
        JOIN ticket ON client.personal_id = ticket.personal_id
        WHERE client.personal_id ILIKE '%{search_query}%' OR
            client.name ILIKE '%{search_query}%';
    """.format(search_query=request.form["search_query"]), database="flights_db")
    
    clients = []
    tickets = []
    
    for client_ticket in clients_tickets:
        clients.append(client_ticket[:5])
        tickets.append(client_ticket[5:])
    
    return render_template("client.html", clients=clients, tickets=tickets)


# Actions on tickets

@client.route("/ticket-add", methods=[ "POST" ])
def add_ticket():
    execute(query="""
        INSERT INTO ticket VALUES (
            '{ticket_code}',
            '{personal_id}',
            '{flight_code}',
            '{status}'
        );
    """.format(
        ticket_code=request.form["ticket-code"],
        personal_id=request.form["personal-id"],
        flight_code=request.form["flight-code"],
        status=request.form["status"]
    ), database="flights_db")
    
    return redirect(url_for("client.show_page"))

@client.route("/ticket-search", methods=[ "POST" ])
def search_ticket():
    sorting: str = request.form["sorting"]
    sql_sort_query: str = ""
    
    if sorting != "no-sort":
        if "ticket-code" in sorting:
            sql_sort_query += " ORDER BY ticket_code"
        elif "flight-code" in sorting:
            sql_sort_query += " ORDER BY flight_code"
        
        if "ascending" in sorting:
            sql_sort_query += " ASC"
        elif "descending" in sorting:
            sql_sort_query += " DESC"
    
    tickets = execute(query="""
        SELECT * FROM ticket
        WHERE ticket_code ILIKE '%{search_query}%'
        {sort_query};
    """.format(
        search_query=request.form["search_query"],
        sort_query=sql_sort_query
    ), database="flights_db")
    
    return render_template("client.html", tickets=tickets)

@client.route("/ticket-edit", methods=[ "POST" ])
def edit_ticket():
    execute(query="UPDATE ticket SET status = '{status}' WHERE ticket_code = '{ticket_code}';".format(
        status=request.form["status"],
        ticket_code=request.form["ticket-code"]
    ), database="flights_db")
    
    return redirect(url_for("client.show_page"))

@client.route("/ticket-delete-<ticket_code>")
def delete_ticket(ticket_code: str):
    execute(query="DELETE FROM ticket WHERE ticket_code = '{ticket_code}';".format(ticket_code=ticket_code), database="flights_db")
    
    return redirect(url_for("client.show_page"))
