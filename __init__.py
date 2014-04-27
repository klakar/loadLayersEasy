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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load loadLayersEasy class from file loadLayersEasy
    from loadlayerseasy import loadLayersEasy
    return loadLayersEasy(iface)
