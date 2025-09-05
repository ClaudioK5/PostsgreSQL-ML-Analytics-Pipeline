import pandas as pd


def data_preprocesser(product, df):

    df_product = df[df['product_name'] == product]

    df_product['timestamp'] = pd.to_datetime(df_product['timestamp'])

    df_product['date_only'] = df_product['timestamp'].dt.floor('D')

    df_product['days_since_start'] = (df_product['date_only'] - df_product['date_only'].min()).dt.days

    daily_amounts = df_product.groupby('days_since_start')[['amount']].sum().reset_index()

    return daily_amounts
