#!/usr/bin/python3
import json
import pygeohash as pgh
import random
from difflib import get_close_matches
class ManageGeocoordinate:
    __file_path = 'nyu_geojson.json'

    @staticmethod
    def reload():
        coordinates = []
        try:
            with open(ManageGeocoordinate.__file_path, 'r') as f:
                objdict = json.load(f)
                for f in objdict["features"]:
                    coordinates.append(f["geometry"]["coordinates"])
                #print(coordinates)

        except FileNotFoundError:
            return
        return coordinates

    @staticmethod
    def encode_coordinate(arr):
        return pgh.encode(arr[0],arr[1])

    @staticmethod
    def genarate_has():
        coordinate_with_hash = {}
        for element in ManageGeocoordinate.reload():
            coordinate_with_hash[pgh.encode(element[0],element[1])] = element
        return coordinate_with_hash
    
    @staticmethod
    def array_of_geoash():
        geo_hash_arr = []
        for element in ManageGeocoordinate.genarate_has():
            geo_hash_arr.append(element)
        return geo_hash_arr


    @staticmethod
    def genarate_rando_coordinate():
        list_coordinate = ManageGeocoordinate.reload()
        random_index = random.randint(0,len(list_coordinate)-1)
        return list_coordinate[random_index]
    
    @staticmethod
    def closet_element(arr = []):
        if not len(arr):
            arr = ManageGeocoordinate.genarate_rando_coordinate()
        for element in ManageGeocoordinate.genarate_has():
            if ManageGeocoordinate.genarate_has()[element] == arr:
                geohas_coordinate = element
        matching_coordinate = get_close_matches(geohas_coordinate, ManageGeocoordinate.array_of_geoash())
        for coordinate in matching_coordinate:
            coordinate_without_geohas_coordinate = []
            if coordinate != geohas_coordinate:
                coordinate_without_geohas_coordinate.append(coordinate)
        return coordinate_without_geohas_coordinate
    
    @staticmethod
    def return_lat_long_for(geohash_string):
        return ManageGeocoordinate.genarate_has()[geohash_string]


        




#hfuu5s4g9s08    
#print(ManageGeocoordinate.reload())
#print(ManageGeocoordinate.genarate_has())
#print(ManageGeocoordinate.genarate_rando_coordinate())
#print(ManageGeocoordinate.closet_element())
#print(ManageGeocoordinate.array_of_geoash())
#print(ManageGeocoordinate.return_lat_long_for("hfuu5s4g9s08"))