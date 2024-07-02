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

    def cbm(self):
    	return self.l*self.b*self.h

    def space_left(self):
        return self.s - self.cbm()*self.n
    
    def run(self):
        CBM = self.cbm()
        Space = self.space_left()
        rc.print("CBM of load: ", CBM, style="green")
        rc.print("Space taken: ", Space, style="red")
