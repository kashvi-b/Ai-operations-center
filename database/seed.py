from faker import Faker
from models import *
from connection import SessionLocal
import random

fake = Faker()

db = SessionLocal()

for _ in range(200):

    customer = Customer(

        name=fake.name(),

        city=fake.city(),

        email=fake.email(),

        age=random.randint(20,70),

        monthly_revenue=random.randint(2000,100000),

        churn_probability=round(random.random(),2)
    )

    db.add(customer)

db.commit()

print("Customers Added")