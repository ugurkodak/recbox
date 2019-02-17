from tkinter import ttk
from data import FieldData


class UI(ttk.tkinter.Tk):
    __nav = None
    __tabidList = []

    def __init__(self, data):
        (super(UI, self).__init__(screenName=None,
                                  baseName=None, className="Tk"))

        self.__nav = ttk.Notebook(self)

        # config = ConfigView(self.__nav)
        fields = FieldsView(self.__nav)
        templates = ttk.Frame(self.__nav)
        lists = ttk.Frame(self.__nav)

        # self.__nav.add(config, text="Config")
        self.__nav.add(fields, text="Fields")
        self.__nav.add(lists, text="Lists")
        self.__nav.add(templates, text="Templates")

        self.__nav.pack(expand=True, fill="both")


# Views

class FieldsView(ttk.Frame):
    def __init__(self, master=None, **kw):
        super(FieldsView, self).__init__(master=None, **kw)

        fieldJSON = ('{"id": "123",'
                     '"name": "Title",'
                     '"description": "Title of a song"}')
        fieldData = FieldData.fromJSON(fieldJSON)

        field = FieldContainer(fieldData, self)
        field.pack()
        # buttonNewField = (ttk.Button(self, text="New Field",
        #                              command=self.__new_field_button_callback))
        # buttonNewField.pack()

    # def __new_field_button_callback(self):
    #     print("Open new tab")





# class ConfigView(ttk.Frame):
#     def __init__(self, master=None, cnf={}, **kw):
#         super(ConfigView, self).__init__(master, cnf, **kw)

# COMPONENTS


class FieldContainer(ttk.Frame):
    __data = {}

    def __init__(self, data, master=None, **kw):
        super(FieldContainer, self).__init__(master, **kw)

        self.__data = data

        (ttk.Label(self, text=data.name + ": ")
         .pack(side="left", expand=True, fill="both"))
        (ttk.Label(self, text=data.description)
         .pack(side="left", expand=True, fill="both"))
