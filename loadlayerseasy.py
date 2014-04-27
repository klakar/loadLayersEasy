# -*- coding: utf-8 -*-
"""
/***************************************************************************
 loadLayersEasy
                                 A QGIS plugin
 Laddar lager från definierad lista
                              -------------------
        begin                : 2014-04-27
        copyright            : (C) 2014 by Klas Karlsson / Geosupportsystem
        email                : klaskarlsson@hotmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from loadlayerseasydialog import loadLayersEasyDialog
import os.path
# Anpassa till UTF-8
import codecs
# Lägg till systemvariabler
import sys

# Globala variabler
typ = []
namn = []
kommando = []

# Detta är en class som ersätter SWITCH/CASE kommandot i andra språk
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False


class loadLayersEasy:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'loadlayerseasy_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = loadLayersEasyDialog()


    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/loadlayerseasy/icon.png"),
            u"Ladda Lager", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

	# Ladda listan med lager från listfilen
	# Hämta sökvägen från variabel
	s = QSettings()
	listfil = s.value("loadlayerseasy/listfil", u"Listfil saknas")
	self.dlg.listfil.setText(listfil)

	# Läs in lista från listfil (om den finns)
	if listfil != u"Listfil saknas":
	   try: #först ett test
	   	ff = codecs.open(listfil, 'r', 'utf-8')
	   	inledning = ff.readline().strip()
	   	ff.close()
	   	if inledning != "# Ladda Lager QGIS Plugin av Klas Karlsson":
			QMessageBox.information(self.iface.mainWindow(),u"Fel", u"Konfigfilen är felaktig eller skadad \n Första raden måste vara:\n# Ladda Lager QGIS Plugin av Klas Karlsson\n\nProva att starta om tillägget eller starta om QGIS.")
			s = QSettings()
			s.setValue("loadlayerseasy/listfil", u"Listfil saknas")
	   except:
		s = QSettings()
		s.setValue("loadlayerseasy/listfil", u"Listfil saknas")
		QMessageBox.information(self.iface.mainWindow(),u"Fel", u"Detta är inte en giltig konfigurationsfil.\nFörsök med en annan fil.\n\nDu måste starta om tillägget eller starta om QGIS.")
	   # Läs in listan
	   f = codecs.open(listfil, 'r', 'utf-8')
	   for rad in f:
		fildata = rad.strip() # läs in raden och ta bort nyrad-tecken (strip)
		if fildata != "":
		    if fildata[:1] != "#":
			lista = fildata.split(",")
			typ.append( lista[0] )
			namn.append( lista[1] )
			kommando.append( lista[2] )
			self.dlg.listWidget.addItem(lista[1])
	   f.close()
	    

	# Skapa händelse vid listfil-knappen
	self.dlg.findList.clicked.connect(self.hittaLista)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Ladda Lager", self.action)

    def hittaLista(self):
	# Vad händer när man trycker på listfilsknappen
	# self.dlg.listWidget.addItem('Test')
	filnamn = QFileDialog.getOpenFileName(None, 'Open File', '.')
	if filnamn != "":
		self.dlg.listfil.setText(filnamn)
		s = QSettings()
		s.setValue("loadlayerseasy/listfil", filnamn)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Ladda Lager", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
		# Gå igenom listan och lägg till markerade lager
		markering = self.dlg.listWidget.selectedItems()
		for i in list(markering):
			index = namn.index(i.text()) # Vilket index har valt lager
			# Gå till rätt typ
			v = typ[index].upper()
			for case in switch(v):
				if case(u'OGR'):
					lager = QgsVectorLayer(kommando[index], namn[index], "ogr")
					break
				if case(u'WFS'):
					lager = QgsVectorLayer(kommando[index], namn[index], "WFS")
					break
				if case(u'GPX'):
					lager = QgsVectorLayer(kommando[index], namn[index], "gpx")
					break
				if case(u'POSTGIS'):
					lager = QgsVectorLayer(kommando[index], namn[index], "postgres")
					break
				if case(u'WMS'):
					lager = QgsRasterLayer(kommando[index], namn[index], "wms")
					break
				if case(u'RASTER'):
					lager = QgsRasterLayer(kommando[index], namn[index])
					break
				if case():
					QMessageBox.information(self.iface.mainWindow(),u"Ladda lager", u"Datatypen %s stöds ej" % typ[index])
					lager = QgsVectorLayer()
					break
			if not lager.isValid():
					QMessageBox.information(self.iface.mainWindow(),u"Fel!", u"%s är inte ett giltigt lager:\n %s" % (namn[index], kommando[index]))
					break
			QgsMapLayerRegistry.instance().addMapLayer(lager)


