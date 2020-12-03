from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from db import execute


airline: Blueprint = Blueprint("airline", __name__)


@airline.route("/airline")
def show_page():
    airlines = execute(query="SELECT * FROM airline;", database="flights_db")
    planes = execute(query="SELECT * FROM plane;", database="flights_db")
    
    return render_template("airline.html", airlines=airlines, planes=planes)


# Actions on airline

@airline.route("/airline-add", methods=[ "POST" ])
def add_airline():
    query: str = "INSERT INTO airline VALUES ('{airline_code}', '{name}', '{website}');"
    formatted_query: str = query.format(
        airline_code=request.form["airline-code"],
        name=request.form["name"],
        website=request.form["website"]
    )
    
    execute(query=formatted_query, database="flights_db")
    
    return redirect(url_for("airline.show_page"))

@airline.route("/airline-search", methods=[ "POST" ])
def search_airline():
    sorting: str = request.form["sorting"]
    sort_query: str = ""
    
    if sorting != "no-sort":
        if "name" in sorting:
            sort_query += " ORDER BY name"
        
        if "ascending" in sorting:
            sort_query += " ASC"
        elif "descending" in sorting:
            sort_query += " DESC"
    
    query: str = """
        SELECT * FROM airline
        WHERE airline_code ILIKE '%{search_query}%' OR
            name ILIKE '%{search_query}%'
        {sort_query};
    """
    formatted_query: str = query.format(
        search_query=request.form["search_query"],
        sort_query=sort_query
    )
    
    airlines = execute(query=formatted_query, database="flights_db")
    
    return render_template("airline.html", airlines=airlines)

@airline.route("/airline-delete-<airline_code>")
def delete_airline(airline_code: str):
    query: str = "DELETE FROM airline WHERE airline_code = '{airline_code}';"
    formatted_query: str = query.format(
        airline_code=airline_code
    )
    
    execute(query=formatted_query, database="flights_db")
    
    return redirect(url_for("airline.show_page"))


# Actions on airline & on plane

@airline.route("/airline-plane-search", methods=[ "POST" ])
def search_airline_plane():
    query: str = """
        SELECT * FROM airline
        JOIN plane ON airline.airline_code = plane.airline_code
        WHERE airline.airline_code ILIKE '%{search_query}%' OR
            airline.name ILIKE '%{search_query}%';
    """
    formatted_query: str = query.format(
        search_query=
        request.form["search_query"]
    )
    
    airlines_planes = execute(query=formatted_query, database="flights_db")
    
    airlines = []
    planes = []
    
    for airline_plane in airlines_planes:
        airlines.append(airline_plane[:3])
        planes.append(airline_plane[3:])
    
    return render_template("airline.html", airlines=airlines, planes=planes)


# Actions on plane

@airline.route("/plane-add", methods=[ "POST" ])
def add_plane():
    query: str = """
        INSERT INTO plane VALUES (
            '{plane_code}',
            '{airline_code}',
            '{flight_code}',
            '{name}',
            '{seats_count}'
        );
    """
    formatted_query: str = query.format(
        plane_code=request.form["plane-code"],
        airline_code=request.form["airline-code"],
        flight_code=request.form["flight-code"],
        name=request.form["name"],
        seats_count=request.form["seats-count"]
    )
    
    execute(query=formatted_query, database="flights_db")
    
    return redirect(url_for("airline.show_page"))

@airline.route("/plane-search", methods=[ "POST" ])
def search_plane():
    sorting: str = request.form["sorting"]
    sort_query: str = ""
    
    if sorting != "no-sort":
        if "name" in sorting:
            sort_query += " ORDER BY name"
        elif "seats-count" in sorting:
            sort_query += " ORDER BY seats_count"
        
        if "ascending" in sorting:
            sort_query += " ASC"
        elif "descending" in sorting:
            sort_query += " DESC"
    
    query: str = """
        SELECT * FROM plane
        WHERE plane_code ILIKE '%{search_query}%' OR
            name ILIKE '%{search_query}%'
        {sort_query};
    """
    formatted_query: str = query.format(
        search_query=request.form["search_query"],
        sort_query=sort_query
    )
    
    planes = execute(query=formatted_query, database="flights_db")
    
    return render_template("airline.html", planes=planes)

@airline.route("/plane-delete-<plane_code>")
def delete_plane(plane_code: str):
    query: str = "DELETE FROM plane WHERE plane_code = '{plane_code}';"
    formatted_query: str = query.format(
        plane_code=plane_code
    )
    
    execute(query=formatted_query, database="flights_db")
    
    return redirect(url_for("airline.show_page"))
