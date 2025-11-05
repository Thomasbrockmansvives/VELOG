# -*- coding: utf-8 -*-
"""
Main Script

Created on Thu Oct 23 16:03:37 2025

@author: thomas brockmans
"""

from models.route import Route
from models.ride import Ride
from models.layout import Layout
from models.export import Export
import sys
from datetime import datetime


user_state = "start"


def startup_application():
    Layout.splash_screen()
        
    Layout.print_title("Welcome to the bike ride logging app")
    Layout.print_text("This application helps you to log rides, based on template routes.")
    Layout.print_text("You can consult all the routes and rides,")
    Layout.print_text("new template routes can also be created,")
    Layout.print_text("and you can ask for csv exports of the rides and routes.")
    
    Layout.print_continue()
    
    
    Layout.print_line()
    Layout.print_5_most_recent_rides()
    Layout.print_line()
    
    
def log_a_new_ride():
    
    global user_state
    
    Layout.print_title("log a new ride")
    
    try:
        date_input = input("> Enter the date (format yyyy-mm-dd):   ")
        while not validate_date(date_input):
            print("*** Invalid date format. Please use yyyy-mm-dd (e.g., 2025-11-05) ***")
            date_input = input("> Enter the date (format yyyy-mm-dd):   ")
        start_input = input("> At what time did your ride start (format hh:mm):   ")
        while not validate_time(start_input):
            print("*** Invalid time format. Please use hh:mm (e.g., 14:30) ***")
            start_input = input("> At what time did your ride start (format hh:mm):   ")
        end_input = input("> At what time did your ride end (format hh:mm):   ")
        while not validate_time(end_input):
            print("*** Invalid time format. Please use hh:mm (e.g., 16:45) ***")
            end_input = input("> At what time did your ride end (format hh:mm):   ")
        print()
        Layout.print_all_routes()
        print()
        try:
            route_input = int(input("> Enter the id of the route you followed (number):   "))
        except ValueError:
            print("*** That is not an id. An id is in the form of a number. ***")
            
        print()
        Layout.print_weather()
        print()
        try:
            weather_input = int(input("> Enter the id of the weather type (number):   "))
        except ValueError:
            print("*** That is not an id. An id is in the form of a number. ***")
        print()
        try:
            score_input = int(input("> Enter a score between 0 and 10 (number):   "))
        except ValueError:
            print("*** That is not a number. ***")
        
        ride = Ride(route_input, date_input, start_input, end_input, score_input, weather_input)
        
        ride.create()
        
        Layout.print_continue()
        
        user_state = "rides"
        
    except Exception as err:
        print()
        print(f"Error when logging a new ride: {err}")
    
    print()
    
    
def update_a_ride():
    
    global user_state
    
    Layout.print_title("update a ride")
    
    try:
        try:
            id_input = int(input("> Which ride id would you like to update (number):   "))
        except ValueError:
            print("*** That is not an id. An id is in the form of a number. ***")
        
        ride = Ride.get_by_id(id_input)
        print(f"Choosen ride: {ride}")
        
        change_date = input("Would you like to change the date? (y/n)   ")
        if change_date == "y":    
            date_input = input("> Enter the date (format yyyy-mm-dd):   ")
            while not validate_date(date_input):
                print("*** Invalid date format. Please use yyyy-mm-dd (e.g., 2025-11-05) ***")
                date_input = input("> Enter the date (format yyyy-mm-dd):   ")
        else:
            date_input = ride.date
        
        change_start = input("Would you like to change the start time? (y/n)   ")
        if change_start == "y":    
            start_input = input("> At what time did your ride start (format hh:mm):   ")
            while not validate_time(start_input):
                print("*** Invalid time format. Please use hh:mm (e.g., 14:30) ***")
                start_input = input("> At what time did your ride start (format hh:mm):   ")
        else:
            start_input = ride.start_time
            
        change_end = input("Would you like to change the end time? (y/n)   ")
        if change_end == "y":    
            end_input = input("> At what time did your ride end (format hh:mm):   ")
            while not validate_time(end_input):
                print("*** Invalid time format. Please use hh:mm (e.g., 16:45) ***")
                end_input = input("> At what time did your ride end (format hh:mm):   ")
        else:
            end_input = ride.end_time
            
        change_route = input("Would you like to change the route? (y/n)   ")
        if change_route == "y":
            print()
            Layout.print_all_routes()
            print()
            try:
                route_input = int(input("> Enter the id of the route you followed (number):   "))
            except ValueError:
                print("*** That is not an id. An id is in the form of a number. ***")
        else:
            route_input = ride.route_id
            
        change_weather = input("Would you like to change the weather? (y/n)   ")
        if change_weather == "y": 
            print()
            Layout.print_weather()
            print()
            try:
                weather_input = int(input("> Enter the id of the weather type (number):   "))
            except ValueError:
                print("*** That is not an id. An id is in the form of a number. ***")
                print()
        else:
            weather_input = ride.weather_id
            
        change_score = input("Would you like to change the score? (y/n)   ")
        if change_score == "y":
            try:
                score_input = int(input("> Enter a score between 0 and 10 (number):   "))
            except ValueError:
                print("*** That is not a number. ***")
        else:
            score_input = ride.score
        
        ride = Ride(route_input, date_input, start_input, end_input, score_input, weather_input)
        
        ride.update(id_input, route_input, date_input, start_input, end_input, score_input, weather_input)
        
        Layout.print_continue()
        
        user_state = "rides"
        
    except Exception as err:
        print()
        print(f"Error when updating a ride: {err}")
    
    print()


def delete_a_ride():
    
    global user_state
    
    Layout.print_title("update a ride")
    
    try:
        id_input = int(input("> Which ride id would you like to update (number):   "))
        Ride.delete_by_id(id_input)
        
        Layout.print_continue()
        
        user_state = "rides"
        
    except ValueError:
        print("*** That is not an id. An id is in the form of a number. ***")
        
          
def create_a_new_route():
    
    global user_state
    
    Layout.print_title("create a new route")
    
    try:
        start_input = input("> Enter a departing city:   ")
        destination_input = input("> Enter a destination city:   ")
            
        print()
        Layout.print_route_types()
        print()
        try:
            type_input = int(input("> Enter the id of the route type (number):   "))
        except ValueError:
            print("*** That is not an id. An id is in the form of a number. ***")
        print()
        
        try:
            length_input = int(input("> Enter a length in km (number):   "))
        except ValueError:
            print("*** That is not a valid length. ***")
        
        route = Route(start_input, destination_input, type_input, length_input)
        
        route.create()
        
        Layout.print_continue()
        
        user_state = "routes"
        
    except Exception as err:
        print()
        print(f"Error when creating a new route: {err}")
    
    print()


def show_rides_of_route():
    
    global user_state
    
    Layout.print_line()
    Layout.print_all_routes()
    Layout.print_line()
    
    try:
        route_input = int(input("> From which route id would you like to see all rides (number):   "))
        Layout.print_all_rides_by_route(route_input)
        Layout.print_continue()
        user_state = "rides"
    except ValueError:
        print("*** That is not an id. An id is in the form of a number. ***")
    

def export_rides():
    
    global user_state
    
    Layout.print_line()
    Layout.print_text("Exporting all rides to a csv in the Export folder.")
    Export.export_all_rides()
    
    Layout.print_continue()
    
    user_state = "rides"
    

def export_routes():
    
    global user_state
    
    Layout.print_line()
    Layout.print_text("Exporting all routes to a csv in the Export folder.")
    Export.export_all_routes()
    
    Layout.print_continue()
    
    user_state = "routes"
    


def close_app():
    print()
    Layout.print_title("Closing the application. Hope to see you soon !")
    sys.exit(0)



def main_options():
    Layout.print_line()
    Layout.print_main_options()


def ride_options():
    Layout.print_line()
    Layout.print_all_rides()
    Layout.print_ride_options()


def route_options():
    Layout.print_line()
    Layout.print_all_routes()
    Layout.print_route_options()
    
def validate_date(date_string):

    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_time(time_string):

    try:
        datetime.strptime(time_string, "%H:%M")
        return True
    except ValueError:
        return False

    




if __name__ == '__main__': 
    
    while not user_state == "end":
        
        if user_state == "start":
            startup_application()
            user_state = "main"
            
        elif user_state == "main":  
            
            main_options()
            
            try:
                option = int(input("Give the number of your choosen option:   "))
                
                if option == 1:
                    user_state = "new_ride"
                elif option == 2:
                    user_state = "rides"
                elif option == 3:
                    user_state = "routes"
                elif option == 4:
                    user_state = "new_route"
                elif option == 5:
                    user_state = "end"
                else:
                    print()
                    print("*** That is not an existing option. Please choose a number between 1 and 5. ***")
                    user_state = "main"
                    
                    
            except ValueError:
                print()
                print("*** That is not a valid option. Please give the number of your option. ***")
                print()
            
        elif user_state == "rides":
            
            ride_options()
            
            try:
                option = int(input("Give the number of your choosen option:   "))
                
                if option == 1:
                    user_state = "new_ride"
                elif option == 2:
                    user_state = "update_ride"
                elif option == 3:
                    user_state = "delete_ride"
                elif option == 4:
                    user_state = "export_rides"
                elif option == 5:
                    user_state = "main"
                else:
                    print()
                    print("*** That is not an existing option. Please choose a number between 1 and 4. ***")
                    user_state = "main"
                    
                    
            except ValueError:
                print()
                print("*** That is not a valid option. Please give the number of your option. ***")
                print()
            
        elif user_state == "routes":
            
            route_options()
            
            try:
                option = int(input("Give the number of your choosen option:   "))
                
                if option == 1:
                    user_state = "new_route"
                elif option == 2:
                    user_state = "rides_by_route"
                elif option == 3:
                    user_state = "export_routes"
                elif option == 4:
                    user_state = "main"
                
                else:
                    print()
                    print("*** That is not an existing option. Please choose a number between 1 and 5. ***")
                    user_state = "routes"
                    
                    
            except ValueError:
                print()
                print("*** That is not a valid option. Please give the number of your option. ***")
                print()
            
        elif user_state == "new_ride":
            
            log_a_new_ride()
            print()
            Layout.print_5_most_recent_rides()
            
            
        elif user_state == "update_ride":
            
            update_a_ride()
    
            
        elif user_state == "delete_ride":
            
            delete_a_ride()
            
            
        elif user_state == "new_route":
            
            create_a_new_route()
            
            
        elif user_state == "rides_by_route":
            
            show_rides_of_route()
            
        elif user_state == "export_rides":
            
            export_rides()
            
        elif user_state == "export_routes":
            
            export_routes()
        
        elif user_state == "end":
            close_app()
            
        else:
            user_state = "main"