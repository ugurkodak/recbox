import tkinter as tk
import tkinter.ttk as ttk
from data import Data

data = Data()

fieldJSONData = ('{"id": "123",'
                 '"name": "Title",'
                 '"description": "Title of a song"}')

root = tk.Tk()
nav = ttk.Notebook()
tabidList = []

templates = tk.Frame(nav)
lists = tk.Frame(nav)


class FieldsTabFrame(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super(FieldsTabFrame, self).__init__(master, cnf, **kw)
        buttonNewField = (tk.Button(self, text="New Field",
                                    command=self.__new_field_button_callback))
        buttonNewField.pack()

    def __new_field_button_callback(self):
        print("Open new tab")


test = FieldsTabFrame()
nav.add(FieldsTabFrame(nav), text="Fields")

nav.add(templates, text="Templates")
nav.add(lists, text="Lists")

print(templates.master)

nav.pack()

# field = models.FieldData.fromJSON(fieldJSONData)
# print(field.toJSON())

root.mainloop()
