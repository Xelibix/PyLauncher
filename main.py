import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
cwd = os.path.dirname(os.path.realpath(__file__))




class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    
    def camhacker(self, button):
        files= cwd + "/Files/camhacker"
        command = "konsole -e 'bash " + files +"'"
        os.system(command)



builder = Gtk.Builder()
gladepath=cwd+"/glade.glade"
builder.add_from_file(gladepath)
builder.connect_signals(Handler())
window = builder.get_object("window1")
window.show_all()

Gtk.main()