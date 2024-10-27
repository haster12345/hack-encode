from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd

app = Flask(__name__, static_folder="static")
CORS(app)


# Route for serving index.html
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


# Route for fetching stock data
@app.route('/data', methods=['GET'])
def get_stock_data():
    try:
        df = pd.read_csv('stonks.csv')
        df['Date'] = pd.to_datetime(df['Date'])  # Convert to datetime
        original_price = df['Stock Price'].iloc[0]  # Get the first price for relative value calculation

        data = []
        for i in range(len(df)):
            relative_value = df['Stock Price'].iloc[i] / original_price  # Calculate relative value
            data.append({
                'Date': df['Date'].iloc[i].strftime('%Y-%m-%d'),  # Format date
                'Stock Price': df['Stock Price'].iloc[i],
                'Relative Stock Value': relative_value
            })

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
