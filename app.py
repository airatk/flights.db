from flask import Flask
from flask import render_template

from airline import airline
from airport import airport
from client import client

from db import execute


flights_db: Flask = Flask(__name__)

flights_db.register_blueprint(airline)
flights_db.register_blueprint(airport)
flights_db.register_blueprint(client)


@flights_db.route("/")
def show_base_page():
    return render_template("base.html")

@flights_db.route("/drop-database")
def drop_database():
    execute(query="DROP DATABASE IF EXISTS flights_db;")
    execute(query="CREATE DATABASE flights_db;")
    
    execute(query="""
        CREATE TABLE airline (
            airline_code VARCHAR(6) PRIMARY KEY,
            name VARCHAR(120),
            website VARCHAR(60)
        );
        
        CREATE TABLE plane (
            plane_code VARCHAR(6) PRIMARY KEY,
            airline_code VARCHAR(6),
            flight_code VARCHAR(6),
            name VARCHAR(120),
            seats_count SMALLINT
        );
        
        CREATE TABLE airport (
            airport_code VARCHAR(6) PRIMARY KEY,
            name VARCHAR(120),
            city VARCHAR(60),
            country VARCHAR(60),
            longitude NUMERIC(7, 4),
            latitude NUMERIC(7, 4),
            timezone VARCHAR(120)
        );
        
        CREATE TABLE flight (
            flight_code VARCHAR(6) PRIMARY KEY,
            departure_airport_code VARCHAR(6),
            arrival_airport_code VARCHAR(6),
            departure_date DATE,
            arrival_date DATE,
            departure_time TIME,
            arrival_time TIME,
            time INTERVAL,
            miles SMALLINT,
            seat_class CHAR,
            seat_number SMALLINT,
            price NUMERIC(9, 2)
        );
        
        CREATE TABLE client (
            personal_id VARCHAR(10) PRIMARY KEY,
            name VARCHAR(40),
            birth_date DATE,
            phone VARCHAR(16),
            email VARCHAR(40)
        );
        
        CREATE TABLE ticket (
            ticket_code VARCHAR(6) PRIMARY KEY,
            personal_id VARCHAR(10),
            flight_code VARCHAR(6),
            status VARCHAR(12)
        );
    """, database="flights_db")
    
    execute(query="""
        ALTER TABLE plane ADD FOREIGN KEY (airline_code) REFERENCES airline(airline_code) ON DELETE CASCADE ON UPDATE CASCADE;
        ALTER TABLE plane ADD FOREIGN KEY (flight_code) REFERENCES flight(flight_code) ON DELETE NO ACTION ON UPDATE CASCADE;
        
        ALTER TABLE flight ADD FOREIGN KEY (departure_airport_code) REFERENCES airport(airport_code) ON DELETE NO ACTION ON UPDATE CASCADE;
        ALTER TABLE flight ADD FOREIGN KEY (arrival_airport_code) REFERENCES airport(airport_code) ON DELETE NO ACTION ON UPDATE CASCADE;
        
        ALTER TABLE ticket ADD FOREIGN KEY (personal_id) REFERENCES client(personal_id) ON DELETE CASCADE ON UPDATE CASCADE;
        ALTER TABLE ticket ADD FOREIGN KEY (flight_code) REFERENCES flight(flight_code) ON DELETE CASCADE ON UPDATE CASCADE;
    """, database="flights_db")
    
    return render_template("base.html")
