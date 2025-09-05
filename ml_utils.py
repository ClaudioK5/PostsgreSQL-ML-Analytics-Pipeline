from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import numpy as np


def forecast_and_plot_product_demand(daily_amounts, product):

    X = daily_amounts[['days_since_start']]
    y = daily_amounts[['amount']]

    degree = 2
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())

    model.fit(X, y)

    future_days = np.arange(X['days_since_start'].max() + 1, X['days_since_start'].max() + 9).reshape(-1,1)

    y_pred = model.predict(future_days)

    return X, y, future_days, y_pred

