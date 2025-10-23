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

