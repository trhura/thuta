from gi.repository import Gtk
from window import ThutaWindow

class ThutaApp ():
    def __init__ (self):
        self.window = ThutaWindow ()
        self.window.connect ('delete-event',
                             self.exit)

    def run (self):
        self.window.show ()
        Gtk.main ()

    def exit (self, *args, **kwargs):
        Gtk.main_quit ()

if __name__ == "__main__":
    app = ThutaApp ()
    app.run ()
