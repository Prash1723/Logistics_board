import numpy as np
from rich.console import Console

rc = Console()

class kpi:
    def __init__(self, l, b, h, n, s):
        self.l = l                                          #Length
        self.b = b                                          #Breadth
        self.h = h                                          #Height
        self.n = n                                          #Number of units
        self.s = s                                          #Space available

    def company(self):
        """Assign company name"""
        name = input("Type your Company name? : ")
        return name

    def cbm(self):
        """Calculate CBM for the items"""
    	return self.l*self.b*self.h

    def space_left(self):
        """Space left in the godown"""
        return self.s - self.cbm()*self.n

    def assortment(self):
        question = input("Are there more than one companies in the list?")
        if question == "yes"

    def run(self):
        x = dict()
        CBM = self.cbm()
        Space = self.space_left()
        question = input("Are there more than one companies in the list?")
        if question == "yes":
            self.company()
        rc.print("Company :", self.company(), style="yellow")
        rc.print("CBM of load: ", CBM, style="green")
        rc.print("Space taken: ", Space, style="red")
