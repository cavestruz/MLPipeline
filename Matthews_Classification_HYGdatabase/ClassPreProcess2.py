#this library has all the functions for handling .csv files
import pandas

#I spent 8 hours straight trying to learn how to code object oriented 
#programing in python using pass by value, which doesn't exist in python 
#apparently, finally typed in these two global variables and everything ran 
#perfectly.
global xvalues
global yvalues

#This class will be expanded in the future to include all the functions for
#pre processing data.
class PreProcess:

#This function gives all x values for the scatterplot.
    def ColumnSelectorForX(self):
#This reads from a data of a combination of 3 datasets, not the one I 
#originally chose, because the Kepler eggheads figured all the planets  
#worth finding are in a narrow set of spectral classes, which is not useful  
#for making an H-R Diagram. So I got the dataset from here:
#http://www.astronexus.com/hyg
#I know there is a way to get the thing to read directly from an online source
#I'll get right on that for next week's assignment, because it's 4:16 AM.
        PreProcessed = pandas.read_csv('/Users/MAC/HRDiagram/hygdata_v3.csv')
#ci is "Color Index", which as an acronym should be capitalized. An it's not
#really a color index, it's blue minus visual, which is "B-V" in every other
#source.
        xcolumn = ['ci']
#This is a funky operation that takes the column set above and puts into
#a "list" which is a wierd way of saying "string array".
        xvalues = PreProcessed[xcolumn]
 #The only coding statement that makes complete sense so far in python.       
        return xvalues
#Everything for this function is like the above function, but for the y values
#the "absmag" is the "Absolute Magnitude" which is pretty important, unless
#you're a kepler or galex egghead, then who cares how bright it is, right?     
    def ColumnSelectorForY(self):

        PreProcessed = pandas.read_csv('/Users/MAC/HRDiagram/hygdata_v3.csv')
        
        ycolumn = ['absmag']
        
        yvalues = PreProcessed[ycolumn]
        
        return yvalues


        
        






