#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Export class

Created on Sun Nov  2 13:12:17 2025

@author: thomasbrockmans
"""

from models.ride import Ride
from models.route import Route
import csv
from datetime import datetime
import os

class Export:
    
    def __init__(self):
        pass
    
    
    # classmethod to export all routes to csv
    @classmethod
    def export_all_routes(cls):
        
        list_routes = Route.get_all()
        
        # creating path to new export file
        try:
            now = datetime.now()
            now_string = now.strftime("%Y%m%d%H%M%S")
            file_name = "export_routes_" + now_string + ".csv"
        
            current_file = os.path.abspath(__file__)
            models_dir = os.path.dirname(current_file)
            project_root = os.path.dirname(models_dir)
            export_folder = os.path.join(project_root, 'Export')
            
            csv_file_path = os.path.join(export_folder, file_name)
        except Exception as err:
            print(f"Error when checking path to export folder: {err}")
        
        # populating export file
        try:
            with open(csv_file_path, 'w',newline='') as file:
                writer = csv.writer(file, delimiter=';')
                
                header = ['id', 'start', 'destination', 'type', 'length_km', 'average_score', 'average_time_minutes']
                writer.writerow(header)
            
                for route in list_routes:
                    writer.writerow(route)
                    
            print()
            print("Export succesful. Please find the export of all routes in the Export folder.")
            print()
            
        except Exception as err:
            print(f"Error when exporting to csv: {err}")
                
            
    # classmethod to export all rides to csv
    @classmethod
    def export_all_rides(cls):
        
        list_rides = Ride.get_all()
        
        # creating path to new export file
        try:
            now = datetime.now()
            now_string = now.strftime("%Y%m%d%H%M%S")
            file_name = "export_rides_" + now_string + ".csv"
        
            current_file = os.path.abspath(__file__)
            models_dir = os.path.dirname(current_file)
            project_root = os.path.dirname(models_dir)
            export_folder = os.path.join(project_root, 'Export')
            
            csv_file_path = os.path.join(export_folder, file_name)
        except Exception as err:
            print(f"Error when checking path to export folder: {err}")
        
        # populating export file
        try:
            with open(csv_file_path, 'w',newline='') as file:
                writer = csv.writer(file, delimiter=';')
                
                header = ['date', 'start_time', 'end_time', 'score', 'weather','start', 'destination', 'route', 'type', 'length_km', 'version', 'average_route_score']
                writer.writerow(header)
            
                for ride in list_rides:
                    writer.writerow(ride)
                    
            print()
            print("Export succesful. Please find the export of all rides in the Export folder.")
            print()
            
        except Exception as err:
            print(f"Error when exporting to csv: {err}")
   
# to test this class, run this script            
if __name__ == '__main__':
    Export.export_all_rides()
    Export.export_all_routes()