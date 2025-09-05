import matplotlib.pyplot as plt
import boto3
from io import BytesIO


def plot_generator(product, X, y, future_days, y_pred):


    s3 = boto3.client("s3")

    plt.figure(figsize=(10, 5))

    plt.plot(X, y, marker='o', color='blue', label=f'Actual Sales - {product}')

    plt.plot(future_days, y_pred, marker='o', color='red', label='Predicted points')

    plt.title(f"Demand Prediction + Statistics for {product}")
    plt.xlabel("Days Since Start")
    plt.ylabel("Amount Sold")
    plt.legend()
    plt.grid(True)
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    file_name = f"graphs/{product}_statistics+prediction.png"

    s3.upload_fileobj(buffer, 'pythonaswbucket', file_name)

    plt.figure(figsize=(10, 5))
    plt.plot(X, y, marker='o', color='blue', label=f'Actual Sales - {product}')

    plt.title(f"Demand statistics for {product}")

    plt.xlabel("Days Since Start")
    plt.ylabel("Amount Sold")
    plt.legend()
    plt.grid(True)
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    file_name = f"graphs/{product}_demand_statistics.png"

    s3.upload_fileobj(buffer, 'pythonaswbucket', file_name)

    plt.figure(figsize=(10, 5))
    plt.plot(future_days, y_pred, marker='o', color='red', label='Predicted points')

    plt.title(f"Demand Prediction for {product}")
    plt.xlabel("Days Since today")
    plt.ylabel("Amount Sold")
    plt.legend()
    plt.grid(True)
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    file_name = f"graphs/{product}_prediction.png"

    s3.upload_fileobj(buffer, 'pythonaswbucket', file_name)