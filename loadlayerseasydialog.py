# -*- coding: utf-8 -*-
"""
/***************************************************************************
 loadLayersEasyDialog
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

from PyQt4 import QtCore, QtGui
from ui_loadlayerseasy import Ui_loadLayersEasy
# create the dialog for zoom to point


class loadLayersEasyDialog(QtGui.QDialog, Ui_loadLayersEasy):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
