import time
import csv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, InfoModel, BitModel

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:test@localhost:5432/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/start')
def loop_entries():
    #This component is responsible for writing each entry to the database
    #Needs to loop through the csv and put each entry into database
    counter = 1

    with open('../docs/bitcoin_csv.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        #c=used to skip heading 
        for row in spamreader:
            if(counter!=1):
                print(row)
                time.sleep(1)
            else:
                counter = counter + 1
                pass

    new_entry = BitModel(
        name='name',
        age=6,
        date = 'Date',
        tx_volume_usd = 'Date',
        adjusted_tx_volume_usd = 'Date',
        tx_count = 'Date',
        marketcap_usd = 'Date',
        price_usd = 'Date',
        exchange_volume_usd = 'Date',
        generated_coins = 'Date',
        fees = 'Date',
        active_addresses = 'Date',
        avg_difficulty = 'Date',
        payment_count = 'Date',
        median_tx_value_usd = 'Date',
        median_fee = 'Date',
        block_size = 'Date',
        Q_value = 'Date',
        )
    db.session.add(new_entry)
    db.session.commit()
    time.sleep(1)
    return {}

@app.route('/time')
def get_current_time():
    new_user = InfoModel(name='name', age=6)
    db.session.add(new_user)
    db.session.commit()
    return {'time': time.time()}

if __name__ == '__main__':
    app.run(debug=True)