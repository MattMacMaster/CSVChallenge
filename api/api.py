import time
import csv
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, InfoModel, BitModel

from sqlalchemy.ext.declarative import DeclarativeMeta

def new_alchemy_encoder():
    _visited_objs = []

    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if obj in _visited_objs:
                    return None
                _visited_objs.append(obj)

                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    fields[field] = obj.__getattribute__(field)
                # a json-encodable dict
                return fields

            return json.JSONEncoder.default(self, obj)

    return AlchemyEncoder

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:test@localhost:5432/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

#This is solely used to begin the write process to the database
@app.route('/start')
def loop_entries():
    #This component is responsible for writing each entry to the database
    #Needs to loop through the csv and put each entry into database
    counter = 1
    while True:
        with open('../docs/bitcoin_csv.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            #counter used to skip heading 
            #Empty needs to be converted to None Type
            for row in spamreader:
                if(counter!=1 and row[5] != ''):
                    print(row)

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

@app.route('/query')
def get_data():
    value = db.session.query(BitModel).filter(BitModel.price_usd != None)
    #BitModels are not serializable so built workaround
    serialized = []
    for x in value:
        serialized.append(x.to_dict())
    return {'data':serialized}
if __name__ == '__main__':
    app.run(debug=True)