from flask import Flask, render_template, send_file, redirect, url_for, request
import os
import sys
import json
import merge_geojson
import war_api_interface
import requests

app = Flask(__name__)

@app.route("/")
def home():
	# war_api_interface.retrieve_api_json()
	return render_template('index.html')


@app.route('/<region>/<zoom>/<y>/<x>', methods=['GET'])
def tiles(region, zoom, y, x):
	print("Trying to load a tile")
	default = 'default.png' # this is a blank tile, change to whatever you want
	# max_y = len(os.listdir('test\\%s\\%s' % (zoom, x)))
	# filename = '%s\\%s\\%s\\%d.png' % (region, zoom, x, max_y - int(y))
	filename = '%s\\%s\\%s\\%s.png' % (region, zoom, x, y)
	if os.path.isfile(filename):
		print("Tile LOADED. CHAMPAGNE BOYS !")
		return send_file(filename)
	else:
		print("Impossible to load " + filename)
		return send_file(default)


@app.route('/tmp_json/recon', methods=['POST'])
def upload_recon():
	print("Uploading recon")
	data = request.get_json()
	print(type(data), data)
	with open("tmp_json/recon/recon.geojson", 'w') as file:
		json.dump(data, file)
	return "0"


@app.route('/tmp_json/removed', methods=['POST'])
def upload_removed():
	print("Uploading removed")
	data = request.get_json()
	print(type(data), data)
	with open("tmp_json/removed/removed.geojson", 'w') as file:
		json.dump(data, file)
	merge_geojson.run()
	return "0"

@app.route("/<file_name>", methods=['GET', 'POST'])
def load_js(file_name):
	print("Loading " + file_name)
	return send_file(file_name)


@app.route("/<path:filename>", methods=['GET', 'POST'])  # VERY DANGEROUS IN REAL WEB APP
def load_image(filename):
	if request.method == 'POST':
		# return 0
		pass
	else:
		print("Loading " + filename)
		return send_file(filename)


if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0', port=int(sys.argv[1]))
