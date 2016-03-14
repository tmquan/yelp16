# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 23:12:52 2016

@author: tmquan
"""


from Utility import *


###############################################################################
def symbol_network():
	#TODO: define deep network architecture 


###############################################################################
if __name__ == '__main__':
    # Draw the net
    data 	= mx.symbol.Variable('data')
	network = symbol_network(data)
	dot = mx.viz.plot_network(network,
		shape={"data" : (65536, 3, 128, 128)}
		) 
	dot.graph_attr['rankdir'] = 'BT'