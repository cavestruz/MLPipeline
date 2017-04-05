#This is matplotlib which is like Matlab but in python form
import matplotlib.pyplot as plt
#This is the python way of inheritance in object oriented program *sigh*.
from ClassPreProcess import PreProcess

#This class makes magnificient scatterplots
class Plot:

#This is the best function for making an H-R Diagram that I've ever made.   
    def HRDiagramPlotter(self, xvalues = 1, yvalues = 1):
#By far the most annoying thing in python is the requirement of making
#instances of classes because poor little python gets confused on what 
#class I'm talking about as if typing the name of it wasn't clear enough.        
        instance = PreProcess()
#Assigns xvalues, which absolutely will not work without declaring a
#"global" variable, I just... I don't know what to say. Of course it's 
#global, I'm calling function from another class...
        xvalues = instance.ColumnSelectorForX()
#Same thing as the function above but for the yvalues.
        yvalues = instance.ColumnSelectorForY()

#This inverts the y-axis so the big boy supergiants can be on the top of the
#graph and the little white dwarfs can be on the bottom.      
        plt.gca().invert_yaxis()
#This actually does the hard labor of plotting the points. I thought I'd 
#never be able to give it the chance to do its job, but I persisted.      
        plt.scatter(xvalues, yvalues, 0.005)
#This is the function that saves the scatter plot to a file.
        plt.savefig('/Users/MAC/HRDiagram/HRdiagram.png')
        
#I know you wanted to see some machine learning stuff with skylearn. Every
#problem I ran into with python took from 1.5 to 8 hours to figure out how
#to do it right. Things should go more smoothly in the future, and I'll get
#more stuff done, and get into the machine learning algorithms, and not write
#run-on sentences.

#Why didn't the koala get the job?

#Because he didn't have the koalifications.