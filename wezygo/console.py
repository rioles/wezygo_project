#!/usr/bin/python3
import cmd, sys
from models.base_person import BasePerson
from models.engine.filestorage import FileStorage
from models import storage
class WezygoShell(cmd.Cmd):
    intro = 'Welcome to wezygo our plateform to match merchant to transporter.   Type help or ? to list commands.\n'
    prompt = '(wezygo) '

    __classes = {
    "BasePerson" 
    }

    def do_create(self, args):
        """create base_person"""
        token = args.split()
        print(WezygoShell.__classes)
        if len(token) == 0 or len(token) > 1:
            print("**too many argument**")
        if token[0] not in WezygoShell.__classes:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(token[0])()
                print(new_instance.id)
                new_instance.save()
            except:
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