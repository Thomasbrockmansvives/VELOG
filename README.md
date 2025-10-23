# VELOG
a command line bike ride logging application in python

## Features

## How to run

## Database structure

**Filename:** velog.db
**Location:** Project root directory
**Foreign Keys:** Enabled by default


### Table 'weather_types'
weather_id (PK): integer
weather_name: text

### Table 'types'
type_id (PK): integer
type_name: text

### Table 'routes'
route_id (PK): integer
start: text
destination: text
version: integer
type_id (FK)
length_km: real
average_score: real
average_time_minutes: integer

types (1) --------------- (many) routes

### Table 'rides'
ride_id (PK): integer
route_id (FK)
date: text
start_time: text
end_time: text
score: integer
weather_id (FK)

routes (1) ------------- (many) rides
weather_types (1) -------------- (many) rides

### Data Flow
when a ride is logged, the application also recalculates and updates the average_score and average_time_minutes in routes

