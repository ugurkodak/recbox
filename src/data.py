import os
import json
import uuid

ROOT_DIR = os.path.dirname(os.path.realpath(__file__)) + "/../"
ARCHIVE_DIR = ROOT_DIR + ".archive"
DATA_DIR = ROOT_DIR + ".archive/data"
MEDIA_DIR = ROOT_DIR + ".archive/media"
CONFIG_FILE = ROOT_DIR + ".archive/data/config.json"
FIELDS_FILE = ROOT_DIR + ".archive/data/fields.json"
TEMPLATES_FILE = ROOT_DIR + ".archive/data/templates.json"
LISTS_FILE = ROOT_DIR + ".archive/data/lists.json"


class Data:
    config = []
    fields = []
    templates = []
    lists = []

    def __init__(self):
        self.__load_archive()

    def __create_archive(self):
        # Quit program if archive exists
        if os.path.isdir(ARCHIVE_DIR):
            input("Error: Old archive directory found while "
                  "creating a new archive. Session will be terminated.\n"
                  "Press any key to close...")
            exit()
        else:
            # Create archive directories
            os.mkdir(ARCHIVE_DIR)
            os.mkdir(DATA_DIR)
            os.mkdir(MEDIA_DIR)

            # Create data files with default JSON objects
            with open(CONFIG_FILE, "w") as fp:
                json.dump([], fp)  # TODO Default configuration
            with open(FIELDS_FILE, "w") as fp:
                json.dump([], fp)
            with open(TEMPLATES_FILE, "w") as fp:
                json.dump([], fp)
            with open(LISTS_FILE, "w") as fp:
                json.dump([], fp)

            print("Info: New archive created.")

            self.__load_archive()

    def __load_archive(self):
        # Create archive if first use
        if not os.path.isdir(ARCHIVE_DIR):
            self.__create_archive()
        else:
            # Load data files as arrays of dictionaries
            with open(CONFIG_FILE, "r") as fp:
                self.config = json.load(fp)
            with open(FIELDS_FILE, "r") as fp:
                self.fields = json.load(fp)
            with open(TEMPLATES_FILE, "r") as fp:
                self.templates = json.load(fp)
            with open(LISTS_FILE, "r") as fp:
                self.lists = json.load(fp)

            print("Info: Archive loaded.")

    def create_field(self, name, description):
        # Set new field properties
        new = {}
        new["id"] = str(uuid.uuid4())
        new["name"] = name
        new["description"] = description

        # Update memory
        self.fields.append(new)
        print("Info: New field created.")

        # Return reference to new field
        return self.fields[-1]

    def update(self):
        # Update fields file
        with open(FIELDS_FILE, "w") as fp:
            json.dump(self.fields, fp, indent=2)

        print("Info: Files updated.")
