# VELOG 🚴🚴‍♂️🚴‍♀️
a command line bike ride logging application in python

## 📃 FEATURES
- the user can log rides (with a score, weather type, time and which route he took)
- the user can also create new or modify existing routes (templates for rides)
- the user can ask for an export in csv of the ride loggings and the routes availables

## 🔧 INSTALLATION INSTRUCTIONS
**after cloning from the remote repository:**
- create a .venv (python -m venv .venv)
- activate the virtual environment
- install the requirements.txt (pip install -r requirements.txt)

## ✏️ APPLICATION DESIGN

We are using some classes with each their own encapsulated logic. Each class handles its own database operations, so their is no separate database class for this:
- UI Class: a class for user interactions: options menu, welcome message, handling user inputs and calling the separate class methods.
- Ride Class: representing a single bike ride with the same attributes as in database and methods like save, read, update, delete
- Route Class: representing a bike route with the same attributes as in database and methods like save, read
- Report Class: generating CSV reports, with methods like export_all_rides and export_all_routes

### CLASS STRUCTURE

#### UI CLASS

##### Methods:
- welcome_message()
- display_menu()

#### ROUTE CLASS
##### Attributes:
&nbsp;&nbsp;&nbsp; route_id, start, destination, version, type_id, length_km, average_score, average_time_minutes

##### Methods:
- create()
- calculate_averages()
- get_all()
- get_by_id()

##### Operations:
- **Create new route:**   main.create_route() > new_route() > new_route.save() > database operation > print success message <br>
- **Show all routes:**   main.show_routes() > routes[] = Route.get_all() > database operation > print routes[] <br>


#### RIDE CLASS
##### Attributes: 
&nbsp;&nbsp;&nbsp; ride_id, route_id,date, start_time, end_time, score, weather_id
##### Methods:
- save()
- update()
- delete()
- get_all()
- get_last_n()
- get_by_id()
- get_by_route()
- update_route_averages()
- calculate_duration()

##### Operations:
- **Log a ride:** main.create_ride() > new_ride() > new.ride_save() > database operation > new_ride.update_route_averages() > database operation > print success message
- **Show last 10 rides:** main.show_last_rides() > rides[] = Ride.get_last_n(10) > database operation > print rides[]
- **Modify a ride:** main.update_ride() > ride = Ride.get_ride_by_id() > database operation > collect new values by input > ride.update() > database operation > ride.update_route_averages() > print success message
- **Delete a ride:** main.delete_ride() > ride = Ride.get_ride_by_id() > database operation > confirm deletion by input > route_id = ride.route_id > ride.delete() > database operation > route = Route.get_by_id(route_id) > database operation > route.calculate_averages() > database operation > print success message

#### REPORT CLASS
##### Methods:
- export_all_rides()
- export_all_routes()

##### Operations:
- **Export routes:** main.export_routes() > routes[] = Route.get_all() > database operation > Report.export_all_routes(routes) > csv file operation > print success message
- **Export rides:** main.export_rides() > rides[] = Ride.get_all() > database operation > Report.export_all_rides(rides) > csv file operation > print success message

## 🗄️ DATABASE
### DB CONNECTION
&nbsp;&nbsp;&nbsp;the application uses a '.env' file to store configuration settings.

   1. Create a .env file in the root directory of the project
   2. Add the configuration as shown in example_env (modify if you placed the database elsewhere)

&nbsp;&nbsp;&nbsp;The database can be tested with the db_testing.py script. <br>
&nbsp;&nbsp;&nbsp;This script tests the connections, checks the existence of the required tables and counts the records in the database. <br>

### DB STRUCTURE

- **Filename:** velog.db
- **Location:** Project root directory
- **Foreign Keys:** Enabled by default


### TABLE 'WEATHER_TYPES'
- weather_id **(PK)**: integer
- weather_name: text

### TABLE 'TYPES'
- type_id **(PK)**: integer
- type_name: text

### TABLE 'ROUTES'
- route_id **(PK)**: integer
- start: text
- destination: text
- version: integer
- type_id **(FK)**
- length_km: real
- average_score: real
- average_time_minutes: integer
  
&nbsp;&nbsp;&nbsp;**types (1) --------------- (many) routes**

### TABLE 'RIDES'
- ride_id **(PK)**: integer
- route_id **(FK)**
- date: text
- start_time: text
- end_time: text
- score: integer
- weather_id **(FK)**
- <br>

&nbsp;&nbsp;&nbsp;**routes (1) ------------- (many) rides** <br>
&nbsp;&nbsp;&nbsp;**weather_types (1) -------------- (many) rides**
<br>

### DATA FLOW
&nbsp;&nbsp;&nbsp;when a ride is logged, the application also recalculates and updates the average_score and average_time_minutes in routes

