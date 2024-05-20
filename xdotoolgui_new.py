#!/usr/bin/env python

import threading

import gi
gi.require_version("Gtk", "3.0")
gi.require_foreign("SourceView") # don't know how to import it
# gi.require_version("GtkSourceView", "4.0")

import sys,runxdotool,time

from gi.repository import Gtk

filename = 'new file'
MouseLocation = False

class xdotoolgui:
    """A gui for xdotool. Make it easy to use in gnome. """

    def __init__(self):
        
        #Set the Glade file
        builder = Gtk.Builder()
        builder.add_from_file("gui.ui")
        self.ui = builder
        self.get_object = self.ui.get_object
        
        self.connect_signals()

        self.update_window_name()

    def update_window_name(self):
        self.get_object('editor').set_title('xdotool-gui - ' + filename)

    def connect_signals(self):
        #Create our dictionay and connect it
        dic = { 
            "show_about" : self.show_about,
            "hide_about" : self.show_about,
        }
        self.ui.connect_signals(dic)

    # About Dialog
    def show_about(self):
        self.get_object('aboutdialog').show()

    def hide_about(self):
        self.get_object('aboutdialog').hide()
    
if __name__ == "__main__":
    editor = xdotoolgui()
    editor.window.show()
    Gtk.main()
