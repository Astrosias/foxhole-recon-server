from flask import Flask, render_template, send_file
import os
import sys

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('index.html')


@app.route("/<file_name>")
def load_js(file_name):
	print("Loading " + file_name)
	return send_file(file_name)


@app.route('/<region>/<zoom>/<y>/<x>', methods=['GET', 'POST'])
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
		return send_file(default)\


@app.route("/<path:filename>")  # VERY DANGEROUS IS REAL WEB APP
def load_image(filename):
	print("Loading " + filename)
	return send_file(filename)


if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0', port=int(sys.argv[1]))
