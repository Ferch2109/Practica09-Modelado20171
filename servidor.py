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
	REANUDAR = 7
	NINGUNO = 8

class Servidor(QtGui.QMainWindow):

	def __init__(self):
		super( Servidor, self ).__init__()
		uic.loadUi( 'servidor.ui', self )
		self.redimensionar()
		self.poner_lienzo_celdas()
		self.clickers()
		self.termina_juego.hide()
		self.estado = Estado.EN_MARCHA
		self.timer = None
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
		self.espera.valueChanged.connect( self.actualizar_espera )
		self.estado_juego.clicked.connect( self.estado_del_juego )
		self.termina_juego.clicked.connect( self.terminar_juego )


	def estado_del_juego( self ):
		if self.estado == Estado.EN_MARCHA:
			self.iniciar_juego()
			self.estado = Estado.PAUSADO
		elif self.estado == Estado.PAUSADO:
			self.pausar_juego()
			self.estado = Estado.REANUDAR
		else:
			self.reanudar_juego()
			self.estado = Estado.PAUSADO


	def cambio_numero_celdas( self ):
		filas = self.filas.value()
		columnas = self.columnas.value()
		self.tabla.setRowCount(filas)
		self.tabla.setColumnCount(columnas)
		self.poner_lienzo_celdas()
		self.redimensionar()


	def actualizar_espera( self ):
		mili_seg = self.espera.value()
		self.timer.setInterval(mili_seg)


	def iniciar_juego( self ):
		self.termina_juego.show()
		self.estado_juego.setText( "PAUSAR JUEGO" )
	

	def pausar_juego( self ):
		self.estado_juego.setText( "REANUDAR JUEGO" )
	

	def reanudar_juego( self ):
		self.estado_juego.setText( "PAUSAR JUEGO" )



	def terminar_juego( self ):
		self.termina_juego.hide()
		self.estado_juego.setText( "INICIAR JUEGO" )



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
