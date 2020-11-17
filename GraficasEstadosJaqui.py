# -*- coding: utf-8 -*-
"""
Created on Mon Oct  26 16:49:29 2020

@author: Jaqui
"""

from matplotlib import pyplot

estado = ('Durango', 'CDMX', 'Coahuila', 'Suma')

color = ('blue', 'orange','yellow', 'red')

fallecidos = (1223, 2104, 4009, 5000)

pyplot.title('DESESOS POR COVID (ESTADOS)')
pyplot.bar(estado, height=fallecidos, color=color, width=1)

pyplot.show()
