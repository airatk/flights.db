from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from db import execute


airport: Blueprint = Blueprint("airport", __name__)


@airport.route("/airport")
def show_page():
    airports = execute(query="SELECT * FROM airport;", database="flights_db")
    flights = execute(query="SELECT * FROM flight;", database="flights_db")
    
    return render_template("airport.html", airports=airports, flights=flights)


# Action on airport

@airport.route("/airport-add", methods=[ "POST" ])
def add_airport():
    execute(query="""
        INSERT INTO airport VALUES (
            '{airport_code}',
            '{name}',
            '{city}',
            '{country}',
            '{longitude}',
            '{latitude}',
            '{timezone}'
        );
    """.format(
        airport_code=request.form["airport-code"],
        name=request.form["name"],
        city=request.form["city"],
        country=request.form["country"],
        longitude=request.form["longitude"],
        latitude=request.form["latitude"],
        timezone=request.form["timezone"]
    ), database="flights_db")
    
    return redirect(url_for("airport.show_page"))

@airport.route("/airport-search", methods=[ "POST" ])
def search_airport():
    sorting: str = request.form["sorting"]
    sql_sort_query: str = ""
    
    if sorting != "no-sort":
        if "airport-code" in sorting:
            sql_sort_query += " ORDER BY airport_code"
        elif "name" in sorting:
            sql_sort_query += " ORDER BY name"
        elif "city" in sorting:
            sql_sort_query += " ORDER BY city"
        elif "country" in sorting:
            sql_sort_query += " ORDER BY country"
        
        if "ascending" in sorting:
            sql_sort_query += " ASC"
        elif "descending" in sorting:
            sql_sort_query += " DESC"
    
    airports = execute(query="""
        SELECT * FROM airport
        WHERE airport_code ILIKE '%{search_query}%' OR
            name ILIKE '%{search_query}%' OR
            city ILIKE '%{search_query}%' OR
            country ILIKE '%{search_query}%'
        {sort_query};
    """.format(
        search_query=request.form["search_query"],
        sort_query=sql_sort_query
    ), database="flights_db")
    
    return render_template("airport.html", airports=airports)

@airport.route("/airport-delete-<airport_code>")
def delete_airport(airport_code: str):
    execute(query="DELETE FROM airport WHERE airport_code = '{airport_code}';".format(airport_code=airport_code), database="flights_db")
    
    return redirect(url_for("airport.show_page"))


# Actions on flights

@airport.route("/flight-add", methods=[ "POST" ])
def add_flight():
    execute(query="""
        INSERT INTO flight VALUES (
            '{flight_code}',
            '{departure_airport_code}',
            '{arrival_airport_code}',
            '{departure_date}',
            '{arrival_date}',
            '{departure_time}',
            '{arrival_time}',
            '{time}',
            {miles},
            '{seat_class}',
            {seat_number},
            {price}
        );
    """.format(
        flight_code=request.form["flight_code"],
        departure_airport_code=request.form["departure-airport-code"],
        arrival_airport_code=request.form["arrival-airport-code"],
        departure_date=request.form["departure-date"],
        arrival_date=request.form["arrival-date"],
        departure_time=request.form["departure-time"],
        arrival_time=request.form["arrival-time"],
        time=request.form["time"],
        miles=request.form["miles"],
        seat_class=request.form["seat-class"],
        seat_number=request.form["seat-number"],
        price=request.form["price"]
    ), database="flights_db")
    
    return redirect(url_for("airport.show_page"))

@airport.route("/flight-search", methods=[ "POST" ])
def search_flight():
    sorting: str = request.form["sorting"]
    sql_sort_query: str = ""
    
    if sorting != "no-sort":
        if "departure-date" in sorting:
            sql_sort_query += " ORDER BY departure_date"
        elif "arrival-date" in sorting:
            sql_sort_query += " ORDER BY arrival_date"
        elif "seat-class" in sorting:
            sql_sort_query += " ORDER BY seat_class"
        elif "price" in sorting:
            sql_sort_query += " ORDER BY price"
        
        if "ascending" in sorting:
            sql_sort_query += " ASC"
        elif "descending" in sorting:
            sql_sort_query += " DESC"
    
    flights = execute(query="""
        SELECT * FROM flight
        WHERE flight_code ILIKE '%{search_query}%' OR
            departure_date = '{search_query}' OR
            arrival_date = '{search_query}'
        {sort_query};
    """.format(
        search_query=request.form["search_query"],
        sort_query=sql_sort_query
    ), database="flights_db")
    
    return render_template("airport.html", flights=flights)

@airport.route("/flight-edit", methods=[ "POST" ])
def edit_flight():
    execute(query="UPDATE flight SET price = {price} WHERE flight_code = '{flight_code}';".format(
        price=request.form["price"],
        flight_code=request.form["flight-code"]
    ), database="flights_db")
    
    return redirect(url_for("airport.show_page"))

@airport.route("/flight-delete-<flight_code>")
def delete_flight(flight_code: str):
    execute(query="DELETE FROM flight WHERE flight_code = '{flight_code}';".format(flight_code=flight_code), database="flights_db")
    
    return redirect(url_for("airport.show_page"))
