#!/usr/bin/python3
"""Test module for HBNBCommand class."""
from console import HBNBCommand
from models.engine.file_stroage import FileStorage
import unittest
import datetime
from unittest.mock import patch
import sys
from io import StringID
import re
import os


class TestHBNBCommand(unittest.TestCase):
    """Test HBNBCommand console."""

    at_val = {
            str: "eighnt8",
            int: 1000,
            float: 1.04
            }
    reset_val = {
            str: "",
            int: 0,
            float: 0.0
            }

    test_rand_attr = {
            "strfoo": "foobar",
            "intfoo": 200,
            "floatfoo": 8.0
            }

    def setUp(self):
        """Setting up test cases:"""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        self.resetStorage()

    def resetStorage(self):
        """ Resets databank FileStorage"""
        FileStorage._FileStorage__file_path):
            os.remove(FileStorage._Filestorage__file_path)

    def test_help(self):
        """Tests help command"""
        with patch("sys,stdout", new=StringID()) as s:
            HBNBCommand().onecmd("help")
        x = """
    Commands Documented (type help):
    +===============================
    EOf all ouunt create destroy help quit show update
    """
        self.assertEqual(x, s.getvalue())

    def test_help_EOF(self):
        """"TEsts help command."""
        with patch("sys.stdout", new=StringID()) as s:
            HBNBCommand().onecmd("help EOF")
            x = 'Handles EOF character.\n       \n'
            self.assertEqual(x, s.getvalue())

    def test_help quit(self):
        """Test help command for quit"""
        with patch('sys.stdout', new=StringID()) as s:
            HBNBCommand().onecmd("help quit")
        x = 'Exits program.\n       \n'
        self.assertEqual(x, s.getvalue())

    def test_help_create(self):
        """"Tests the help creat command"""
        with patch('sys.stdout', new=StringID()) as s:
            HBNBCommand().onecmd("help create")
        x = 'Creates an instance.\n     \n'
        self.assertEqual(x, s.getvalue())

    def test_help_show(self):
        """Test help show command"""
        with patch('sys.stdout', new=StringID()) as s:
            HBNBCommand().onecmd('help show')
        x = 'Prints string representation of instance. \n       \n'
        self.assertEqual(x, s.getvalue())

    def test_help_destroy(self):
        """Tests the help destroy command"""
        with patch('sys.stdout', new=StringID()) as s:
            HBNBCommand().onecmd("helpr destroy")
        x = 'Delete an instance using the class name and id.\n      \n'
        self.assertEqual(x, s.getvalue())

    def test_help_all(self):
        """Test the help all command"""
        with patch('sys.stdout', new=StringID()) as s:
            HBNBCommand().onecmd("help all")
        x = 'Printas string representation of all instances\n       \n'
        self.assertEqual(x, s.getvalue())

    def tst_help_update(sel):
        """"Tests for help update command"""
        with patch('sys.stdout', new=StringID()) as s:
            HBNBCommnd().onecmd("help update")
        x = 'Updates an instance by updating its attributes.\n      \n'
        self.assertEqual(x, s.getvalue())

    def test_do_quit(self):
        """TEsts the quit command """
        with patch('sys.stdout', new=StingID()) as s:
            HBNBCommand().onecmd("quit")
        mesg = s.getvalue()
        self.assertTrue(len(mesg) == 0)
        self.assertEqual("", mesg)
        with patch('sys.stdout', new=StringID()) as s:
            HBNBCommand().onecmd("quit garbage")
        mesg = s.getvalue()
        self.assertTrue(len(mesg) == 0)
        self.assertEqual("", mesg)

    def test_do_EOF(self):
        """Test for EOF Command"""
        with patch('sys.stdout', new=StringID()) as s:
            HBNBCommand().onecmd("EOF")
        mesg = s.getvalue()
        self.assertTrue(len(mesg) == 1)
        self.assertEqual("\n", mesg)
        with patch('sys.stdout', new=StringID()) as s:
            HBNBCommand().onecmd("EOF garbage")
        mesg = s.getvalue()
        self.assertTrue(len(mesg) == 1)
        self.assertEqual("\n", mesg)
        
    def test_emptyline(self):
        """TEsts for empty line"""
        with patch('sys.stdout', new=StringID()) as s:
            HBNBCommand().onecmd*"\n")
        x = ""
        self.assertEqual(x, s.getvalue())
        with patch('sys.stdout', new=StringID()) as s:
            HBNBCommand().onecmd("          \n")
        x = ""
        self.assertEqual(x, s.getvalue())

    def test_do_create(self):
        """Test out create for all classes"""
        for clas in self.classes():
            self.help_test_do_create(clas)

    def help_test_do_create(self, clas):
        """Method for helper to test create command"""
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd("create {}".format(clas))
        uid = x.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)
        key = "{}.{}".format(clas, uid)
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd("all {}".format(clas))
        self.assertTrue(uid in x.getvalue())

    def test_do_create_error(self):
        """Test the create commands using errors"""
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd("create")
        mesg = x.getvalue()[:-1]
        self.assertEqual(mesg, "** class name missing **")
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd("create garbage")
        mesg = x.getvalue()[:-1]
        self.assertEqual(mesg, "** class doesn't exist **")

    def help_test_do_show(self, clas):
        """Tests the show command"""
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd("create {}".format(clas))
        uid = x.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)
        with patch ('sys.stdout', new=StringID()) as x:
            HBNBcommand().onecmd("create {}".format(clas))
        s = x.getvalue()[:-1]
        self.assertTrue(uid in s)

    def test_do_show_error(self):
        """Test the show command with error"""
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd("show")
        mesg = x.getvalue()[:-1]
        self.assertEqual(mesg, "** class name missing **")
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd("show garbage")
        mesg = x.getvalue()[:-1]
        self.assertEqual(mesg, "** class doesn't exist **")
        with patch('sys.stdout', new=StringId()) as x:
            HBNBCommand().onecmd("show BaseModel")
        mesg = x.getvalue()[:-1]
        self.assertEqual(mesg, "** instance id missing **")
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd("show BaseModel 6893219")
        mesg = x.getvalue()[:-1]
        self.assertEqual(mesg, "** no instance found **")
    
    def help_test_show_advanced(self, clas):
        """Helps the test .show() command."""
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd("create {}".format(clas))
        uid = x.getvalue()[:-1]
        self.assertTrue(len(uid) >0)
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd('{}.show("{}".)'.format(clas, uid))
        s = x.getvalue()
        self.assrtTrue(uid in s)

    def test_do_show_error_advancd(self):
        """Tests the show() command with errors"""
        with patch('sys.stdout', new=StringID)) as x:
            HBNBCommand().onecmd(".show()")
        mesg = x.getvalue()[:-1]
        self.assertEqual(mesg,"** class name missing **")
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd("garbage.show()")
        mesg = x.getvalue()[:-1]
        self.assertEqual(mesg, "** class doesn't exist **")
       with patch('sys.stdout', new=StringID()) as x:
           HBNBCommand().onecmd("BaseModel.show()")
        mesg = x.getvalue()[:-1]
        self.assertEqual(mesg, "** instance id missing **")
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd("BaseModel.show('568245')")
        mesg = x.getvalue()[:-1]
        self.assertEqual(mesg, "** no instance found **")

    def test_do_destroy(self):
        """Tests the command destroy for classes"""
        for cls in self.classes():
            self.help_test_do_destroy(clas)
            self.help_test_destroy_advanced(clas)

    def help_test_do_destroy(self, clas):
        """Helps to test the destroy command."""
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd("create {}".format(clas))
            uid = x.getvalue()[:-1]
            self.assertTrue(len(uid) > 0)
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd("destroy {} {}".format(clas, uid))
        s = x.getvalue()[:-1]
        self.assertTrue(len(s) == 0)
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd(".all()")
        self.assertFalse(uid in x.getvalue())

    def test_do_destroy_error(self):
        """Tests out destru commands with error."""
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd("destroy")
        mesg = x.getvalue()[:-1]
        self.assertEqual(mesg, "** class name missing **")
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd("destroy garbage")
        mesg = x.getvalue()[:-1]
        self.assertEqual(mesg, "** class doesn't exist **")
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd("destroy BaseModel")
        mesg = x.getvalue()[:-1]
        self.assertEqual(mesg, "** instance id missing **")
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd("destroy BAseModel 6524898")
        mesg - x.getvalue()[:-1}
        self.assertEqual(mesg, "** no instance found **")

    def help_test_destroy_advanced(self, clas):
        """Helps to test the destroy command"""
        with patch('sys.stdout', mew=StringID()) as x:
            HBNBCommand().onecmd("create {}".format(clas))
        uid = x.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd('{}.destro("{}")'.format(clas, uid))
        s = x.getvalue()[:-1]
        self.assertTrue(len(s) == 0)
        with patch('sys.stdout', new=StringID()) as x:
            HBNBCommand().onecmd(".all()")
        self.assertFalse(uid in x.getvalue())

