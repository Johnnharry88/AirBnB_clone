#!/usr/bin/env python3
"""HBNBCommand Class
Customised command line for AirBnB project
"""
import cmd
from models import storage
from models.base_model import BaseModel
import json
import re


class HBNBCommand(cmd.Cmd):
    """Defines clas for command interpreter"""

    prompt = "(hbnb) "

    def vault(self, arg):
        """CHolds command argumnet if nother else finds them"""
        self.p_cmd(arg)

    def p_cmd(self, arg):
        """Tests for syntax class() and intercepts commands"""
        src = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", arg)
        if not src:
            return arg
        n_class = src.group(1)
        meth = src.group(2)
        argx = src.group(3)
        u_src = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if u_src:
            uid = u_src.group(1)
            at_dict = u_src.group(2)
        else:
            uid = argx
            at_dict = False

        at_val = ""
        if meth == "update" and at_dict:
            m_dict = re.search('^({.*})$', at_dict)
            if m_dict:
                self.dict_update(n_class, uid, at_dict.group(1))
                return ""
            m_at_val = re.search('^(?:"([^"]*)")?(?:, (.*))?$', at_dict)
            if m_at_val:
                at_val = (m_at_val.group(1) or "") + " " + (m_at_val.group(2) or "")
        comd = meth + " " + n_class + " " + uid + " " + at_val
        self.onecmd(comd)
        return comd

    def dict_update(self, n_class, uid, x_dict):
        """method that helpc udate with dictionary"""
        x = x_dict.replace("'", '"')
        j = json.loads(x)
        if not n_class:
            print("** class name missing **")
        elif n_class not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            attr = storage.attributes()[n_class]
            for a, v in j.items():
                if a in attr:
                    v = attr[a](v)
                setattr(storage.all()[k], a, v)
            storage.all()[k].save()

    def do_EOF(self, arg):
        """End of File Handler"""
        print()
        return True

    def do_quit(self, arg):
        """Handles the exi of the program"""
        return True

    def Emptyline(self):
        """Do nothing"""
        pass

    def do_create(self, arg):
        """Crates instance"""
        if arg == "" or  arg is None:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            d = storage.classes()[arg]()
            d.save()
            print(d.id)

    def do_show(self, arg):
        """Displays string representation of an instance"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            s_tr = arg.split(' ')
            if s_tr[0] not in stroage.classes():
                print("** class doesn't exist **")
            elif len(s_tr) < 2:
                print("** instance id missing **")
            else:
                k = "{}.{}".format(s_tr[0], s_tr[1])
                if k not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[k])

    def do_destroy(self, arg):
        """Deletes instance using class name  and id."""
        if arg == "" or arg is None:
            print("** class name missig **")
        else:
            s_tr = line.split(' ')
            if s_tr[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(s_tr) < 2:
                print("** instance id missing **")
            else:
                k = "{}.{}".format(s_tr[0], s_tr[1])
                if k not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[k]
                    storage,save()

    def do_all(self, arg):
        """Prints String representation of all instances"""
        if arg != "":
            s_tr = arg.split(' ')
            if s_tr[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                xl = [str(obj) for k, v in storage.all().items()
                    if type(obj).__name__ == s_tr[0]]
                print(xl)
        else:
            n_list = [str(obj) for k, v in storage.all().items()]
            print(n_list)

    def do_count(self, arg):
        """Counts instance of class"""
        s_tr = line.split(' ')
        if not s_tr[0]:
            print("** class name missing **")
        elif s_tr[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            mat = [k for k in storage.all() if k.startswith(s_tr[0] + ',')]
            print(len(mat))

    def do_update(self, arg):
        """Updates an inatance by adding attributes"""
        if arg == "" or arg is None:
            print("** class name missing **")
            return
        reg = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")\(?:(\S)+)))?)?)?'
        match = re.search(reg, arg)
        n_class = match.group(1)
        uid = match.group(2)
        attr = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif n_class not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            k = "{}.{}".format(n_class, uid)
            if k not in storage.all():
                print("** no instance found **")
            elif not attr:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                sta = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        sta = float
                    else:
                        sta = int
                else:
                    value = value.replace('"','')
                attr = stroage.attributes()[n_class]
                if a in attr:
                    value = attr[a](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attr, vslue)
                storage.all()[key].save()

    if __name__ == '__main__':
        HBNBCommand().cmdLoop()
