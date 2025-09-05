from sqlalchemy.orm import Session
import pandas as pd
from data_utils import data_preprocesser
from ml_utils import forecast_and_plot_product_demand
from database import SessionLocal
from models import Customer, Order
from plot_utils import plot_generator

db: Session = SessionLocal()

query = (
    db.query(
        Order.id.label("order_id"),
        Order.product_name,
        Order.amount,
        Order.timestamp,
        Customer.id.label("customer_id"),
        Customer.name.label("customer_name"),
        Customer.email.label("customer_email"),
    )
    .join(Customer, Customer.id == Order.customer_id)

)


df = pd.read_sql(query.statement, db.bind)

product_list = df['product_name'].unique().tolist()


for product in product_list:

    daily_amounts = data_preprocesser(product, df)

    X , y, future_days, y_pred = forecast_and_plot_product_demand(daily_amounts, product)

    plot_generator(product, X, y, future_days, y_pred)

