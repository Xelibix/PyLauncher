import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
cwd = os.path.dirname(os.path.realpath(__file__))
install_script= cwd + "/Files/clone.sh"

class Handler:
    def onDestroy(self, *args):    #When pressed close windows
        Gtk.main_quit()            # Close window and stop the script
 
    def camhacker(self, button):
        
        command = "konsole -e 'bash " + install_script +" camhacker https://github.com/AngelSecurityTeam/Cam-Hackers'"
        os.system(command)

    def enterctfr(self, button, data=None):
        text= entry.get_text()
        print(text)
        command = "konsole -e 'bash " + install_script +" ctfr https://github.com/UnaPibaGeek/ctfr "+ text +"'"
        os.system(command)

    
        

builder = Gtk.Builder()       
gladepath=cwd+"/glade.glade"       #Load glade file
builder.add_from_file(gladepath)   
builder.connect_signals(Handler()) #Load events
window = builder.get_object("window1")
entry = builder.get_object("ctfr_entry")

window.show_all()
Gtk.main()