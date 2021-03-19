from flask_sqlalchemy import SQLAlchemy
 
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

class BitModel(db.Model):
    __tablename__ = 'Bitcoin_Table'
 
    id = db.Column(db.Integer, primary_key = True)
    """
    date = db.column()
    tx_volume_usd = db.column()
    adjusted_tx_volume_usd = db.column()
    tx_count = db.column()
    marketcap_usd = db.column()
    price_usd = db.column()
    exchange_volume_usd = db.column()
    generated_coins = db.column()
    fees = db.column()
    active_addresses = db.column()
    avg_difficulty = db.column()
    payment_count = db.column()
    median_tx_value_usd = db.column()
    median_fee = db.column()
    block_size = db.column()
    Q_value = db.column()
    """

 
    def __init__(self, name,age):
        self.name = name
        self.age = age
 
    def __repr__(self):
        return f"{self.name}:{self.age}"