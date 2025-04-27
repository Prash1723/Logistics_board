import numpy as np
from rich.console import Console

rc = Console()

class kpi:
    def __init__(self, l, b, h, n, s, OD, TD):
        self.l = l                                          #Length
        self.b = b                                          #Breadth
        self.h = h                                          #Height
        self.n = n                                          #Number of units
        self.s = s                                          #Space available
        self.OD = OD                                        #Ontime Deliveries
        self.TD = TD                                        #Total Deliveries

    def company(self):
        """Assign company name"""
        name = input("Type your Company name? : ")
        return name

    def cbm(self):
        """Calculate CBM for the items"""
    	cbm = self.l * self.b * self.h
        return cbm

    def otd(self):
        """Calculate Ontime Deliveries"""
        otd = (self.OD/self.TD)*100
        return otd

    def space_left(self):
        """Space left in the godown"""
        space_left = self.s - self.cbm()*self.n
        return space_left

#    def assortment(self):
#        question = input("Are there more than one companies in the list?")
#        if question == "yes"

    def run(self):
        x = dict()
        CBM = self.cbm()
        Space = self.space_left()
        OTD = self.otd()
        question = input("Are there more than one companies in the list?")
        if question == "yes":
            self.company()
        rc.print("Company :", self.company(), style="yellow")
        rc.print("CBM of load: ", CBM, style="green")
        rc.print("Space taken: ", Space, style="red")
        rc.print("OTd %; ", OTD, style="orange")
