# VELOG
a command line bike ride logging application in python

## Features

## How to run

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

