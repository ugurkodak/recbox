from data import Data
# from ui import UI
# from pprint import pprint

# UI(Data()).mainloop()

data = Data()
# data.create_field("Title", "The title of a work")
data.fields[0]["description"] = "Edited description"
data.update()
