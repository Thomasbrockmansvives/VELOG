#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Layout class

Created on Sun Nov  2 13:54:40 2025

@author: thomasbrockmans
"""

from models.ride import Ride
from models.route import Route
import os
import sqlite3
from dotenv import load_dotenv

class Layout:
    
    def __init__(self):
        pass
    
    @classmethod
    def splash_screen(cls):
        
        velog_logo = [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "███████████████████████████████████████████████████████████████████████████████████",
            "="*83,
            "███████████████████████████████████████████████████████████████████████████████████",
            "████████████████████████████████████████████   ████████████████████████████████████",
            "█████████████████████████████████████   █████ █████████████████████████████████████",
            "██████████████████████████████████████        █████████████████████████████████████",
            "█████████████████████████████████   █  █ ███   ████████████████████████████████████",
            "████████████████████████████████ ███    ███ ███ ███████████████████████████████████",
            "█████████████████████████████████   ████████   ████████████████████████████████████",
            "███████████████████████████████████████████████████████████████████████████████████",
            "██████████████████  ██████  ██      ██  ████████    ██████    █████████████████████",
            "███████████████████  ████  ███  ██████  ███████  ██  ████  ████████████████████████",
            "=================███==██==████====████==██████==████==██==██====███================",
            "█████████████████████    █████  ██████  ███████  ██  ████  ██  ████████████████████",
            "██████████████████████  ██████      ██      ████    ██████    █████████████████████",
            "███████████████████████████████████████████████████████████████████████████████████",
            "███████████████████" + "{:^45}".format("***   the  bike  ride  logging  app   ***".upper()) + "███████████████████",
            "███████████████████████████████████████████████████████████████████████████████████",
            "███████████████████████████████████████████████████████████████████████████████████",
            ""
            ]
        
        for line in velog_logo:
            print(line)
            
    
    @classmethod 
    def print_5_most_recent_rides(cls):
        
        print("{:^83}".format("<<< FIVE MOST RECENT RIDES >>>"))
        print("="*83)
        print("")
        
        rides = Ride.get_last_n(5)
        
        print("{:<4}".format("") + "|" + "{:<11}".format("DATE") + "|" + "{:<6}".format("START") + "|" + "{:<6}".format("END") + "|" + "{:<6}".format("SCORE") + "|" + "{:<9}".format("FROM") + "|" + "{:<9}".format("TO") + "|" + "{:<4}".format("KM") + "|" + "{:<9}".format("TYPE") + "|" + "{:<10}".format("WEATHER") + "|")
        print("-"*83)
        
        for ride in rides:

            date = ride[0]
            start = ride[1]
            end = ride[2]
            score = ride[3]
            from_location = ride[4]
            to_location = ride[5]
            length = ride[7]
            type_route = ride[8]
            weather = ride[9]
            print("{:<4}".format("") + "|" + "{:<11}".format(f"{date}") + "|" + "{:<6}".format(f"{start}") + "|"  + "{:<6}".format(f"{end}") + "|"   + "{:<6}".format(f"{score}") + "|"   + "{:<9}".format(f"{from_location}") + "|"   + "{:<9}".format(f"{to_location}") + "|"  + "{:<4}".format(f"{length}") + "|" + "{:<9}".format(f"{type_route}") + "|"+ "{:<10}".format(f"{weather}") + "|")
            
        print("")
        
            
    @classmethod
    def print_title(cls, title):

        title = [
            "",
            "█"*83,
            "",
            "{:^83}".format("<<< " +title.upper() + " >>>"),
            "_"*83,
            ""
            ]
        
        for line in title:
            print(line)
            
            
    @classmethod
    def print_text(cls, text):
        text = "{:^83}".format(text.title())
        
        print(text)
        
        
    @classmethod
    def print_line(cls):  
        print()
        print("█"*83,)
        print()
    
    
        
    @classmethod
    def print_continue(cls):
        
        print()
        input("{:^83}".format("enter any key to continue..."))

            
    @classmethod
    def print_main_options(cls):
        
        print("{:^83}".format("<<< MAIN OPTIONS >>>"))
        print("="*83)
        print("")
        
        list_main_options = [
            [1, "LOG a new ride"],
            [2, "Show all RIDES"],
            [3, "Show all ROUTES"],
            [4, "Create a NEW route"],
            [5, "CLOSE the application"]
            ]

        for option in list_main_options:
            number = option[0]
            description = option[1]
            
            print(f"{number} - {description}")
            
        print("_"*83)
        print("")
        
        
    @classmethod 
    def print_all_rides(cls):
        
        print("{:^83}".format("<<< ALL RIDES >>>"))
        print("="*83)
        print("")
        
        rides = Ride.get_all()
        
        print("{:<4}".format("ID") + "|" + "{:<11}".format("DATE") + "|" + "{:<6}".format("START") + "|" + "{:<6}".format("END") + "|" + "{:<6}".format("SCORE") + "|" + "{:<9}".format("FROM") + "|" + "{:<9}".format("TO") + "|" + "{:<4}".format("KM") + "|" + "{:<9}".format("TYPE") + "|" + "{:<10}".format("WEATHER") + "|")
        print("-"*83)
        
        for ride in rides:
            ride_id = ride[12]
            date = ride[0]
            start = ride[1]
            end = ride[2]
            score = ride[3]
            from_location = ride[4]
            to_location = ride[5]
            length = ride[8]
            type_route = ride[7]
            weather = ride[11]
            print("{:<4}".format(f"{ride_id}") + "|" + "{:<11}".format(f"{date}") + "|" + "{:<6}".format(f"{start}") + "|"  + "{:<6}".format(f"{end}") + "|"   + "{:<6}".format(f"{score}") + "|"   + "{:<9}".format(f"{from_location}") + "|"   + "{:<9}".format(f"{to_location}") + "|"  + "{:<4}".format(f"{length}") + "|" + "{:<9}".format(f"{type_route}") + "|"+ "{:<10}".format(f"{weather}") + "|")
           
            
        print("")    
    
        
    @classmethod
    def print_ride_options(cls):
        
        print("{:^83}".format("<<< RIDE OPTIONS >>>"))
        print("="*83)
        print("")
        
        list_ride_options = [
            [1, "LOG a new ride"],
            [2, "UPDATE a ride"],
            [3, "DELETE a ride"],
            [4, "EXPORT all rides"],
            [5, "BACK to the main menu"]
            ]
        
        for option in list_ride_options:
            number = option[0]
            description = option[1]
            
            print(f"{number} - {description}")
            
        print("_"*83)
        print(" ")
        
        
    @classmethod 
    def print_all_routes(cls):
        
        print("{:^83}".format("<<< ALL ROUTES >>>"))
        print("="*83)
        print("")
        
        routes = Route.get_all()
        
        print("{:<4}".format("ID") + "|" + "{:<11}".format("FROM") + "|" + "{:<11}".format("TO") + "|" + "{:<11}".format("TYPE") + "|" + "{:<5}".format("KM") + "|" + "{:<17}".format("AVERAGE SCORE") + "|" + "{:<17}".format("AVERAGE TIME") + "|")
        print("-"*83)
        
        for route in routes:
            route_id = route[0]
            from_location = route[1]
            to_location = route[2]
            type_route = route[3]
            length = route[4]
            average_score = route[5]
            average_minutes = route[6]
            print("{:<4}".format(f"{route_id}") + "|" + "{:<11}".format(f"{from_location}") + "|"  + "{:<11}".format(f"{to_location}") + "|"   + "{:<11}".format(f"{type_route}") + "|"   + "{:<5}".format(f"{length}") + "|"   + "{:<17}".format(f"{average_score}") + "|"  + "{:<17}".format(f"{average_minutes} minutes") + "|")
            
        print("") 
        
        
    
    @classmethod
    def print_all_rides_by_route(cls,route_id):
        print("{:^83}".format(f"<<< ALL RIDES OF ROUTE {route_id} >>>"))
        print("="*83)
        print("")
        
        rides = Ride.get_rides_by_route_id(route_id)
        
        print("{:<4}".format("ID") + "|" + "{:<11}".format("DATE") + "|" + "{:<6}".format("START") + "|" + "{:<6}".format("END") + "|" + "{:<6}".format("SCORE") + "|" + "{:<9}".format("FROM") + "|" + "{:<9}".format("TO") + "|" + "{:<4}".format("KM") + "|" + "{:<9}".format("TYPE") + "|" + "{:<10}".format("WEATHER") + "|")
        print("-"*83)
        
        for ride in rides:
            ride_id = ride[10]
            date = ride[0]
            start = ride[1]
            end = ride[2]
            score = ride[3]
            from_location = ride[4]
            to_location = ride[5]
            length = ride[7]
            type_route = ride[8]
            weather = ride[9]
            print("{:<4}".format(f"{ride_id}") + "|" + "{:<11}".format(f"{date}") + "|" + "{:<6}".format(f"{start}") + "|"  + "{:<6}".format(f"{end}") + "|"   + "{:<6}".format(f"{score}") + "|"   + "{:<9}".format(f"{from_location}") + "|"   + "{:<9}".format(f"{to_location}") + "|"  + "{:<4}".format(f"{length}") + "|" + "{:<9}".format(f"{type_route}") + "|"+ "{:<10}".format(f"{weather}") + "|")
           
            
        print("")   
        
        
    @classmethod    
    def print_weather(cls):
        
        current_file = os.path.abspath(__file__)
        models_dir = os.path.dirname(current_file)
        project_root = os.path.dirname(models_dir)
        load_dotenv()
        db_path = os.getenv("DATABASE_PATH")
        db_root_path = os.path.join(project_root, db_path)
        
        # writing to the database
        try:
            with sqlite3.connect(db_root_path) as connection:
        
                cursor = connection.cursor()
            
                query = """
                    SELECT * FROM weather_types
                    """
                
                cursor.execute(query)
                
                weather_list = cursor.fetchall()
                
                for weather in weather_list:
                    id = weather[0]
                    name = weather[1]
                    print(f"{id} - {name}")
            
        
        except Exception as err:
            print(f"Error when reading from the database: {err}")
            
            
    @classmethod    
    def print_route_types(cls):
        
        current_file = os.path.abspath(__file__)
        models_dir = os.path.dirname(current_file)
        project_root = os.path.dirname(models_dir)
        load_dotenv()
        db_path = os.getenv("DATABASE_PATH")
        db_root_path = os.path.join(project_root, db_path)
        
        # writing to the database
        try:
            with sqlite3.connect(db_root_path) as connection:
        
                cursor = connection.cursor()
            
                query = """
                    SELECT * FROM types
                    """
                
                cursor.execute(query)
                
                route_type_list = cursor.fetchall()
                
                for route_type in route_type_list:
                    id = route_type[0]
                    name = route_type[1]
                    print(f"{id} - {name}")
            
        
        except Exception as err:
            print(f"Error when reading from the database: {err}")
    
    
    
        
    @classmethod
    def print_route_options(cls):
        
        print("{:^83}".format("<<< ROUTE OPTIONS >>>"))
        print("="*83)
        print("")
        
        list_route_options = [
            [1, "CREATE a new ROUTE"],
            [2, "Show all RIDES of a specific ROUTE"],
            [3, "EXPORT all routes"],
            [4, "BACK to the main menu"]
            ]
            
        for option in list_route_options:
            number = option[0]
            description = option[1]
                
            print(f"{number} - {description}")
                
        print("_"*83)
        print(" ")
    
    

if __name__ == '__main__':
    Layout.print_weather()
    Layout.print_route_types()
    