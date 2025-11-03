# -*- coding: utf-8 -*-
"""
Ride class

Created on Thu Oct 30 14:47:47 2025

@author: thomas brockmans
"""

import sqlite3
from dotenv import load_dotenv
import os
from datetime import datetime

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
            
            
    def __str__(self):
        
        return (f"{self.route_id} - {self.date} {self.start_time} - {self.end_time} | {self.score} | {self.weather_id}")
     
           
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
        
    
    # method to update a record
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
            print("That ride does not exist. Please use an existing ride id.")
    
    # class method to delete a ride
    @classmethod    
    def delete_by_id(cls, ride_id):
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
                    DELETE FROM rides WHERE ride_id LIKE ?
                    """
                
                cursor.execute(query, (ride_id,))
                
                connection.commit()
                
            
        
        except Exception as err:
            print("That ride does not exist. Please use an existing ride id.")
            
        
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
                
                ride_object = Ride(ride[1],ride[2],ride[3],ride[4],ride[5],ride[6])
            
                return ride_object
        
        except Exception as err:
            print("That ride does not exist. Please use an existing ride id.")
        
        
    
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
                    SELECT  rides.date as date, rides.start_time as start_time, rides.end_time as end_time, rides.score as score, routes.start as start, routes.destination as destination, routes.route_id as route, types.type_name as type, routes.length_km as length_km, routes.version as version, routes.average_score as average_route_score, weather_types.weather_name as weather, rides.ride_id as ride_id
                    FROM rides 
                    JOIN routes ON rides.route_id = routes.route_id
                    JOIN weather_types on rides.weather_id = weather_types.weather_id
                    JOIN types on routes.type_id = types.type_id
                    ORDER BY rides.date DESC, rides.start_time DESC
                    """
                
                cursor.execute(query)
                
                list_rides = cursor.fetchall()
            
                return list_rides
        
        except Exception as err:
            print(f"Error when reading from the database: {err}")
            
            
    
      
    # class method to get last n rides   
    @classmethod
    def get_last_n(cls, n): 
        
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
                    SELECT  rides.date as date, rides.start_time as start_time, rides.end_time as end_time, rides.score as score, routes.start as start, routes.destination as destination, routes.version as version, routes.length_km as length_km, types.type_name as type, weather_types.weather_name as weather
                    FROM rides 
                    JOIN routes ON rides.route_id = routes.route_id
                    JOIN weather_types on rides.weather_id = weather_types.weather_id
                    JOIN types on routes.type_id = types.type_id
                    ORDER BY rides.date DESC, rides.start_time DESC
                    LIMIT ?
                    """
                
                cursor.execute(query, (n,))
                
                list_n_rides = cursor.fetchall()
            
                return list_n_rides
        
        except Exception as err:
            print(f"Error when reading from the database: {err}")
            
    
    # class method to get all rides from a specific route
    @classmethod
    def get_rides_by_route_id(cls, route_id):
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
                    SELECT  rides.date as date, rides.start_time as start_time, rides.end_time as end_time, rides.score as score, routes.start as start, routes.destination as destination, routes.version as version, routes.length_km as length_km, types.type_name as type, weather_types.weather_name as weather, rides.ride_id as ride_id
                    FROM rides 
                    JOIN routes ON rides.route_id = routes.route_id
                    JOIN weather_types on rides.weather_id = weather_types.weather_id
                    JOIN types on routes.type_id = types.type_id
                    WHERE rides.route_id LIKE ?
                    ORDER BY rides.date DESC, rides.start_time DESC
                    """
                
                cursor.execute(query, (route_id,))
                
                list_rides = cursor.fetchall()
                
                    
                return list_rides
        
        except Exception as err:
            print("That route doesn't exist. Please use an existing route id.")
        
    
    # classmethod to calculate the duration in minutes
    @classmethod
    def calculate_duration(cls, date, start_time, end_time):
        
        date_str = date
        start_time_str = start_time
        end_time_str = end_time
        
        start_datetime = datetime.strptime(f"{date_str} {start_time_str}", "%Y-%m-%d %H:%M")
        end_datetime = datetime.strptime(f"{date_str} {end_time_str}", "%Y-%m-%d %H:%M")
        
        duration = end_datetime - start_datetime
        
        duration_minutes = int(duration.total_seconds() / 60)
        
        return duration_minutes



        
if __name__ == '__main__':
    

        list_rides = Ride.get_all()
        print(list_rides)
        
        print(Ride.get_by_id(1))
        
        print(Ride.get_rides_by_route_id(1))
