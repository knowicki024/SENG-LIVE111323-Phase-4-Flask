#contains seed file, create instances 
from faker import Faker # add faker 
from random import choice as rc
from sqlalchemy import func

from app import app 
from models import Coffee, Customer, Order, db 

with app.app_context(): # create app context with app.app_context()
    Coffee.query.delete()
    Customer.query.delete()
    Order.query.delete()

    fake = Faker() # create and initialize a faker generator

    #create some seeds for coffee and commit them to the db
    cappuccino = Coffee(
        name="cappuccino",
        image="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Cappuccino_at_Sightglass_Coffee.jpg/440px-Cappuccino_at_Sightglass_Coffee.jpg",
        price=4.50,
        description="steamed milk and foam on top of a shot of espresso"
    )

    espresso = Coffee(
        name="espresso",
        image = "espresso.jpeg",
        price=3.50,
        description="the concentrated coffee, very strong!"
    )

    zaquari = Customer(
        name="Zaquari",
        address = fake.address(),
        phone = fake.phone_number(),
        emoji = fake.emoji()
    )

    o1 = Order(
            date=func.now(),
            customer=zaquari,
            coffee=cappuccino
        )
    
    db.session.add_all([cappuccino, zaquari, o1])
    db.session.commit()

    coffee_list = [] #create an empty list
    for c in range(250):
        cup = Coffee(
            name= rc(["Double Espresso", "Iced Americano", "Frappuccino", "Latte", "Macchiato", "Chai Latte", "Mocha", "Matcha"]),
            image = fake.image_url(),
            price = rc([3.50, 4.50, 4.00, 2.00, 1.50, 7.00, 4.00, 0.99]),
            description = fake.catch_phrase()
        )
        coffee_list.append(cup)

    customer_list = []
    for c in range(20):
        customer = Customer(
            name=fake.name(),
            address = fake.address(),
            phone = fake.phone_number(),
            emoji = fake.emoji()
        )
        customer_list.append(customer)

    db.session.add_all([cappuccino, espresso])
    db.session.add_all(coffee_list)
    db.session.add_all(customer_list)
    db.session.commit() #commit! 

    customer_rec = Customer.query.all()
    coffee_rec = Coffee.query.all()

    # Generate random instances for Order and store them in a list
    order_list = []
    for _ in range(100):
        order = Order(
            date=fake.date_time(),
            customer_id=rc([customer.id for customer in customer_rec]),
            coffee_id=rc([coffee.id for coffee in coffee_rec])
        )
        order_list.append(order)


    db.session.add_all(order_list)

    db.session.commit() #commit! 

    print(" DONE SEEDING!!👌🎍😍")