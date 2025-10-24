# VELOG
a command line bike ride logging application in python

## Features
the user can log rides (with a score, weather type, time and which route he took)
the user can also create new or modify existing routes (templates for rides)
the user can ask for an export in csv of the ride loggings, the routes availables and a summary of his biking history

## How to install
after cloning from the remote repository
create a .venv (python -m venv .venv)
activate the virtual environment
install the requirements.txt (pip install -r requirements.txt)

## Application Design

We are using some classes with each their own encapsulated logic. Each class handles its own database operations, so their is no separate database class for this:
- UI Class: a class for user interactions: options menu, welcome message, handling user inputs and calling the separate class methods.
- Ride Class: representing a single bike ride with the same attributes as in database and methods like save, read, update, delete
- Route Class: representing a bike route with the same attributes as in database and methods like save, read, update
- Report Class: generating CSV reports, with methods like export_all_rides, export_all_routes and export_summary

### Class Structure

#### UI Class
includes main.py
**Methods:** welcome_message(), display_menu(), run()

#### Route Class
**Attributes:** route_id, start, destination, version, type_id, length_km, average_score, average_time_minutes
**Methods:** save(), update(), calculate_averages(), get_all(), get_by_id()
##### Operations:
**Create new route:** main.create_route() > new_route() > new_route.save() > database operation > print success message
**Show all routes:** main.show_routes() > routes[] = Route.get_all() > database operation > print routes[]
**Modify route:** main.modify_route() > route = Route.get_by_id() > database operation > collect new values by input > route.update() > database operation > print success message


#### Ride Class
**Attributes:** ride_id, route_id,date, start_time, end_time, score, weather_id
**Methods:** save(), update(), delete(), get_all(), get_last_n(), get_by_id(), get_by_route(), update_route_averages(),calculate_duration()

#### Report Class
**Methods:** export_all_rides(), export_all_routes(), export_summary()









## Database connection
the application uses a '.env' file to store configuration settings.

1. Create a .env file in the root directory of the project
2. Add the configuration as shown in example_env (modify if you placed the database elsewhere)

The database can be tested with the db_testing.py script.
This script tests the connections, checks the existence of the required tables and counts the records in the database.

## Database structure

**Filename:** velog.db <br>
**Location:** Project root directory <br>
**Foreign Keys:** Enabled by default <br>


### Table 'weather_types'
weather_id **(PK)**: integer <br>
weather_name: text <br>

### Table 'types'
type_id **(PK)**: integer <br>
type_name: text <br>

### Table 'routes'
route_id **(PK)**: integer <br>
start: text <br>
destination: text <br>
version: integer <br>
type_id **(FK)** <br>
length_km: real <br>
average_score: real <br>
average_time_minutes: integer <br>
 <br>
types (1) --------------- (many) routes

### Table 'rides'
ride_id **(PK)**: integer <br>
route_id **(FK)** <br>
date: text <br>
start_time: text <br>
end_time: text <br>
score: integer <br>
weather_id **(FK)** <br>
 <br>
routes (1) ------------- (many) rides <br>
weather_types (1) -------------- (many) rides <br>

### Data Flow
when a ride is logged, the application also recalculates and updates the average_score and average_time_minutes in routes

