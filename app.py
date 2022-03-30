import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

ipca = pd.read_excel('ipca_com_tratativa.xlsx', parse_dates=['data']).sort_values(by='data').tail(12)['valor'].sum()

@app.route('/')
def root():
	return jsonify({
		'ipca': ipca
	})

app.run()
