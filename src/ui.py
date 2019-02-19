from data import Data
from tkinter import ttk
from tkinter import Text
from tkinter import messagebox

# TODO
# Sort fields using identifier cell
# Make fields used by templates unselectable


class UI(ttk.tkinter.Tk):
    __data = None
    __nav = None

    def __init__(self):
        (super(UI, self).__init__(screenName=None,
                                  baseName=None, className="Tk"))

        self.title("Recbox")

        self.__data = Data()  # Instantiate and load archive data

        # Notebook holds all views with tabs
        self.__nav = ttk.Notebook(self)
        self.__nav.pack(expand=True, fill="both")

        # Init static views
        self.__init_fields_view()
        # self.__init_templates_view()

    def __init_fields_view(self):
        view = ttk.Frame(self.__nav)
        self.__nav.fieldsView = view  # Make view reachable from outside
        self.__nav.add(view, text="Fields")

        # Configure grid layout
        view.grid_columnconfigure(0, weight=1)
        view.grid_columnconfigure(1, weight=1)
        view.grid_columnconfigure(2, weight=1)
        view.grid_rowconfigure(0, weight=1)
        view.grid_rowconfigure(1, weight=0)  # Buttons row doesn't expand

        # List fields in a Treeview
        view.table = (ttk.Treeview(view, columns=["name",
                                                  "description"]))
        view.table.heading("name", text="Name", anchor="w")
        view.table.heading("description", text="Description", anchor="w")
        view.table["show"] = "headings"  # Don't show left most id column
        for field in self.__data.fields:
            (view.table.insert("", 0, iid=field["id"],
                               values=[field["name"],
                                       field["description"]]))
        view.table.grid(row=0, column=0, columnspan=3, sticky="nsew")

        # Button to open new field view
        newFieldButton = (ttk.Button(view, text="New Field",
                                     command=self.__open_new_field_view))
        newFieldButton.grid(row=1, column=0, sticky="ew")

        # TODO Button to open create template view with selected fields
        newTemplateButton = ttk.Button(view, text="New Template")
        newTemplateButton.grid(row=1, column=1, sticky="ew")

        # Button to delete selected from fields table
        def delete_fields():
            selection = view.table.selection()
            if selection == ():
                (messagebox.showinfo(
                    "Info", "Select one or more unused fields to delete."))
            else:
                message = "Following fields will be deleted:\n\n"
                for i in selection:
                    message += view.table.item(i)["values"][0] + "\n"
                isConfirmed = (messagebox.askokcancel(
                    "Info", message, default=messagebox.CANCEL))
                if isConfirmed:
                    self.__data.delete_fields(view.table.selection())
                    self.__data.update_files("fields")
                    self.__update_static_views("fields")
        deleteFieldsButton = (ttk.Button(view, text="Delete",
                                         command=delete_fields))
        deleteFieldsButton.grid(row=1, column=2, sticky="ew")

    def __open_new_field_view(self):
        view = ttk.Frame(self.__nav)
        self.__nav.add(view, text="New Field")
        self.__nav.select(view)

        # Configure grid layout
        view.grid_columnconfigure(0, weight=0)
        view.grid_columnconfigure(1, weight=1)
        view.grid_columnconfigure(2, weight=1)
        view.grid_rowconfigure(0, weight=0)
        view.grid_rowconfigure(1, weight=1)
        view.grid_rowconfigure(2, weight=0)

        # Field creation form
        nameLabel = ttk.Label(view, text="Name")
        nameLabel.grid(row=0, column=0, sticky="ne")
        descriptionLabel = ttk.Label(view, text="Description")
        descriptionLabel.grid(row=1, column=0, sticky="ne")
        nameEntry = ttk.Entry(view)
        nameEntry.grid(row=0, column=1, sticky="nw")
        descriptionTextArea = Text(view)
        descriptionTextArea.grid(row=1, column=1, sticky="nw")

        # Button to create new field update data and close view
        def create_field():
            (self.__data.create_field(
                nameEntry.get(),
                descriptionTextArea.get("1.0", 'end-1c')))
            self.__data.update_files("fields")
            self.__update_static_views("fields")
            self.__nav.forget(view)
        createButton = ttk.Button(view, text="Create", command=create_field)
        createButton.grid(row=2, column=0, columnspan=2, sticky="ew")

        # Button to cancel the procedure
        cancelButton = (ttk.Button(view, text="Cancel",
                                   command=lambda: self.__nav.forget(view)))
        cancelButton.grid(row=2, column=2, sticky="ew")

    def __open_new_template_view(self, *fields):
        view = ttk.Frame(self.__nav)
        self.__nav.add(view, text="New Template")
        self.__nav.select(view)

    def __update_static_views(self, *views):
        for v in views:
            if (v == "fields"):
                table = self.__nav.fieldsView.table
                table.delete(*table.get_children())
                for field in self.__data.fields:
                    (table.insert("", 0, iid=field["id"],
                                  values=[field["name"],
                                          field["description"]]))
