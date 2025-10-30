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
                
                
        except ValueError as err:
            print(f"Error when logging a ride. Invalid use of value: {err}")
            
        except Exception as err:
            print(f"Error when logging a ride: {err}")
     
           
     # method to write object to the database       
    def create(self):
        
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
                    INSERT INTO rides (route_id, date, start_time, end_time, score, weather_id)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """
                params = (
                    self.route_id,
                    self.date,
                    self.start_time,
                    self.end_time,
                    self.score,
                    self.weather_id
                    )
                cursor.execute(query, params)
                connection.commit()
            
        
        except Exception as err:
            print(f"Error when writing to the database: {err}")
        
    
    
    def update(self, ride_id, route_id,date,start_time, end_time, score, weather_id):
            
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
                    UPDATE rides 
                    SET route_id = ?,
                        date = ?,
                        start_time = ?,
                        end_time = ?,
                        score = ?,
                        weather_id = ?
                    WHERE ride_id LIKE ?
                    """
                params = (
                    route_id,
                    date,
                    start_time,
                    end_time,
                    score,
                    weather_id,
                    ride_id
                    )
                cursor.execute(query, params)
                connection.commit()
        
        except Exception as err:
            print(f"Error when writing to the database: {err}")
    
    
        
    # class method to get a ride by id   
    @classmethod
    def get_by_id(cls, ride_id): 
        
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
                    SELECT * FROM rides WHERE ride_id LIKE ?
                    """
                
                cursor.execute(query, (ride_id,))
                
                ride = cursor.fetchone()
            
                return ride
        
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
    
    ride = Ride.get_by_id(3)
    print(ride)
    ride_update = Ride(ride[1], ride[2], ride[3], ride[4], ride[5], ride[6])
    
    ride_update.update(ride[0],ride[1], ride[2],ride[3],"10:10",7,ride[6])
        
