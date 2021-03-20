from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()
 
class InfoModel(db.Model):
    __tablename__ = 'info_table'
 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
 
    def __init__(self, name,age):
        self.name = name
        self.age = age
 
    def __repr__(self):
        return f"{self.name}:{self.age}"

class BitModel(db.Model, SerializerMixin):
    __tablename__ = 'bitcoin_table'

    serialize_only = ('id', 'price_usd', 'date')

 
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date())
    tx_volume_usd = db.Column(db.Float())
    adjusted_tx_volume_usd = db.Column(db.Float())
    tx_count = db.Column(db.Integer())
    marketcap_usd = db.Column(db.Float())
    price_usd = db.Column(db.Float())
    exchange_volume_usd = db.Column(db.Float())
    generated_coins = db.Column(db.Float())
    fees = db.Column(db.Float())
    active_addresses = db.Column(db.Integer())
    average_difficulty = db.Column(db.Float())
    payment_count = db.Column(db.Integer())
    median_tx_value_usd = db.Column(db.Float())
    median_fee = db.Column(db.Float())
    block_size = db.Column(db.Integer())
    
 
    def __init__(
        self,
        date,
        tx_volume_usd,
        adjusted_tx_volume_usd,
        tx_count,marketcap_usd,
        price_usd,
        exchange_volume_usd,
        generated_coins,
        fees,
        active_addresses,
        average_difficulty,
        payment_count,
        median_tx_value_usd,
        median_fee,
        block_size,
        ):
        self.date = date
        self.tx_volume_usd = tx_volume_usd
        self.adjusted_tx_volume_usd = adjusted_tx_volume_usd
        self.tx_count = tx_count
        self.exchange_volume_usd = exchange_volume_usd
        self.generated_coins = generated_coins
        self.fees = fees
        self.active_addresses = active_addresses
        self.average_difficulty = average_difficulty
        self.payment_count = payment_count
        self.median_tx_value_usd = median_tx_value_usd
        self.median_fee = median_fee
        self.block_size = block_size
 