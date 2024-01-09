print("""Modul wurde geladen...""")
print("""Version final_final_05""")

# # Klassen / Objekte aus der Veranstaltung WissDV 2023/2024
# # Schöne Feiertage und einen guten Rutsch!

import this
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


class CoffeeMachine(object):
# #     name = None
#     beans = 0
#     water = 0
 
    def __init__(self, name, beans, water):
        self.name = name
        self.beans = beans
        self.water = water
 
    def addBean(self):
        self.beans = self.beans + 1
 
    def removeBean(self):
        self.beans = self.beans - 1
 
    def addWater(self):
        self.water = self.water + 1
 
    def removeWater(self):
        self.water = self.water - 1
 
    def printState(self):
        print("Name  = " + self.name)
        print("Beans = " + str(self.beans))
        print("Water = " + str(self.water))

    def make_coffee(self, number=1):
        self.water -= 4 * number
        self.beans -= 3 * number

    def refill_machine(self):
        self.water += 10
        self.beans += 10

    
        