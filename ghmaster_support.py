#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Apr 01, 2021 09:18:31 PM IST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global txtdistrictorcity
    txtdistrictorcity = tk.StringVar()
    global txtstate
    txtstate = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def save():
    print('ghmaster_support.save')
    sys.stdout.flush()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import ghmaster
    ghmaster.vp_start_gui()



