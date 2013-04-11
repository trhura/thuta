from gi.repository import Gtk
from uimanager import ui_string, ui_actions
from poppler import PopplerDocument

class ThutaWindow (Gtk.Window):
    def __init__ (self):
        super(ThutaWindow, self).__init__()
        self.set_property ("title", "Main Window")

        # automatic callback declaration for actions
        for action in ui_actions:
            if action[-1]:
                action[-1] = getattr (self, action[-1])

        action_group = Gtk.ActionGroup ("thuta_actions")
        action_group.add_actions (ui_actions)

        uimanager = Gtk.UIManager ()
        uimanager.insert_action_group (action_group)
        uimanager.add_ui_from_string (ui_string)

        menubar = uimanager.get_widget ('/MenuBar')
        toolbar = uimanager.get_widget ('/ToolBar')
        self.scrolledwindow = Gtk.ScrolledWindow ()
        self.scrolledwindow.set_policy (Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.ALWAYS)

        mainbox = Gtk.VBox ()
        mainbox.pack_start (menubar, False, False, 0)
        mainbox.pack_start (toolbar, False, False, 0)
        mainbox.pack_start (self.scrolledwindow, True, True, 0)

        self.add (mainbox)
        self.set_size_request (800, 600)
        self.add_accel_group (uimanager.get_accel_group ())

    def show (self):
        self.show_all ()

    def on_file_open (self, *args, **kwargs):
        filechooser = Gtk.FileChooserDialog ("Open Document",
                                             self,
                                             Gtk.FileChooserAction.OPEN,
                                             [Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                              Gtk.STOCK_OPEN, Gtk.ResponseType.ACCEPT])

        if filechooser.run () == Gtk.ResponseType.ACCEPT:
            filename = filechooser.get_uri ()

        filechooser.destroy ()

        # TODO: determine file type, new tab
        document = PopplerDocument (filename)
        self.set_title (document.title)
        self.scrolledwindow.add_with_viewport (document.get_view_widget ())

        if getattr(document, 'on_scroll'):
            adjustment = self.scrolledwindow.get_vadjustment()
            adjustment.connect ('value-changed', document.on_scroll)

    def on_file_recent (self, *args, **kwargs):
        pass

    def on_file_quit (self, *args, **kwargs):
        self.emit ('delete-event', None)

    def on_edit_copy (self, *args, **kwargs):
        pass

    def on_edit_paste (self, *args, **kwargs):
        pass

    def on_edit_preferences (self, *args, **kwargs):
        pass

    def on_view_fullscreen (self, *args, **kwargs):
        pass

    def on_view_sidepane (self, *args, **kwargs):
        pass

    def on_view_zoom_in (self, *args, **kwargs):
        pass

    def on_view_normal (self, *args, **kwargs):
        pass

    def on_view_zoom_out (self, *args, **kwargs):
        pass

    def on_help_help (self, *args, **kwargs):
        pass

    def on_help_report (self, *args, **kwargs):
        pass

    def on_help_about (self, *args, **kwargs):
        pass
