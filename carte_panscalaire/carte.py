from PyQt5 import QtWidgets, QtWebEngineWidgets, QtCore, QtGui
import sys

class MapWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Carte OpenLayers")
        
        # Créer la vue WebEngine
        self.browser = QtWebEngineWidgets.QWebEngineView()
        
        # Charger l'URL
        url = QtCore.QUrl("https://lostinzoom.huma-num.fr/seism/")
        self.browser.setUrl(url)
        
        # Définir la vue Web comme widget central
        self.setCentralWidget(self.browser)
        
        # Mettre la fenêtre en plein écran
        self.showFullScreen()

        # Ajouter un raccourci pour quitter avec la touche Escape
        exit_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Escape"), self)
        exit_shortcut.activated.connect(self.close_window)

    def close_window(self):
        self.close()  # Ferme la fenêtre

# Initialiser l'application PyQt
app = QtWidgets.QApplication(sys.argv)
window = MapWindow()
sys.exit(app.exec_())