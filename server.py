from flask import Flask, request, jsonify
import requests
import pandas as pd

app = Flask(__name__)

BAUBUDDY_VEHICLES_URL = "https://api.baubuddy.de/dev/index.php/v1/vehicles/select/active"
BAUBUDDY_LABELS_URL = "https://api.baubuddy.de/dev/index.php/v1/labels/{labelId}"


@app.route("/api/vehicles", methods=["POST"])
def process_vehicles(result_data=None):
    csv_file = request.files['csv_file']
    csv_data = pd.read_csv(csv_file)

    # todo: Fetch vehicles, merge, filter, resolve colors, ...

    return jsonify(result_data)


if __name__ == "__main__":
    app.run(debug=True)  # Change debug=False for production
