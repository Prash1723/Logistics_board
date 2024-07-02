import numpy as np
from rich.console import Console

rc = Console()

class kpi:
    def __init__(self, l, b, h, n, s):
        self.l = l
        self.b = b
        self.h = h
        self.n = n
        self.s = s

    def company(self):
        name = input("Type your Company name? : ")
        return name

    def cbm(self):
    	return self.l*self.b*self.h

    def space_left(self):
        return self.s - self.cbm()*self.n
    
    def run(self):
        CBM = self.cbm()
        Space = self.space_left()
        rc.print("Company :", self.company(), style="yellow")
        rc.print("CBM of load: ", CBM, style="green")
        rc.print("Space taken: ", Space, style="red")
