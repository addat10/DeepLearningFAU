import numpy as np
import matplotlib.pyplot as plt
class Checker():
    """Class for the Checker"""
    def __init__(self,resolution,tile_size):
        self.res=resolution         # No of pixels in both directions
        self.ts=tile_size           # No of pixels in a tile
        self.output=np.zeros((self.res,self.res))  # Initialize output
        print("Creating an object instance of Checker")
    def draw(self):
        vec_count=np.linspace(0,self.res-1,self.res)  # Create a vector [1,2,...,res]
        idx=((np.remainder(vec_count,(2*self.ts))>=(self.ts))) # Find indices in the white region in one direction
        IDX=idx*np.ones((self.res,1))   # Vertical patches
        IDY=np.transpose(IDX)           # Horizontal patches
        ID=np.logical_xor(IDX,IDY)      # XOR the two patches
        #self.output[IDX.astype(bool)]=1  # For looking at the vertical patches indices
        #self.output[IDY.astype(bool)]=1  # For looking at the horizontal patches indices
        self.output[ID.astype(bool)] = 1  # The correct output. Set the value at correct indices to 1
        output = self.output.copy()
        return output
    def show(self):
        plt.imshow(self.output,cmap = 'gray')
        plt.show()  # To hold the image

class Circle():
    """Class for the Checker"""
    def __init__(self,resolution,radius,center):
        self.res=resolution         # No of pixels in both directions
        self.rad=radius             # Radius of the Circle
        self.cen=np.array(center)   # center of the circle
        self.output = np.zeros((self.res, self.res))  # Initialize output
        print("Creating an object instance of Circle")
    def draw(self):
        print("Circle needs to be drawn")
        start_id=self.cen-self.rad
        end_id=self.cen+self.rad
        self.output[start_id[0]:end_id[0]+1,start_id[1]:end_id[1]+1]=self.draw_inscribed_circle()
        output=self.output.copy()
        return output
    def show(self):
        plt.imshow(self.output,cmap = 'gray')
        plt.show()  # To hold the image
    def draw_inscribed_circle(self):
        n=self.rad*2+1;
        cen=self.rad+1
        M = np.ones((n, n))
        x=np.arange(1,n+1)
        x_min_cen_squared=np.square((x-cen))
        Z=np.reshape(x_min_cen_squared,(n,1))+np.reshape(x_min_cen_squared,(1,n))
        M[Z>=np.square(self.rad)]=0
        return M

class Spectrum():
    def __init__(self,resolution):
        self.res=resolution
        self.output=np.zeros([self.res,self.res,3])
        print("Created an instance of the class Spectrum")
    def draw(self):
        print("Need to draw the spectrum")

        '''
        # The following code uses exponentially decaying fields        
        r_cen=np.array([0,self.res])
        g_cen = np.array([self.res, self.res/2])
        b_cen = np.array([0, 0])
        vec=np.reshape(np.arange(0,self.res),[self.res,1])
        sigma_r=0.000002;
        sigma_g = 0.000009;
        sigma_b = 0.000002;
        Z1=np.square(vec-r_cen[0])+np.transpose(np.square(vec-r_cen[1]))
        exp_Z1=np.exp(-sigma_r*Z1)

        Z2 = np.square(vec - g_cen[0]) + np.transpose(np.square(vec - g_cen[1]))
        exp_Z2 = np.exp(-sigma_g * Z2)

        Z3 = np.square(vec - b_cen[0]) + np.transpose(np.square(vec - b_cen[1]))
        exp_Z3 = np.exp(-sigma_b * Z3)
        self.output[:, :, 0] = exp_Z1
        self.output[:, :, 1] = exp_Z2
        self.output[:,:,2]=exp_Z3
        '''

        # The following code uses linearly decaying fields
        vec=np.reshape(np.linspace(0,1,self.res),[self.res,1])
        Z2 = vec * np.ones([1,self.res])
        print(Z2)

        Z1=np.ones([self.res,1])*np.transpose(vec)

        vec_rev=np.reshape(np.linspace(1,0,self.res),[self.res,1])
        Z3=np.ones([self.res,1])*np.transpose(vec_rev)

        self.output[:, :, 0] = Z1
        self.output[:, :, 1] = Z2
        self.output[:,:,2]=Z3
        output = self.output.copy()
        return output
    def show(self):
        print("Need to show the spectrum")
        plt.imshow(self.output)
        plt.show()  # To hold the image
