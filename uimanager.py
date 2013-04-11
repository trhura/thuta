from gi.repository import Gtk

ui_string = """
<ui>
    <menubar name='MenuBar'>
	<menu action='FileMenu'>
		<menuitem action='FileOpen' />
		<menuitem action='FileRecent' />
		<menuitem action='FileQuit' />
	</menu>

	<menu action='EditMenu'>
	    <menuitem action='EditCopy' />
	    <menuitem action='EditPaste' />
	    <menuitem action='EditPreferences' />
	</menu>

	<menu action='ViewMenu'>
	    <menuitem action='ViewSidepane'/>
	    <menuitem action='ViewFullscreen'/>
            <separator />
	    <menuitem action='ViewZoomOut'/>
	    <menuitem action='ViewNormal'/>
	    <menuitem action='ViewZoomIn'/>
	</menu>

	<menu action='HelpMenu'>
	    <menuitem action='HelpHelp'/>
	    <menuitem action='HelpReport'/>
	    <menuitem action='HelpAbout'/>
	</menu>
    </menubar>

    <toolbar name='ToolBar'>
	<toolitem action='FileOpen' />
	<toolitem action='FileQuit' />
	<separator />
	<toolitem action='ViewZoomIn'/>
	<toolitem action='ViewNormal'/>
	<toolitem action='ViewZoomOut'/>
	<separator />
	<toolitem action='EditPreferences' />
	<toolitem action='HelpAbout' />
    </toolbar>
    <!-- <popup name='PopupMenu'> -->
    <!-- 	<menuitem action='EditCopy' /> -->
    <!-- 	<menuitem action='EditPaste' /> -->
    <!-- 	<menuitem action='EditSomething' /> -->
    <!-- </popup> -->
</ui>
"""

ui_actions = [
    ['FileMenu', None, "_File", None, None, None],
    ['FileOpen', Gtk.STOCK_OPEN, "_Open", "<control>O", None, 'on_file_open'],
    ['FileRecent', None, "_Recent Files", None, None, 'on_file_recent'],
    ['FileQuit', Gtk.STOCK_QUIT, "_Quit", "<control>Q", None, 'on_file_quit'],

    ['EditMenu', None, "_Edit", None, None, None],
    ['EditCopy', Gtk.STOCK_COPY, "_Copy", "<control>C", None, 'on_edit_copy'],
    ['EditPaste', Gtk.STOCK_PASTE, "_Paste", "<control>V", None, 'on_edit_paste'],
    ['EditPreferences', Gtk.STOCK_PREFERENCES, "_Preferences", None, None, 'on_edit_preferences'],

    ['ViewMenu',None, "_View", None, None, None],
    ['ViewFullscreen', Gtk.STOCK_FULLSCREEN, "_Fullscreen", "F11", None, 'on_view_fullscreen'],
    ['ViewSidepane', None, "_Sidepane", "F9", None, 'on_view_sidepane'],
    ['ViewZoomIn', Gtk.STOCK_ZOOM_IN, "_Zoom _Out", "<control>plus", None, 'on_view_zoom_in'],
    ['ViewZoomOut', Gtk.STOCK_ZOOM_OUT, "Zoom _In", "<control>minus", None, 'on_view_zoom_out'],
    ['ViewNormal', Gtk.STOCK_ZOOM_FIT, "_Normal", "<control>0", None, 'on_view_normal'],

    ['HelpMenu',None, "_Help", None, None, None],
    ['HelpHelp', Gtk.STOCK_HELP, "_Help", "F1", None, 'on_help_help'],
    ['HelpReport', None, "_Report Problems", None, None, 'on_help_report'],
    ['HelpAbout', Gtk.STOCK_ABOUT, "_About", None, None, 'on_help_about'],
    ]
