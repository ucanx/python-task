import requests
import argparse
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Color, Font, Alignment
import datetime

BASE_URL = "https://api.baubuddy.de/vehicles"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--keys", nargs="+", required=True, help="Keys to include as columns")
    parser.add_argument("-c", "--colored", action="store_true", help="Color rows based on HU age")
    args = parser.parse_args()

    # Read CSV data
    df = pd.read_csv("vehicles.csv")

    # API request
    response = requests.post(BASE_URL, files={'csv_file': open('vehicles.csv', 'rb')})
    response.raise_for_status()  # Raise an error if the request fails
    vehicles_data = response.json()

    # todo: Process data, create Excel, ...


if __name__ == "__main__":
    main()
