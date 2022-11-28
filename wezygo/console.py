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
from util import ManageGeocoordinate
class WezygoShell(cmd.Cmd):
    intro = 'Welcome to wezygo our plateform to match merchant to transporter.   Type help or ? to list commands.\n'
    prompt = '(wezygo) '

    __classes = {
    "BasePerson",
    "Geolocation",
    "Merchandises",
    "Merchant",
    "Truck",
    "TruckOwner"
    }

    __att_person = {
    "first_name",
    "surname"
    "birthday"
    "pictur_url"
    "id_card_url"
    }

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
        for element in lat_long_arr:
            lat_long_arr_flot.append(eval(element))
        print(ManageGeocoordinate.closet_element(lat_long_arr_flot))
        print(lat_long_arr)

    def do_EOF(self, args):
        """end_of_file"""
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

if __name__ == "__main__":
    console = WezygoShell()
    console.cmdloop()