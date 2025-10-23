# -*- coding: utf-8 -*-
"""
Database testing script

Created on Thu Oct 23 14:47:47 2025

@author: thomas brockmans
"""

import sqlite3
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# get database path from dotenv
database_path = os.getenv('DATABASE_PATH', 'velog.db')


# method to test connection
def test_database_connection():
    try:
        connection = sqlite3.connect(database_path)
        print(f"Succesfully connected to database: {database_path}")
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None
    

# method to check existence of tables (from list)
def test_tables_exist(connection):
    cursor = connection.cursor()
    
    required_tables = ['weather_types', 'types', 'routes', 'rides']
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    existing_tables = [row[0] for row in cursor.fetchall()]
    
    print("\n")
    print("=" * 60)
    print("Table existence check:")
    print("=" * 60)
    
    for table in required_tables:
        if table in existing_tables:
            print(f"   Table '{table}' exists")
        else:
            print(f"   Table '{table}' NOT FOUND")
    
    return existing_tables

        
    
# method to count records for each table
def count_records(connection, table_name):
    cursor = connection.cursor()
    
    try:
        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
        count = cursor.fetchone()[0]
        print(f"   Records in '{table_name}': {count}")
        return count
    except sqlite3.Error as e:
        print(f"   Error counting records in {table_name}: {e}")
        
     
        
# main method of the script
def main():
    print("=" * 60)
    print("VELOG Database Test Script")
    print("=" * 60)
    
    connection = test_database_connection()
    if not connection:
        return

        
    existing_tables = test_tables_exist(connection)
                
    
    print("\n" + "=" * 60)
    print("Record counts:")
    print("=" * 60)
    for table in existing_tables:
        if table != 'sqlite_sequence':
            count_records(connection, table)
            
    connection.close()
    print("\n Database connection closed")
    print("=" * 60)
    
if __name__ == '__main__':
    main()