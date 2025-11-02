# -*- coding: utf-8 -*-
"""
Route class

Created on Thu Oct 23 14:47:47 2025

@author: thomas brockmans
"""

import sqlite3
from dotenv import load_dotenv
import os
from ride import Ride

class Route:

    def __init__ (self, start, destination, type_id, length_km):
        try:
            # type_id can only between 5 and 8
            if type_id < 5 or type_id > 8:
                print("That type of route is not supported.")
                
            else:
                self.start = start.lower()
                self.destination = destination.lower()
                self.type_id = type_id
                self.length_km = int(length_km)
                
                
        except ValueError as err:
            print(f"Error when creating a new route. Invalid use of value: {err}")
            
        except Exception as err:
            print(f"Error when creating a new route: {err}")
     
    
    def set_length_km(self, new_length_km):
        self.length_km = new_length_km
        
    def set_start(self, new_start):
        self.start = new_start
        
    def set_destination(self, new_destination):
        self.destination = new_destination
        
    def set_type(self, new_type_id):
        if new_type_id < 5 or new_type_id > 8:
            print("This type does not exist")
        else:
            self.type_id = new_type_id
            
     # method to write object to the database       
    def create(self):
        
        # checking if a route with this start and destination already exists, in which case a next version is created
        version_index = 1
        
        while Route.route_exists(self.start, self.destination, version_index):
            version_index += 1
        
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
                    INSERT INTO routes (start, destination, version, type_id, length_km)
                    VALUES (?, ?, ?, ?, ?)
                    """
                params = (
                    self.start,
                    self.destination,
                    version_index,
                    self.type_id,
                    self.length_km
                    )
                cursor.execute(query, params)
                connection.commit()
        
        except Exception as err:
            print(f"Error when writing to the database: {err}")
        
            
    # class method to get a route by id   
    @classmethod
    def get_by_id(cls, route_id): 
        
        current_file = os.path.abspath(__file__)
        models_dir = os.path.dirname(current_file)
        project_root = os.path.dirname(models_dir)
        load_dotenv()
        db_path = os.getenv("DATABASE_PATH")
        db_root_path = os.path.join(project_root, db_path)
        
        
        try:
            with sqlite3.connect(db_root_path) as connection:
        
                cursor = connection.cursor()
            
                query = """
                    SELECT * FROM routes WHERE route_id LIKE ?
                    """
                
                cursor.execute(query, (route_id,))
                
                route = cursor.fetchone()
            
                return route
        
        except Exception as err:
            print(f"Error when reading from the database: {err}")
        
        
    
    # class method to get all routes   
    @classmethod
    def get_all(cls): 
        
        current_file = os.path.abspath(__file__)
        models_dir = os.path.dirname(current_file)
        project_root = os.path.dirname(models_dir)
        load_dotenv()
        db_path = os.getenv("DATABASE_PATH")
        db_root_path = os.path.join(project_root, db_path)
        
        
        try:
            with sqlite3.connect(db_root_path) as connection:
        
                cursor = connection.cursor()
            
                query = """
                    SELECT routes.route_id as id, routes.start as start, routes.destination as destination, types.type_name as type, routes.length_km as length_km, routes.average_score as average_score, routes.average_time_minutes as average_time_minutes
                    FROM routes
                    JOIN types ON routes.type_id = types.type_id
                    ORDER BY average_score DESC
                    """
                
                cursor.execute(query)
                
                list_routes = cursor.fetchall()
            
                return list_routes
        
        except Exception as err:
            print(f"Error when reading from the database: {err}")
            
            
    # method to check whether a route with that start and destination and version already exists   
    def route_exists(start,destination, version):
        
        current_file = os.path.abspath(__file__)
        models_dir = os.path.dirname(current_file)
        project_root = os.path.dirname(models_dir)
        load_dotenv()
        db_path = os.getenv("DATABASE_PATH")
        db_root_path = os.path.join(project_root, db_path)
        
        
        try:
            with sqlite3.connect(db_root_path) as connection:
        
                cursor = connection.cursor()
            
                query = """
                    SELECT * FROM routes WHERE start LIKE ? AND destination LIKE ? AND version = ?
                    """
                
                params = (
                    start.lower(), destination.lower(), int(version)
                    )
                
                cursor.execute(query,params)
                
                list_routes = cursor.fetchall()
            
                if len(list_routes) > 0:
                    return True
                else:
                    return False
        
        except Exception as err:
            print(f"Error when reading from the database: {err}")
        
        
    
    # classmethod to update all averages of a route
    @classmethod
    def calculate_averages(cls, route_id):
        
        total_duration = 0
        total_score = 0
        
        list_rides = Ride.get_rides_by_route_id(route_id)
        
        count_rides = len(list_rides)
        
        # Only calculate and update if there are rides for this route
        if count_rides == 0:
            print(f"No rides found for route_id {route_id}")
            return
        
        for ride in list_rides:
                        
            date = ride[0]
            start_time = ride[1]
            end_time = ride[2]
            score = ride[3]
            
            ride_duration = Ride.calculate_duration(date, start_time, end_time)
            total_duration += ride_duration
            total_score += score
        
        average_duration = total_duration / count_rides
        average_score = total_score / count_rides
        

        current_file = os.path.abspath(__file__)
        models_dir = os.path.dirname(current_file)
        project_root = os.path.dirname(models_dir)
        load_dotenv()
        db_path = os.getenv("DATABASE_PATH")
        db_root_path = os.path.join(project_root, db_path)
        
        try:
            with sqlite3.connect(db_root_path) as connection:
                cursor = connection.cursor()
                
                query = """
                    UPDATE routes 
                    SET average_score = ?, average_time_minutes = ?
                    WHERE route_id = ?
                    """
                
                params = (
                    round(average_score, 2),
                    int(round(average_duration)),
                    route_id
                )
                
                cursor.execute(query, params)
                connection.commit()
                
                print(f"Updated route {route_id}: average_score={round(average_score, 2)}, average_time_minutes={int(round(average_duration))}")
        
        except Exception as err:
            print(f"Error when updating route averages in the database: {err}")



        
if __name__ == '__main__':
    
    print("GET ALL ROUTES")
        
    list = Route.get_all()
    print(list)
    
    print("")
    
    Route.calculate_averages(4)

        
