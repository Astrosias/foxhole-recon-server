import os
import json

def run():
	abspath = os.path.abspath(".")
	# abspath = r"."
	original_geojson_path = r"recon.geojson"
	new_geojsons_path = r"tmp_json/recon"
	removed_geojsons_path = r"tmp_json/removed"

	all_new_files = os.listdir(new_geojsons_path)
	all_new_geojson = []

	for path_ in all_new_files:
		if path_.endswith(".geojson"):
			print(path_)
			all_new_geojson.append(os.path.join(new_geojsons_path, path_))

	all_removed_files = os.listdir(removed_geojsons_path)
	all_removed_geojson = []

	for path_ in all_removed_files:
		if path_.endswith(".geojson"):
			print(path_)
			all_removed_geojson.append(os.path.join(removed_geojsons_path, path_))

	if os.path.exists(original_geojson_path):
		with open(original_geojson_path, 'r') as j:
			original_geojson = json.loads(j.read())
	else:
		original_geojson = {"type": "FeatureCollection", "features": []}

	for feature in original_geojson["features"]:
		if feature["type"] == "FeatureCollection":
			# print(feature)
			for feature_ in feature["features"]:
				original_geojson["features"].append(feature_)
			original_geojson["features"].remove(feature)

	for path_ in all_new_geojson:
		print(path_)
		with open(path_, 'r') as j:
			geojson_tmp = json.loads(j.read())
		print(geojson_tmp)
		for feature in geojson_tmp["value"]["features"]:
			# print(feature)
			original_geojson["features"].append(feature)

	# for feature in original_geojson["features"]:
	# 	print(feature)

	for path_ in all_removed_geojson:
		with open(path_, 'r') as j:
			geojson_tmp = json.loads(j.read())
		for feature in geojson_tmp["value"]["features"]:
			print(feature)
			if feature is None:
				continue
			for feature_ in original_geojson["features"]:
				if "coordinates" in feature.keys() and "coordinates" in feature_.keys():
					if feature["coordinates"] == feature_["coordinates"] and feature['type'] == feature_["type"]:
						print("removing ", feature)
						original_geojson["features"].remove(feature)
						continue
				elif "geometry" in feature.keys() and "geometry" in feature_.keys():
					if feature["geometry"]["coordinates"] == feature_["geometry"]["coordinates"] and feature['type'] == \
							feature_["type"]:
						print("removing ", feature)
						original_geojson["features"].remove(feature)
						continue
			print(feature, " not removed")

	with open(original_geojson_path, 'w') as file:
		json.dump(original_geojson, file)

	print("Job done, geojsons merged")


if __name__ == "__main__":
	run()




