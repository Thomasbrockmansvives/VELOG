#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Layout class

Created on Sun Nov  2 13:54:40 2025

@author: thomasbrockmans
"""

from ride import Ride
from route import Route

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
            "███████████████████████████████████████████████████████████████████████████████████",
            "",
            "{:^83}".format("<<< " +title.upper() + " >>>"),
            "_"*83,
            ""
            ]
        
        for line in title:
            print(line)
            
    @classmethod
    def print_main_options(cls):
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
        list_ride_options = [
            [1, "LOG a new ride"],
            [2, "UPDATE a ride"],
            [3, "DELETE a ride"],
            [4, "BACK to the main menu"]
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
        
        
    #TODO: show rides of a route
        
        
        
    @classmethod
    def print_route_options(cls):
        list_route_options = [
            [1, "CREATE a new ROUTE"],
            [2, "Show all RIDES of a specific ROUTE"],
            [3, "BACK to the main menu"]
            ]
            
        for option in list_route_options:
            number = option[0]
            description = option[1]
                
            print(f"{number} - {description}")
                
        print("_"*83)
        print(" ")
    
    

if __name__ == '__main__':
    Layout.splash_screen()
    Layout.print_5_most_recent_rides()
    Layout.print_title("choose an option")
    Layout.print_main_options()
    