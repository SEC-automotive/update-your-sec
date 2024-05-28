import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Güncelleme Aracı")
        self.set_default_size(300, 200)

        vbox = Gtk.VBox(spacing=6)
        self.add(vbox)

        button1 = Gtk.Button(label="Güncellemeleri Kontrol Edin")
        button1.connect("clicked", self.on_check_updates_clicked)
        vbox.pack_start(button1, True, True, 0)

        button2 = Gtk.Button(label="Güncelle")
        button2.connect("clicked", self.on_upgrade_clicked)
        vbox.pack_start(button2, True, True, 0)

    def on_check_updates_clicked(self, button):
        try:
            subprocess.Popen(["pkexec", "apt", "update"], stdin=subprocess.PIPE)
        except Exception as e:
            print("Hata:", e)

    def on_upgrade_clicked(self, button):
        try:
            subprocess.Popen(["pkexec", "apt", "upgrade", "-y"], stdin=subprocess.PIPE)
        except Exception as e:
            print("Hata:", e)

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
