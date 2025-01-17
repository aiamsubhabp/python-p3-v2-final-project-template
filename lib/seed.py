#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.manufacturer import Manufacturer
from models.product import Product

def seed_database():
    Product.drop_table()
    Manufacturer.drop_table()
    Manufacturer.create_table()
    Product.create_table()

    # Create seed data
    toyota = Manufacturer.create('Toyota', 'Automobiles')
    ford = Manufacturer.create('Ford', 'Automobiles')
    honda = Manufacturer.create('Honda', 'Automobiles')
    sony = Manufacturer.create('Sony', 'Electronics')
    samsung = Manufacturer.create('Samsung', 'Electronics')
    apple = Manufacturer.create('Apple', 'Technology')
    google = Manufacturer.create('Google', 'Technology')

    corolla = Product.create('Toyota Corolla', 'Automobile', toyota.id)
    tacoma = Product.create('Toyota Tacoma', 'Autombile', toyota.id)
    camry = Product.create('Toyota Camry', 'Automobile', toyota.id)
    runner = Product.create('Toyota 4Runner', 'Automobile', toyota.id)
    prius = Product.create('Toyota Prius', 'Automobile', toyota.id)
    tundra = Product.create('Toyota Tundra', 'Automobile', toyota.id)
    civic = Product.create('Honda Civic', 'Automobile', honda.id)
    raptor = Product.create('Ford Raptor', 'Automobile', ford.id)
    escape = Product.create('Ford Escape', 'Automobile', ford.id)
    expedition = Product.create('Ford Expedition', 'Automobile', ford.id)
    ps5 = Product.create('Playstation 5', 'Videogames', sony.id)
    wh1000xm5 = Product.create('WH-1000XM5', 'Headphones', sony.id)
    galaxy_s = Product.create('Samsung Galaxy S', 'Cell Phone', samsung.id)
    iphone_15_pro = Product.create('iPhone 15 Pro', 'Cell Phone', apple.id)
    pixel_8 = Product.create('Google Pixel 8', 'Cell Phone', google.id)

seed_database()
print('Seeded database')



    

