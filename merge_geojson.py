import os
import json

abspath = os.path.abspath(".")

original_geojson_path = ""
new_geojsons_path = ""

all_new_files = os.listdir(new_geojsons_path)
all_new_geojson = []

for path_ in all_new_files:
	if path_.endswith(".geojson"):
		all_new_geojson.append(os.path.join(abspath, path_))

original_geojson = json.loads(original_geojson_path)


for path_ in all_new_geojson:
	geojson_tmp = json.loads(path_)
	for feature in geojson_tmp["features"]:
		original_geojson["features"].append(feature)





def retrieve_api_json():
	"""
	Get all the map data from the WAR API, and stores them in separate jsons for each region.
	:return:
	"""
	url = "https://war-service-live.foxholeservices.com/api/worldconquest/maps"
	req = requests.get(url)
	regions = req.json()

	geojon = {"type": "FeatureCollection", "features": []}

	for region in regions:
		# print(region)
		url_tmp = "https://war-service-live.foxholeservices.com/api/worldconquest/maps/{}/dynamic/public".format(region)
		req = requests.get(url=url_tmp)
		with open("json_data/{}.json".format(region), 'w') as file:
			json_tmp = req.json()
			json.dump(req.json(), file)
			for item in json_tmp['mapItems']:
				region = region.replace("Hex", "")
				coords = [item['x'] * coefx + region_to_offsets[region][0] * coefCol, item['y'] * coefy + region_to_offsets[region][1] * coefLine]
				gj_item = {"type": "Feature",
						   "properties": {"name": icon_dictionnary[str(item["iconType"])], "popupContent": "warapi", "teamId": item["teamId"]},
						   "geometry": {"type": "Point", "coordinates": [coords[0], coords[1]]}}
				geojon["features"].append(gj_item)
				# print(gj_item)
		with open(geojson_path, 'w') as file:
			json.dump(geojon, file)
