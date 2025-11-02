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

class Export:
    
    def __init__(self):
        pass
    
    
    # classmethod to export all routes to csv
    @classmethod
    def export_all_routes(cls):
        list_routes = Route.get_all()
        
        
        now = datetime.now()
        now_string = now.strftime("%Y%m%d%H%M%S")
        file_name = "export_routes_" + now_string + ".csv"
        print(file_name)
        
        with open(file_name, 'w',newline='') as file:
            writer = csv.writer(file, delimiter=';')
        
            for route in list_routes:
                pass
            
if __name__ == '__main__':
    Export.export_all_routes()