## About
This project was a task given to me by a company as a challenge during the hiring process.
The concept of this project is to have 3 components working together to complete said task.

The task being have a csv file of pricing data written to a database and have the frontend actively 
reading from the database and updating a graphic to view the information


## Technologies
Linux(Ubuntu- Bionic Beaver), VScode(IDE), Flask(Python), React(Javascript,HTML,CSS)
Libraires of note: SQLAlchemy, Nivo

## Needed steps for Demonstration
    Have a clear database
    npm start - start frontend 
    flask run - start backend

## Database
    psql -U postgres
    
    Credentials in a env file
    Using a simple starter database, which I will be using postgresql - 

    postgres username
    test password


## Startup

    Two Commands are required to function
    if needed: 
    export FLASK_APP=api.py

    Startup React -> npm start
    Startup Flask Backend -> 
        cd /api
        source venv/bin/activate -> enter vm for versioning reasons
        flask run
## Future Additions
Add a means to pause the writing to DB instead of infinite loop.
Add a snackbar response for requests(Error and Success).
More Styling.
