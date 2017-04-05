
import matplotlib.pyplot as plt

from ClassPreProcess import PreProcess

class Plot:



    def HRDiagramPlotter(self, xvalues = 1, yvalues = 1):
        
        instance = PreProcess()

        xvalues = instance.ColumnSelectorForX()
        
        yvalues = instance.ColumnSelectorForY()

        
        plt.gca().invert_yaxis()
        
        plt.scatter(xvalues, yvalues, 0.005)
        
        plt.savefig('/Users/MAC/HRDiagram/HRdiagram.png')