#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Export class

Created on Sun Nov  2 13:12:17 2025

@author: thomasbrockmans
"""

from ride import Ride
from route import Route
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
        now = datetime.now()
        now_string = now.strftime("%Y%m%d%H%M%S")
        file_name = "export_routes_" + now_string + ".csv"
    
        current_file = os.path.abspath(__file__)
        models_dir = os.path.dirname(current_file)
        project_root = os.path.dirname(models_dir)
        export_folder = os.path.join(project_root, 'Export')
        
        csv_file_path = os.path.join(export_folder, file_name)
        
        # populating export file
        with open(csv_file_path, 'w',newline='') as file:
            writer = csv.writer(file, delimiter=';')
            
            header = ['id', 'start', 'destination', 'type', 'length_km', 'average_score', 'average_time_minutes']
            writer.writerow(header)
        
            for route in list_routes:
                writer.writerow(route)
            
if __name__ == '__main__':
    Export.export_all_routes()