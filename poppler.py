from gi.repository import Poppler, Gtk, Gdk, GObject
from document import Document
import cairo

class PopplerDocument (Document):
    _current_page = 0

    @property
    def current_page (self):
        return self._current_page

    @current_page.setter
    def current_page (self, value):
        self._current_page = value

    def __init__ (self, filename=None):
        super (PopplerDocument, self).__init__ (filename)

        self.poppler_document = Poppler.Document.new_from_file (self.filename, None)
        self.title = self.poppler_document.get_title ()
        self.n_pages = self.poppler_document.get_n_pages ()

        self.vbox = Gtk.Box (homogeneous=False, spacing=0)
        self.vbox.set_orientation (Gtk.Orientation.VERTICAL)
        self.vbox.show ()

        for i in range(0, self.n_pages):
            page = PopplerPage (self.poppler_document.get_page (i), i)
            self.vbox.pack_start (page, False, False, 0)
            page.show_all ()

    def can_navigate(self, ):
        """
        """
        return True

    def get_view_widget (self):
        return self.vbox

    def next_page(self, ):
        """
        """
        if not self.current_page < self.n_pages:
            return

    def on_scroll (self, adjustment):
        upper = adjustment.get_upper ()
        value = adjustment.get_value ()
        value_per_page = round(upper / float(self.n_pages))
        current_position= abs((value - (value_per_page/4)) / float(upper))
        self.current_page =  round (self.n_pages * current_position) + 1

class PopplerPage (Gtk.EventBox):

    # __gsignals__ = {
    #     "viewing" :  (GObject.SIGNAL_RUN_FIRST, None, ())
    #     }

    def __init__ (self, page, n_page):
        super (PopplerPage, self).__init__ ()

        self.page   = page
        self.image  = Gtk.Image ()
        self.n_page = n_page

        self.add (self.image)
        self.add_events (Gdk.EventMask.ALL_EVENTS_MASK)
        self.image.set_can_focus (True)

        self.image.set_size_request (*page.get_size ())
        self.connect ('visibility-notify-event', self.on_visibility_notify)

    def on_visibility_notify (self, widget, event):
        if event.state == Gdk.VisibilityState.FULLY_OBSCURED:
            self.clear_page ()
        else:
            self.draw_page ()

    def clear_page (self):
        self.image.clear ()

    def draw_page (self):
        dpi   = 150
        scale = 1
        width, height = [int(x) for x in self.page.get_size ()]
        surface = cairo.ImageSurface (cairo.FORMAT_ARGB32,
                                      dpi * width / 72,
                                      dpi * height / 72)

        context = cairo.Context (surface)
        context.scale (dpi / 72, dpi / 72)

        context.save ()
        self.page.render (context)
        context.restore ()

        pixbuf  = Gdk.pixbuf_get_from_surface (surface, 0, 0,
                                               int(scale * width),
                                               int(scale * height))
        self.image.set_from_pixbuf (pixbuf)

    def __repr__ (self):
        return "<PopplerPage object (" + str(self.n_page) + ")>"
