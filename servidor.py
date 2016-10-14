# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, uic
from enum import Enum

MainWindowUI, MainWindowBase = uic.loadUiType("servidor.ui")

class Dir(Enum):
	ARRIBA = 1
	ABAJO = 2
	IZQ = 3
	DER = 4

class Estado(Enum):
	EN_MARCHA = 5
	PAUSADO = 6
	NINGUNO = 7

class Servidor(QtGui.QMainWindow):
   
    def __init__(self):
    	super( Servidor, self ).__init__()
    	uic.loadUi( 'servidor.ui', self )
    	self.redimensionar()
    	self.poner_lienzo_celdas()
    	self.estado = Estado.NINGUNO


    def redimensionar(self):
    	self.table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
    	self.table.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)


    def poner_lienzo_celdas(self):
    	self.table.setSelectionMode(QtGui.QTableWidget.NoSelection) 
    	for i in range( self.table.rowCount() ) :
    		for j in range( self.table.columnCount() ) :
    			self.table.setItem( i, j, QtGui.QTableWidgetItem() )
    			self.table.item( i, j ).setBackground( QtGui.QColor( 0, 0, 0 ) )



class Snake():
	def __init__( self, r, g, b ):
		self.lista = [[0,0],[1,0],[2,0],[3,0],[4,0]]
		self.tamanio = len(self.lista)
		self.direccion = Dir.ABAJO
		self.color = (r,g,b)



app = QtGui.QApplication(sys.argv)
window = Servidor()
window.show()
sys.exit(app.exec_())
