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
		self.clickers()
		self.estado = Estado.NINGUNO
    	#self.principal.setWidgetResizable(True)


	def redimensionar( self ):
		self.tabla.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
		self.tabla.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)


	def poner_lienzo_celdas( self ):
		self.tabla.setSelectionMode(QtGui.QTableWidget.NoSelection) 
		for i in range( self.tabla.rowCount() ) :
			for j in range( self.tabla.columnCount() ) :
				self.tabla.setItem( i, j, QtGui.QTableWidgetItem() )
				self.tabla.item( i, j ).setBackground( QtGui.QColor( 0, 0, 0 ) )


	def clickers( self ):
		self.columnas.valueChanged.connect( self.cambio_numero_celdas )
		self.filas.valueChanged.connect( self.cambio_numero_celdas )
		#self.espera.valueChanged.connect(self.actualizar_espera)


	def cambio_numero_celdas( self ):
		filas = self.filas.value()
		columnas = self.columnas.value()
		self.tabla.setRowCount(filas)
		self.tabla.setColumnCount(columnas)
		self.poner_lienzo_celdas()
		self.redimensionar()


class Snake():
	def __init__( self, r, g, b ):
		self.lista = [[0,0],[1,0],[2,0],[3,0],[4,0]]
		self.tamanio = len( self.lista )
		self.direccion = Dir.ABAJO
		self.color = (r,g,b)



app = QtGui.QApplication(sys.argv)
window = Servidor()
window.show()
sys.exit(app.exec_())
