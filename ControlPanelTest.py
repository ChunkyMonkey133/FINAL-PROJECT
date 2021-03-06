from tkinter import *

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

def raise_frame(frame):
    frame.tkraise()

root = Tk()

pane = PanedWindow(orient=HORIZONTAL)
pane.pack(fill=BOTH, expand=1)

left = Frame(pane)
pane.add(left)
right = Frame(pane)
pane.add(right)

pp_frame = Frame(right)
cm_frame = Frame(right)
bp_frame = Frame(right)
sp_frame = Frame(right)

pp_listbox = Frame(left)
cm_listbox = Frame(left)
bp_listbox = Frame(left)
sp_listbox = Frame(left)

for frame in (pp_frame, cm_frame, bp_frame, sp_frame):
    frame.grid(row=0, column=0, sticky='news')

for frame in (pp_listbox, cm_listbox, bp_listbox, sp_listbox):
    frame.pack()

def Update_Data_Loc(string):
    "Saves updated data location to ini"
    config = ConfigParser()
    config.read('datavis.ini')
    config.set('general', 'dataset_location', string)
    with open('datavis.ini', 'w') as configfile:
        config.write(configfile)

Label(pp_frame, text='facetgrid').pack()
data_loc_entry = Entry(pp_frame)
data_loc_entry.pack()
Button(pp_frame, text='commit address', command=lambda: Update_Data_Loc(data_loc_entry.get())).pack()
Button(pp_listbox, text='Pairplot', command=lambda: raise_frame(pp_frame)).pack()

Label(cm_frame, text='heatmap').pack()
Button(cm_listbox, text='Correlation Matrix', command=lambda: raise_frame(cm_frame)).pack()

Label(bp_frame, text='hist').pack()
Button(bp_listbox, text='Bar Plot', command=lambda: raise_frame(bp_frame)).pack()

Label(sp_frame, text='lmplot').pack()
Button(sp_listbox, text='Scatter Plot', command=lambda: raise_frame(sp_frame)).pack()

"""
Label(pp_frame, text='facetgrid').pack()
Label(cm_frame, text='heatmap').pack()
Label(bp_frame, text='hist').pack()
Label(sp_frame, text='lmplot').pack()

Button(pp_listbox, text='Pairplot', command=lambda: raise_frame(pp_frame)).pack()
Button(cm_listbox, text='Correlation Matrix', command=lambda: raise_frame(cm_frame)).pack()
Button(bp_listbox, text='Bar Plot', command=lambda: raise_frame(bp_frame)).pack()
Button(sp_listbox, text='Scatter Plot', command=lambda: raise_frame(sp_frame)).pack()
"""

raise_frame(pp_frame)

root.mainloop()