# week_05_python_project_travel_bucket

TRAVEL BUCKET PYTHON PROJECT README

THE PROJECTS BRIEF:

Travel Bucket List -
Build an app to track someone's travel adventures.

MVP:
The app should allow the user to track countries and cities they want to visit and those they have visited.
The user should be able to create and edit countries
Each country should have one or more cities to visit
The user should be able to create and delete entries for cities
The app should allow the user to mark destinations as visited or still to see

THE TECHNOLOGY USED:

HTML / CSS,
Python,
Flask,
PostgreSQL and the psycopg

RUNNING INSTRUCTIONS FOR THE APP:

* open the "app_end_point" folder in VS code
* create database "travel_bucket" (command "createdb travel_bucket" in terminal)
* in the Terminal run "psql -d travel_bucket -f db/travel_bucket.sql" command in terminal
* run "python3 console.py"
* check if the database's tables "cities" and "countries" appear in Postico
* run "flask run" command in terminal and follow the http link to open the app in the browser
* Press CTRL+C to quit flask 


