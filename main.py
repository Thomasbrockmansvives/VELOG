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


user_state = "start"


def startup_application():
    Layout.splash_screen()
    
    Layout.print_continue()
        
    Layout.print_title("Welcome to the bike ride logging app")
    Layout.print_text("This application helps you to log rides, based on template routes.")
    Layout.print_text("You can consult all the routes and rides,")
    Layout.print_text("new template routes can also be created,")
    Layout.print_text("and you can ask for csv exports of the rides and routes.")
    
    Layout.print_continue()
    
    
    Layout.print_line()
    Layout.print_5_most_recent_rides()
    Layout.print_line()
    
    
# TODO
# input values
def log_a_new_ride():
    pass


# TODO
# input ride to update
# input updates, if empty keep existing
def update_a_ride():
    pass


# TODO
# input ride to delete
def delete_a_ride():
    pass


# TODO
# input values
def create_a_new_route():
    pass


# TODO
# input route
def show_rides_of_route():
    pass


def close_app():
    print()
    Layout.print_title("Closing the application. Hope to see you soon !")
    sys.exit(0)


# TODO    
# input option: set user_state according to option
def main_options():
    Layout.print_line()
    Layout.print_main_options()

# TODO
# input option: set user_state according to option
def ride_options():
    pass


# TODO
# input option: set user_state according to option
def route_options():
    pass

# TODO
def get_option():
    pass
    




if __name__ == '__main__': 
    
    while not user_state == "end":
        
        if user_state == "start":
            startup_application()
            user_state = "main"
            
        elif user_state == "main":  
            # TODO
            main_options()
            close_app()
            
        elif user_state == "rides":
            # TODO
            ride_options()
            close_app()
            
        elif user_state == "routes":
            # TODO
            route_options()
            close_app()
            
        elif user_state == "new_ride":
            # TODO
            log_a_new_ride()
            close_app()
            
        elif user_state == "update_ride":
            # TODO
            update_a_ride()
            close_app()
            
        elif user_state == "delete_ride":
            # TODO
            delete_a_ride()
            close_app()
            
        elif user_state == "new_route":
            # TODO
            create_a_new_route()
            close_app()
        
        elif user_state == "end":
            close_app()
            
        else:
            user_state = "end"