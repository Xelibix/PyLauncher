import gi
import os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
cwd = os.path.dirname(os.path.realpath(__file__))

class Handler:
    def onDestroy(self, *args):    #When pressed close windows
        Gtk.main_quit()            # Close window and stop the script
 
    def camhacker(self, button):
        files= cwd + "/Files/clone.sh"
        command = "konsole -e 'bash " + files +" camhacker https://github.com/AngelSecurityTeam/Cam-Hackers'"
        os.system(command)
    
    def ctfr(self, button):
        files= cwd + "/Files/clone.sh"
        command = "konsole -e 'bash " + files +" ctfr https://github.com/UnaPibaGeek/ctfr'"
        os.system(command)

    def edited(self, button, data=None):
        numele= entry.get_text()
        print(numele)

class ButtonWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        gladepath=cwd+"/glade.glade"
        builder = Gtk.Builder.new_from_file(gladepath)
        builder.connect_signals(Handler()) #Load events
        self.window = builder.get_object("window1")
        entry = builder.get_object("entry1")
        self.window.show_all()



win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
Gtk.main()
