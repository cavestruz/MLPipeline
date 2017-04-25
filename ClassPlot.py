
import matplotlib.pyplot as plt

from ClassPreProcess import PreProcess



class Plot():

   
    def HRDiagramPlotter(self):
     
        P = PreProcess()

        xvaluesT = P.ColumnSelectorForX

        yvaluesT = P.ColumnSelectorForY()
 
        plt.gca().invert_yaxis()
   
        plt.scatter(xvaluesT, yvaluesT, 0.005)

        plt.savefig('/Users/MAC/HRDiagram/HRdiagram.png')
