import requests
import json

geojson_path = "warapi.geojson"

ratio = (40960 - 10230)/35520
coef = 296
coefCol, coefLine = coef * ratio, coef * -1
ratio = 40960/35520
coefx, coefy = coef * ratio, coef * -1
region_to_offsets = {'Acrithia': (4, 5.5), 'AllodsBight': (5, 4), 'AshFields': (1, 5), 'BasinSionnach': (3, 0), 'CallahansPassage': (3, 2),
		   'CallumsCape': (1, 1), 'ClansheadValley': (5, 1), 'DeadLands': (3, 3), 'DrownedVale': (4, 3.5), 'EndlessShore': (5, 3),
		   'FarranacCoast': (1, 3), 'FishermansRow': (0, 3.5), 'Godcrofts': (6, 2.5), 'GreatMarch': (3, 5), 'Heartlands': (2, 4.5),
		   'HowlCounty': (4, 0.5), 'Kalokai': (3, 6), 'LinnMercy': (2, 2.5), 'LochMor': (2, 3.5), 'MarbanHollow': (4, 2.5),
		   'MooringCounty': (2, 1.5), 'MorgensCrossing': (6, 1.5), 'NevishLine': (0, 1.5), 'Oarbreaker': (0, 2.5), 'Origin': (0, 4.5),
		   'ReachingTrail': (3, 1), 'RedRiver': (2, 5.5), 'ShackledChasm': (4, 4.5), 'SpeakingWoods': (2, 0.5), 'Stonecradle': (1, 2),
		   'TempestIsland': (6, 3.5), 'Terminus': (5, 5), 'TheFingers': (6, 4.5), 'UmbralWildwood': (3, 4), 'ViperPit': (4, 1.5),
		   'WeatheredExpanse': (5, 2), 'Westgate': (1, 4)}

icon_dictionnary = {"8": "ForwardBase", "11": "Medical", "12": "Vehicle", "17": "Manufacturing", "18": "Shipyard",
					"20": "Salvage", "21": "Components", "22": "OilWell", "23": "Sulfur", "27": "Keep", "28": "ObservationTower",
					"32": "SulfurMine", "33": "StorageFacility", "34": "Factory", "35": "SafeHouse", "37": "RocketSite", "38": "SalvageMine",
					"39": "ConstructionYard", "40": "ComponentMine", "47": "RelicBase", "51": "MassProductionFactory",
					"52": "Seaport", "53": "CoastalGun", "54": "SoulFactory", "56": "StaticBase1", "57": "StaticBase2", "58": "StaticBase3",
					"59": "StormCannon", "60": "IntelCenter", "61": "Coal", "62": "Fuel", "19": "TechCenter", "45": "RelicBase"}


class JsonMaker:

	def __int__(self):
		self.all_war_json = []
		self.war_url = "https://war-service-live.foxholeservices.com/api/worldconquest/maps"
		req = requests.get(self.war_url)
		self.regions = req.json()
		pass

	def retrieve_all_json(self):
		for region in self.regions:
			# print(region)
			url_tmp = "{}}/{}/dynamic/public".format(self.war_url, region)
			req = requests.get(url=url_tmp)
			self.all_war_json.append(req.json())
			with open("json_data/{}.json".format(region), 'w') as file:
				json.dump(req.json(), file)

	def create_geojson(self):
		pass


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


if __name__ == "__main__":
	retrieve_api_json()
