# VELOG 🚴🚴‍♂️🚴‍♀️
a command line bike ride logging application in python

## 📃 FEATURES
- the user can log rides (with a score, weather type, time and which route they took)
- the user can update or delete existing rides
- the user can create new routes (templates for rides)
- the user can view the 5 most recent rides on startup
- the user can view all rides or all rides for a specific route
- the user can ask for an export in csv of the ride loggings and the routes available

## 🔧 INSTALLATION INSTRUCTIONS
**after cloning from the remote repository:**
- create a .venv (python -m venv .venv)
- activate the virtual environment
- install the requirements.txt (pip install -r requirements.txt)
- create a .env file in the root directory with the correct path to the database
  - add: DATABASE_PATH=velog.db (or your custom path)
- ensure your SQLite database (velog.db) is in the project root directory

## ✏️ APPLICATION DESIGN

We are using some classes with each their own encapsulated logic. Each class handles its own database operations, so there is no separate database class for this:
- **Layout Class**: a class for user interactions: options menu, welcome message, splash screen, handling user inputs and calling the separate class methods
- **Ride Class**: representing a single bike ride with the same attributes as in database and methods like create, read, update, delete
- **Route Class**: representing a bike route with the same attributes as in database and methods like create, read, calculate_averages
- **Export Class**: generating CSV reports, with methods like export_all_rides and export_all_routes

### CLASS STRUCTURE

#### ROUTE CLASS
##### Attributes:
&nbsp;&nbsp;&nbsp; route_id, start, destination, version, type_id, length_km, average_score, average_time_minutes

##### Methods:
- create()
- calculate_averages()
- get_all()
- get_by_id()
- route_exists()

##### Operations:
- **Create new route:**   main.create_a_new_route() > new_route() > new_route.create() > database operation > print success message <br>
- **Show all routes:**   main.route_options() > Layout.print_all_routes() > Route.get_all() > database operation > display routes <br>


#### RIDE CLASS
##### Attributes: 
&nbsp;&nbsp;&nbsp; ride_id, route_id, date, start_time, end_time, score, weather_id
##### Methods:
- create()
- update()
- delete_by_id()
- get_all()
- get_last_n()
- get_by_id()
- get_rides_by_route_id()
- calculate_duration()

##### Operations:
- **Log a ride:** main.log_a_new_ride() > new_ride() > new_ride.create() > database operation > print success message
- **Show last 5 rides:** main.startup_application() > Layout.print_5_most_recent_rides() > Ride.get_last_n(5) > database operation > display rides
- **Modify a ride:** main.update_a_ride() > Ride.get_by_id() > database operation > collect new values by input > ride.update() > database operation > Route.calculate_averages() > print success message
- **Delete a ride:** main.delete_a_ride() > Ride.delete_by_id() > database operation > print success message

#### EXPORT CLASS
##### Methods:
- export_all_rides()
- export_all_routes()

##### Operations:
- **Export routes:** main.export_routes() > Export.export_all_routes() > Route.get_all() > database operation > csv file operation > print success message
- **Export rides:** main.export_rides() > Export.export_all_rides() > Ride.get_all() > database operation > csv file operation > print success message


#### LAYOUT CLASS
##### Methods:
- splash_screen()
- print_5_most_recent_rides()
- print_title()
- print_text()
- print_line()
- print_continue()
- print_main_options()
- print_all_rides()
- print_ride_options()
- print_all_routes()
- print_all_rides_by_route()
- print_weather()
- print_route_types()
- print_route_options()


## 🗄️ DATABASE
### DB CONNECTION
&nbsp;&nbsp;&nbsp;the application uses a '.env' file to store configuration settings.

   1. Create a .env file in the root directory of the project
   2. Add the configuration: DATABASE_PATH=velog.db (modify if you placed the database elsewhere)

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

&nbsp;&nbsp;&nbsp;**routes (1) ------------- (many) rides** <br>
&nbsp;&nbsp;&nbsp;**weather_types (1) -------------- (many) rides**
<br>

### DATA FLOW
&nbsp;&nbsp;&nbsp;when a ride is logged, the application stores it in the database. When a ride is updated or deleted, the application recalculates and updates the average_score and average_time_minutes in the routes table using Route.calculate_averages()

## 🚀 USAGE
Run the application from the project root directory:
```bash
python main.py
```

The application will:
1. Display a splash screen with the VELOG logo
2. Show the 5 most recent rides
3. Present a main menu with options to:
   - Log a new ride
   - Show all rides (with options to update, delete, or export)
   - Show all routes (with options to create, view rides by route, or export)
   - Create a new route
   - Close the application

## 📁 PROJECT STRUCTURE
```
velog/
├── main.py              # Main application script with user interface logic
├── models/
│   ├── ride.py          # Ride class definition and methods
│   ├── route.py         # Route class definition and methods
│   ├── layout.py        # Layout class for UI formatting
│   └── export.py        # Export class for CSV generation
├── Export/              # Directory for CSV exports (created automatically)
├── velog.db             # SQLite database
├── .env                 # Environment configuration (DATABASE_PATH)
├── .venv/               # Virtual environment
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## 📋 REQUIREMENTS
This application meets the following project requirements:
- ✅ Git version control with remote repository on GitHub
- ✅ Sensitive data stored in .env file
- ✅ SQLite database with 4 tables (weather_types, types, routes, rides)
- ✅ Application modifies and adds rows to the database
- ✅ CSV export functionality for rides and routes
- ✅ Object-oriented design with classes (Route, Ride, Export, Layout)
- ✅ Terminal-based user interaction
- ✅ Modular structure with separate model files
- ✅ Virtual environment setup
- ✅ Requirements.txt with all dependencies