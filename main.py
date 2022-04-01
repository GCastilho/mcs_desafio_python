import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

ipca = pd.read_excel('ipca.xlsx', parse_dates=['data'])

ipca_last_12_months = round(ipca.sort_values(by='data').tail(12)['valor'].sum(), 2)

@app.route('/')
def root():
	return jsonify({
		'ipca': ipca_last_12_months
	})

if __name__ == "__main__":
	app.run()
