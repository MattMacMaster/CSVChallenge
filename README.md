## Assumptions
All entries are database viable, but when querying from the database, we only query for ones with a price and display them.

## Technologies
Linux(Ubuntu), VScode, Flask(Python), React(Javascript)
SQLAlchemy
## Needed steps for Demonstration
    Cleared Database
    npm start
    flask run

## Startup
    Two Commands are required to function
    Startup React -> npm start
    Startup Flask Backend -> 
        cd /api
        source venv/bin/activate -> enter vm for versioning reasons
        flask run

## TODO LIST in order
    Connect to postgresDB from flask
    make models for data(bitcoin)
    have some test data implemented
    Loops every x and updates frontend data when new data is added

    CSV WRITER to database
    Loops over the csv file and writes it to DB
    Is done in 1 sec intervals
