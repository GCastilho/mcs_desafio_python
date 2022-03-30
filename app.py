import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

ipca = pd.read_excel('ipca.xlsx', parse_dates=['data']).sort_values(by='data').tail(12)['valor'].sum()
ipca = round(ipca, 2)

@app.route('/')
def root():
	return jsonify({
		'ipca': ipca
	})

app.run()
