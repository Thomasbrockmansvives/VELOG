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

def test_database_connection():
    try:
        connection = sqlite3.connect(database_path)
        print(f"Succesfully connected to database: {database_path}")
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None
    

def test_tables_exist(connection):
    cursor = connection.cursor()
    
    required_tables = ['weather_types', 'types', 'routes', 'rides']
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    existing_tables = [row[0] for row in cursor.fetchall()]
    
    print("\nTable existence check:")
    for table in required_tables:
        if table in existing_tables:
            print(f"Table '{table}' exists")
        else:
            print(f"Table '{table}' NOT FOUND")
    
    return existing_tables


def show_table_structure(connection, table_name):
    cursor = connection.cursor()
    
    try:
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        
        print(f"\nStructure of table '{table_name}':")
        print("-" * 60)
        for col in columns:
            col_id, name, col_type, not_null, default, pk = col
            pk_str = " (PRIMARY KEY)" if pk else ""
            not_null_str = " NOT NULL" if not_null else ""
            print(f" {name}: {col_type}{pk_str}{not_null_str}")
            
        cursor.execute(f"PRAGMA foreign_key_list({table_name});")
        fks = cursor.fetchall()
        if fks:
            print("\n Foreign Keys:")
            for fk in fks:
                fk_id, sed, ref_table, from_col, to_col = fk[0:5]
                print(f"   {from_col} -> {ref_table}({to_col})")
                
    except sqlite3.Error as e:
        print(f"Error getting structure for {table_name}: {e}")
        
        
def count_records(connection, table_name):
    cursor = connection.cursor()
    
    try:
        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
        count = cursor.fetchone()[0]
        print(f"   Records in '{table_name}': {count}")
        return count
    except sqlite3.Error as e:
        print(f"   Error counting records in {table_name}: {e}")
        
        
def main():
    print("=" * 60)
    print("VELOG Database Test Script")
    print("=" * 60)
    
    connection = test_database_connection()
    if not connection:
        return
    
    
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys;")
    fk_enabled = cursor.fetchone()[0]
    print(f"Foreign keys enabled: {'Yes' if fk_enabled else 'No'}")
    
    existing_tables = test_tables_exist(connection)
    
    for table in existing_tables:
        if table != 'sqlite_sequence':
            show_table_structure(connection, table)
            
    
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