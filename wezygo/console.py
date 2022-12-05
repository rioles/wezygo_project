#!/usr/bin/python3
import cmd, sys
from models.base_person import BasePerson
from models.engine.filestorage import FileStorage
from models import storage
from uuid import uuid4
from models.geolocation import Geolocation
from models.merchandise import Merchandises
from models.merchant import Merchant
from models.truck import Truck
from models.truck_owner import TruckOwner
from models.truck_merchandise import TruckMerchandise
from util import ManageGeocoordinate
from os import getenv
class WezygoShell(cmd.Cmd):
    intro = 'Welcome to wezygo our plateform to match merchant to transporter.   Type help or ? to list commands.\n'
    prompt = '(wezygo) '

    __classes = {
    "BasePerson",
    "Geolocation",
    "Merchandises",
    "Merchant",
    "Truck",
    "TruckOwner",
    "TruckMerchandise"
    }

    __match_classes = {"Merchandises":Merchandises, "Truck":Truck}
 

    def do_create(self, args):
        """create base_person"""

        print(WezygoShell.__classes)
        try:
            if not args:
                raise SyntaxError()
            my_list = args.split(" ")

            kwargs = {}
            for i in range(1, len(my_list)):
                key, value = tuple(my_list[i].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value
                print(kwargs)

            if kwargs == {}:
                obj = eval(my_list[0])()
            else:
                if id not in kwargs:
                    kwargs['id'] = str(uuid4())
                obj = eval(my_list[0])(**kwargs)
                print(obj)
                storage.new(obj)
            print(obj.id)
            obj.save()
            print(obj.id)


        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")


    def do_show(self, args):
        """show instance based on class name and id"""
        token = args.split()
        
        if len(token) == 0:
            print(len(token))
            print("***class missing***")
            return
        if len(token) == 1 and token[0] not in WezygoShell.__classes:
            print("** class doesn't exist **")
            return
        if len(token) == 1 and token[0] in WezygoShell.__classes:
            print("**instance id missing**")
            return
        storage.reload()
        objs_dict = storage.all()
        key = f"{token[0]}.{token[1]}"
        if key in objs_dict:
            print(str(objs_dict[key]))
        else:
            print("** no instance found **")

        
    
    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (saves the changes into the JSON file)
        Structure: destroy [class name] [id]
        """
        token = args.split()
        if len(token) == 0:
            print("** class name missing **")
            return
        if token[0] not in WezygoShell.__classes:
            print("** class doesn't exist **")
            return
        if len(token) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objs_dict = storage.all()
        key = token[0] + "." + token[1]
        if key in objs_dict:
            del objs_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_genaretecoordinate(self, args):
        """
        genarate a random coordinate
        """
        print(ManageGeocoordinate.genarate_rando_coordinate())

    def do_find_nearcab(self, args):
        """
        find near cab for given coordinate ([lat, long])
        """
        lat_long_arr = args.split()
        lat_long_arr_flot = []

        if len(lat_long_arr) < 1:
            print("** longitude is missing, but we genarate a random coordinate for you **")
            print(ManageGeocoordinate.closet_element())
        else:

            for element in lat_long_arr:
                lat_long_arr_flot.append(eval(element))
            print(f"merchant coordinate {ManageGeocoordinate.encode_coordinate(lat_long_arr_flot)}")
            print(f" close drivers coordinates = {ManageGeocoordinate.closet_element(lat_long_arr_flot)}")
        

    def do_tripe(self, args):
        """
        make a trip
        """
        my_list = args.split(" ")
        kwargs = {}
        for i in range(0, len(my_list)):
            #print(my_list[i])
            try:
                key, value = tuple(my_list[i].split("="))
                kwargs[key] = value
            except (SyntaxError,ValueError):
                print("** SynthaxeError **")
                return
        print(kwargs)

        geohash_ids = {}
        merchandise_dic = {}
        truck_dic = {}
        truck_merchandises = {}
        geocoordinate_merchant = {}
        geocoordinate_truck = {}
        for element in kwargs:
            value = kwargs[element]
            print(element)
            try:
                key, v = tuple(element.split("_"))
                if key not in WezygoShell.__match_classes:
                    truck_merchandises["prices"] = eval(value)
                else:
                    data_type_user = (merchandise_dic,truck_dic)
                    self.update_merchandise_truck_data(key,data_type_user,v, value)
                geohash_ids["Merchandises"] = merchandise_dic
                geohash_ids["Truck"] = truck_dic
            except (SyntaxError,ValueError):
                print("** SynthaxError **")
                return
        #print(truck_merchandises)
        if len(geohash_ids) < 1:
            print("** classe Merchandises or Truck miss **")
            return
        else:
            location_data = (geocoordinate_merchant,geocoordinate_truck)
            self.update_tripe_data(geohash_ids, truck_merchandises,location_data)

            geocoordinate_truck['id'] = str(uuid4())
            geocoordinate_merchant['id'] = str(uuid4())

            geocoordinate_merchant_obj = Geolocation(**geocoordinate_merchant)
            geocoordinate_truck_obj = Geolocation(**geocoordinate_truck)
            truck_merchandise_obj= TruckMerchandise(**truck_merchandises)

            storage.new(geocoordinate_merchant_obj)
            storage.new(geocoordinate_truck_obj)
            storage.new(truck_merchandise_obj)
            geocoordinate_merchant_id = geocoordinate_merchant_obj.id
            geocoordinate_truck_id = geocoordinate_truck_obj.id
            geocoordinate_merchant_obj.save()
            geocoordinate_truck_obj.save()
            truck_merchandise_obj.save()

            storage.update(Merchandises,merchandise_dic['merchandise_id'],geocoordinate_merchant_id)
            storage.update(Truck,truck_dic['truck_id'],geocoordinate_truck_id)
            print(geocoordinate_truck_obj)
            print(truck_dic)
            print(truck_merchandises)
            

    
    def update_merchandise_truck_data(self, user_type, data_type_user, v, value):
        if user_type == "Merchandises":
            if v =="id":
                data_type_user[0]["merchandise_id"] = value
            if v == "geohash":
                data_type_user[0]["merchandise_coordinate"] = value
        if user_type == "Truck":
            if v =="id":
                data_type_user[1]["truck_id"] = value
            if v == "geohash":
                data_type_user[1]["truck_coordinate"] = value


    def update_geolocation_data(self,location_data, type_user,geohash_ids,ele):
        if type_user == "Merchandises":
            coordinate_data = ManageGeocoordinate.return_lat_long_for(geohash_ids["Merchandises"][ele])
            location_data["coordinate_of"] = "marchandise"
        else:
            coordinate_data = ManageGeocoordinate.return_lat_long_for(geohash_ids["Truck"][ele])
            location_data["coordinate_of"] = "truck"
        location_data["latitude"] = coordinate_data[0]
        location_data["longitude"] = coordinate_data[1]

    
    def update_tripe_data(self,geohash_ids, truck_merchandise_data,location_data):
        for element in geohash_ids:
            if element == "Merchandises":
                for ele in geohash_ids["Merchandises"]:
                    if ele == "merchandise_id":
                        truck_merchandise_data[ele] = geohash_ids["Merchandises"][ele]
                    else:
                        user_type = "Merchandises"
                        self.update_geolocation_data(location_data[0],user_type,geohash_ids,ele)
           
            elif element == "Truck":
                for ele in geohash_ids["Truck"]:
                    if ele == "truck_id":
                        truck_merchandise_data[ele] = geohash_ids["Truck"][ele]
                    else:
                        user_type = "Truck"
                        self.update_geolocation_data(location_data[1],user_type,geohash_ids,ele)

        


    def do_all(self, args):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        if not args:
            objects = storage.all()
            print([objects[k].__str__() for k in objects])
            return
        try:
            my_list = args.split(" ")
            if my_list[0] not in self.__classes:
                raise NameError()

            objects = storage.all(eval(my_list[0]))
            print([objects[k].__str__() for k in objects])

        except NameError:
            print("** class doesn't exist **")


    def do_EOF(self, args):
        """end_of_file"""
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

if __name__ == "__main__":
    console = WezygoShell()
    console.cmdloop()