# -*- coding: utf-8 -*-
"""
Route class

Created on Thu Oct 23 14:47:47 2025

@author: thomas brockmans
"""

import sqlite3
from dotenv import load_dotenv
import os

class Route:

    def __init__ (self, start, destination, type_id, length_km):
        try:
            if type_id < 5 or type_id > 8:
                print("That type of route is not supported.")
                
            else:
                self.start = start.lower()
                self.destination = destination.lower()
                self.type_id = type_id
                self.length_km = int(length_km)
                print(f"A new route with start {start} and destination {destination} and {length_km} km longs has successfully been created.")
                
        except ValueError as err:
            print(f"Error when creating a new route. Invalid use of value: {err}")
            
        except Exception as err:
            print(f"Error when creating a new route: {err}")
            
            
            
    def create(self):
        
        # TODO: if that route already exists, create a new version
        
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
                    INSERT INTO routes (start, destination, version, type_id, length_km)
                    VALUES (?, ?, ?, ?, ?)
                    """
                params = (
                    self.start,
                    self.destination,
                    1,
                    self.type_id,
                    self.length_km
                    )
                cursor.execute(query, params)
                connection.commit()
            
            print("The new route has been saved to the database.")
        
        except Exception as err:
            print(f"Error when writing to the database: {err}")
            
        
        
        



        
if __name__ == '__main__':
        route = Route("overijse", "oostende", 7, 135)
        route.create()