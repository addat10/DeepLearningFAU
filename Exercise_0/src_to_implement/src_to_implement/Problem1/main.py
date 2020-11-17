from pattern import Checker
from pattern import Circle
from pattern import Spectrum
import numpy as np
import matplotlib.pyplot as plt

'''
Checker1=Checker(300,12)
Checker_out=Checker1.draw()
Checker1.show()
'''


Circle1=Circle(1024,200,(512,256))
Circle_out=Circle1.draw()
plt.imshow(Circle_out,cmap = 'gray')
plt.show()  # To hold the image
#Circle1.show()


'''
Spectrum1=Spectrum(1000)
Spectrum_out=Spectrum1.draw()
Spectrum1.show()
'''