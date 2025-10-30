# -*- coding: utf-8 -*-
"""
Ride class

Created on Thu Oct 30 14:47:47 2025

@author: thomas brockmans
"""

import sqlite3
from dotenv import load_dotenv
import os

class Ride:

    # TODO
    def __init__ (self, route_id, date, start_time, end_time, score, weather_id):
        try:
            # weather_id can only between 6 and 13
            if weather_id < 6 or weather_id > 13:
                print("That type of weather is not supported.")
                
            elif score < 0 or score > 10:
                print("The score must be between 0 and 10.")
                
            else:
                self.route_id = route_id
                self.date = date
                self.start_time = start_time
                self.end_time = end_time
                self.score = score
                self.weather_id = weather_id
                
                print(f"A new ride has been created on {date} from {start_time} to {end_time} with a score of {score}.")
                
        except ValueError as err:
            print(f"Error when logging a ride. Invalid use of value: {err}")
            
        except Exception as err:
            print(f"Error when logging a ride: {err}")
     
    
    # TODO        
     # method to write object to the database       
    def create(self):
        
        # checking if a route with this start and destination already exists, in which case a next version is created
        version_index = 1
        
        while Route.route_exists(self.start, self.destination, version_index):
            version_index += 1
        
        print(f"This version will be {version_index}")
        
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
            
            print("The new route has been saved to the database.")
        
        except Exception as err:
            print(f"Error when writing to the database: {err}")
        
    
    
    # TODO        
    # class method to get a ride by id   
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
        
        
    # TODO    
    # class method to get all rides   
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
                    SELECT * FROM routes
                    """
                
                cursor.execute(query)
                
                list_routes = cursor.fetchall()
            
                return list_routes
        
        except Exception as err:
            print(f"Error when reading from the database: {err}")
            
            
    
    # TODO
    def calculate_averages(self):
        pass
        
    



        
if __name__ == '__main__':
    
    pass
        
