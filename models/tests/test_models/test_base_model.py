#!/usr/bin/env python3
"""unittest module used for testing BaseModel Class."""

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import re
import time
import unittest
import uuid


class TestBaseModel(unittest.TestCase):

    """Cases to be tested for the BaseModel class."""

    def setUp(self):
        """Sets up the test methods."""
        pass

    def tearDown(self):
        """Takes down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Method that resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_3_instancer(self):
        """Tests the instantiation of BaseModel class."""

        x = BaseModel()
        self.assertEqual(str(type(x)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(x, BaseModel)
        self.assertTrue(issubclass(type(x), BaseModel))

    def test_3_init_noargs(self):
        """Tests __init__ without arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as x:
            BaseModel.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(x.exception), msg)

    def test_3_init_manyargs(self):
        """Tests __init__ with many arguments."""
        self.resetStorage()
        args = [a for a in range(1000)]
        x = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        x = BaseModel(*args)

    def test_3_attributes(self):
        """Tests attributes value for instance of a BaseModel class."""
        attributes = storage.attributes()["BaseModel"]
        s = BaseModel()
        for k, v in attributes.items():
            self.assertTrue(hasattr(x, k))
            self.assertEqual(type(getattr(x, k, None)), v)

    def test_3_datetime_created(self):
        """Tests if updated_at & created_at are corresponding with time"""
        date_now = datetime.now()
        x = BaseModel()
        dif = x.updated_at - x.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        dif = x.created_at - date_now
        self.assertTrue(abs(dif.total_seconds()) < 0.1)

    def test_3_id(self):
        """Tests the unique user ids."""
        n = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(n)), len(n))

    def test_3_save(self):
        """Tests the public instance method save()."""
        x = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        x.save()
        dif = x.updated_at - date_now
        self.assertTrue(abs(dif.total_seconds()) < 0.01)

    def test_3_str(self):
        """Testing the __str__ method."""
        x = BaseModel()
        rx = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        rs = rx.match(str(x))
        self.assertIsNotNone(rs)
        self.assertEqual(rs.group(1), "BaseModel")
        self.assertEqual(rs.group(2), x.id)
        s = rs.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        d = json.loads(s.replace("'", '"'))
        _d = b.__dict__.copy()
        _d["created_at"] = repr(d["created_at"])
        _d["updated_at"] = repr(d["updated_at"])
        self.assertEqual(d, _d)

    def test_3_to_dict(self):
        """Tests the mthod for public instance to_dict()."""
        x = BaseModel()
        x.name = "Laura"
        x.age = 23
        s = x.to_dict()
        self.assertEqual(s["id"], x.id)
        self.assertEqual(s["__class__"], type(x).__name__)
        self.assertEqual(s["created_at"], x.created_at.isoformat())
        self.assertEqual(s["updated_at"], x.updated_at.isoformat())
        self.assertEqual(s["name"], x.name)
        self.assertEqual(s["age"], x.age)

    def test_3_to_dict_no_args(self):
        """Tests to_dict() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as f:
            BaseModel.to_dict()
        msg = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(f.exception), msg)

    def test_3_to_dict_excess_args(self):
        """Tests to_dict() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as f:
            BaseModel.to_dict(self, 98)
        msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(f.exception), msg)

    def test_4_instantiation(self):
        """Tests instantiation with **kwargs."""

        model_t = BaseModel()
        model_t.name = "Holberton"
        model_t.my_number = 89
        model_t_json = model_t.to_dict()
        new_model_t = BaseModel(**model_t_json)
        self.assertEqual(new_model_t.to_dict(), model_t.to_dict())

    def test_4_instantiation_dict(self):
        """Tests instantiation with **kwargs from custom dict."""
        n = {"__class__": "BaseModel",
             "updated_at":
             datetime(2050, 12, 30, 23, 59, 59, 123456).isoformat(),
             "created_at": datetime.now().isoformat(),
             "id": uuid.uuid4(),
             "var": "foobar",
             "int": 108,
             "float": 3.14}
        x = BaseModel(**d)
        self.assertEqual(x.to_dict(), n)

    def test_5_save(self):
        """Tests that storage.save() is called from save()."""
        self.resetStorage()
        x = BaseModel()
        x.save()
        key = "{}.{}".format(type(b).__name__, x.id)
        s = {key: x.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(s)))
            f.seek(0)
            self.assertEqual(json.load(f), s)

    def test_5_save_no_args(self):
        """Tests save() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as x:
            BaseModel.save()
        mesg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(x.exception), mesg)

    def test_5_save_excess_args(self):
        """Tests save() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as f:
            BaseModel.save(self, 98)
        mesg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(f.exception), mesg)


if __name__ == '__main__':
    unittest.main()
