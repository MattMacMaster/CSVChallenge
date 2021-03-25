import time
import csv
import os
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, BitModel
import psycopg2
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import DeclarativeMeta
from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
#Load ENV variables
load_dotenv(dotenv_path=env_path)


#Setting up Database configurations - Add to ENV 
app = Flask(__name__)
databaseString = "postgresql://" + os.getenv('POSTGRES_USER') +"}:" + os.getenv('POSTGRES_PASSWORD') + "@localhost:5432/" + os.getenv('DB_NAME') + "}"
app.config['SQLALCHEMY_DATABASE_URI'] = databaseString
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

#This route will begin the infinite loop of writing to the DB
@app.route('/start')
def loop_entries():
    #This component is responsible for writing each entry to the database
    #Needs to loop through the csv and put each entry into database
    counter = 1
    while True:
        with open('../docs/bitcoin_csv.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            #Empty needs to be converted to None Type or it will fail
            for row in spamreader:
                if(counter!=1 and row[5] != ''):
                    #Taking a row and assigning it to its respective value in the model
                    new_entry = BitModel(
                    date = row[0] if row[0] != '' else None,
                    tx_volume_usd = row[1] if row[1] != '' else None,
                    adjusted_tx_volume_usd = row[2] if row[2] != '' else None,
                    tx_count = row[3] if row[3] != '' else None,
                    marketcap_usd = row[4] if row[4] != '' else None,
                    price_usd = row[5] if row[5] != '' else None,
                    exchange_volume_usd = row[6] if row[6] != '' else None,
                    generated_coins = row[7] if row[7] != '' else None,
                    fees = row[8] if row[8] != '' else None,
                    active_addresses = row[9] if row[9] != '' else None,
                    average_difficulty = row[10] if row[10] != '' else None,
                    payment_count = row[11] if row[11] != '' else None,
                    median_tx_value_usd = row[12] if row[12] != '' else None,
                    median_fee = row[13] if row[13] != '' else None,
                    block_size = row[14] if row[14] != '' else None,
                    )       
                    db.session.add(new_entry)
                    db.session.commit()
                    
                    time.sleep(1)
                else:
                    counter = counter + 1
                    pass

        return {}

#This route is for querying and serializing the data and returning it to the frontend
@app.route('/query')
def get_data():
    value = db.session.query(BitModel).filter(BitModel.price_usd != None).order_by(BitModel.date)
    #BitModels are not serializable so built workaround
    serialized = [{"data": []}]

    for x in value:
        value = x.to_dict()
        value["x"] = value.pop("date")
        value["y"] = value.pop("price_usd")
        serialized[0]["data"].append(value)
    return {'data':serialized}

#Connects and drops and then reistablishes the DB table
@app.route('/clear')
def reset_db():
    conn = psycopg2.connect("dbname=flask user={0} password={1}".format(os.getenv('POSTGRES_USER'),os.getenv('POSTGRES_PASSWORD')))
    cur = conn.cursor()
    #Drop the current table
    cur.execute("DROP TABLE {0};".format(os.getenv('TABLE_NAME')))
    #Restablish it
    cur.execute("""
    CREATE TABLE {0} (
    ID SERIAL PRIMARY KEY NOT NULL,
    DATE DATE NOT NULL,
    TX_VOLUME_USD REAL ,
    ADJUSTED_TX_VOLUME_USD REAL ,
    TX_COUNT INT , 
    MARKETCAP_USD DOUBLE PRECISION ,
    PRICE_USD FLOAT ,
    EXCHANGE_VOLUME_USD FLOAT ,
    GENERATED_COINS DOUBLE PRECISION ,
    FEES DOUBLE PRECISION ,
    ACTIVE_ADDRESSES INT ,
    AVERAGE_DIFFICULTY DOUBLE PRECISION ,
    PAYMENT_COUNT BIGINT ,
    MEDIAN_TX_VALUE_USD DOUBLE PRECISION ,
    MEDIAN_FEE DOUBLE PRECISION ,
    BLOCK_SIZE BIGINT ,
    BLOCK_COUNT INT 
);
    """.format(os.getenv('TABLE_NAME')))

    conn.commit()
    cur.close()
    conn.close()

    return {}

if __name__ == '__main__':
    app.run(debug=True)