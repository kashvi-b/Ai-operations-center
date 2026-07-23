from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy.orm import mapped_column


class Customer(Base):

    __tablename__ = "customers"

    id = mapped_column(Integer, primary_key=True)

    name = mapped_column(String)

    city = mapped_column(String)

    email = mapped_column(String)

    age = mapped_column(Integer)

    monthly_revenue = mapped_column(Float)

    churn_probability = mapped_column(Float)
class Supplier(Base):

    __tablename__ = "suppliers"

    id = mapped_column(Integer, primary_key=True)

    supplier_name = mapped_column(String)

    location = mapped_column(String)

    delivery_score = mapped_column(Float)

    risk_score = mapped_column(Float)
class Product(Base):

    __tablename__ = "products"

    id = mapped_column(Integer, primary_key=True)

    product_name = mapped_column(String)

    category = mapped_column(String)

    price = mapped_column(Float)

    stock = mapped_column(Integer)
from sqlalchemy import ForeignKey


class Order(Base):

    __tablename__ = "orders"

    id = mapped_column(Integer, primary_key=True)

    customer_id = mapped_column(
        ForeignKey("customers.id")
    )

    product_id = mapped_column(
        ForeignKey("products.id")
    )

    quantity = mapped_column(Integer)

    total_amount = mapped_column(Float)
class Shipment(Base):

    __tablename__ = "shipments"

    id = mapped_column(Integer, primary_key=True)

    supplier_id = mapped_column(
        ForeignKey("suppliers.id")
    )

    expected_days = mapped_column(Integer)

    actual_days = mapped_column(Integer)

    delayed = mapped_column(Integer)