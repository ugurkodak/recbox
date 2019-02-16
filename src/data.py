# NOTE

# MODELS
# Field
# Template
# Item
# List

# RELATIONS
# A field is a text
# A template can have multiple fields
# A item can have multiple templates
# A list can have multiple items

import os
import json
import uuid

ROOT_DIR = os.path.dirname(os.path.realpath(__file__)) + "/../"
ARCHIVE_DIR = ROOT_DIR + ".archive"
DATA_DIR = ROOT_DIR + ".archive/.data"
MEDIA_DIR = ROOT_DIR + ".archive/.media"
CONFIG_FILE = ROOT_DIR + ".archive/config.json"


class Data:
    config = {}
    fields = {}
    templates = {}
    lists = {}

    def __init__(self):
        self.load()
        print(self.config)

    def create(self):
        if os.path.isdir(ARCHIVE_DIR):
            print("Error: Old archive directory found while "
                  "trying to create a new archive.")
            input("Press any key to close...")
            exit()
        else:
            os.mkdir(ARCHIVE_DIR)
            os.mkdir(DATA_DIR)
            os.mkdir(MEDIA_DIR)
            open(CONFIG_FILE, "x")
            # TODO Write a default config file
            print("Info: New archive created.")

    def load(self):
        if not os.path.isdir(ARCHIVE_DIR):
            self.create()
        else:
            with open(CONFIG_FILE, "r") as f:
                self.config = json.load(f)
                # TODO Load archive data


class FieldData:
    id = None
    name = None
    description = None
    __dict = None

    def __init__(self, name, description, id=None):
        self.id = id if id is not None else uuid.uuid4()
        self.name = name
        self.description = description
        self.__dict = {
            "id": self.id,
            "name": name,
            "description": description
        }

    @classmethod
    def fromJSON(self, jsonString):  # TODO: is it correct to put self here?
        dic = json.loads(jsonString)
        if (not dic.get("id")
                or not dic.get("name")
                or not dic.get("description")
                or dic["id"] == ""
                or dic["name"] == ""
                or dic["description"] == ""):
            print("Error: Invalid json object for field")
            return None
        else:
            return FieldData(dic["name"], dic["description"], dic["id"])

    def toJSON(self):
        return json.dumps(self.__dict)
