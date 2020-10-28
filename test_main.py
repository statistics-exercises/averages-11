import scipy.stats as st
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_xplot(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_x)==200, "your graph has the wrong number of coordinates" )
        for i in range( len(this_x) ) :
             self.assertTrue( np.abs(i + 1 - this_x[i])<1e-7, "the x-coordinates of the graph have not been set correctly" )
             
    def test_plot(self):
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        counts = 5*[0]
        for i in range(1,len(this_y)) : 
            last_var = math.log( (i+1)*this_y[i] - i*this_y[i-1], 2 )  
            if last_var< 6 : counts[ int(last_var) - 1  ] = counts[ int(last_var) - 1  ] + 1
        for i in range(5) : 
            prob = 0.5**(i+1)
            mean = (len(this_y)-1)*prob
            var = mean*(1-prob)
            bar = np.sqrt(var)*st.norm.ppf( (0.99 + 1) / 2 )
            self.assertTrue( np.fabs( counts[i] - mean )<bar, "you don't seem to be calculating the y-coordinates correctly" )
