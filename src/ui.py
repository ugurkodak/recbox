from tkinter import ttk
from data import Data


class UI(ttk.tkinter.Tk):
    __data = None
    __nav = None

    def __init__(self):
        (super(UI, self).__init__(screenName=None,
                                  baseName=None, className="Tk"))

        self.__data = Data()  # Instantiate and load archive data

        # Notebook holds all views with tabs
        self.__nav = ttk.Notebook(self)
        self.__nav.pack(expand=True, fill="both")

        self.init_fields_view()

    def init_fields_view(self):
        view = ttk.Frame(self.__nav)
        view.grid_columnconfigure(0, weight=1)
        view.grid_columnconfigure(1, weight=1)
        view.grid_rowconfigure(0, weight=1)
        view.grid_rowconfigure(1, weight=0)  # Buttons row doesn't expand

        # List fields in a Treeview
        table = ttk.Treeview(view, columns=["name", "description"])
        table.heading("name", text="Name", anchor="w")
        table.heading("description", text="Description", anchor="w")
        table["show"] = "headings"  # Don't show left most identifier column
        for field in self.__data.fields:
            table.insert("", 0, values=[field["name"], field["description"]])
        table.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # Button opens new field view
        buttonNewField = ttk.Button(view, text="New Field")
        buttonNewField.grid(row=1, column=0, sticky="ew")

        # Button creates new template
        buttonNewTemplate = ttk.Button(view, text="New Template")
        buttonNewTemplate.grid(row=1, column=1, sticky="ew")

        self.__nav.add(view, text="Fields")
