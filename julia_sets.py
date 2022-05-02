# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 16:01:20 2020

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
#Creating Julia Set Function
#Decide the image width and height
plotwidth, plotheight = 400, 400
#Set the maximum absolute value of the complex number and number of iterations so
#that it stays bounded
zabs_max = 2
nit_max = 400
#We want the reals to be plotted between -2 and 2 so we set the x values
xmin, xmax = -2, 2
xwidth = xmax - xmin
#We want the imaginary numbers to be plotted between -1 and 1 so we set the y values
ymin, ymax = -1, 1
yheight = ymax - ymin
#Now to define our function to produce Julia sets. I put in power as variable instead
#of 2 as I will investigate Julia sets of other forms later
def juliaset(c,power):
    #To create the plot we start with a matrix of zeros
    julia = np.zeros((plotwidth, plotheight))
    for x in range(plotwidth):
        for y in range(plotheight):
            nit = 0
            #Set the real and imaginary coponents scaling them to a 1x1 pixel  
            a = x / plotwidth * xwidth + xmin
            b = (y / plotheight * yheight + ymin)*2
            #Map the pixel position to a point in the complex plane
            z = complex(a,b)
            #Create a while loop to make sure z is bounded
            while abs(z) <= zabs_max and nit < nit_max:
                z = z**power + c
                nit += 1
           
            #By setting each entry in the matrix to the ratio we can see where
            #there are more iterations and where the iterations have reached 
            #the max (i.e. on the bound)
            ratio = nit / nit_max
            julia[x,y] = ratio
    
    #transpose the matrix so graph is the correct way round            
    julia=julia.transpose()
    #this counts the number of entries in the matrix that are here the iterations 
    #have reached the max (i.e. on the bound)
    Ne=np.count_nonzero(julia == 1)
    return(julia,Ne)

#plot the julia set with c=-1
fig, ax = plt.subplots() 
plt.suptitle('Figure 1') 
plt.imshow(juliaset(complex(-1, 0),2)[0], interpolation='nearest', cmap=cm.inferno, origin='lower')
plt.show()

#Box Counting Dimension
#I have decided to take each pixel (entry in the matrix) as my epsilon hence epsilon=1/400 
#N(epsilon) is the number of n-dimesional boxes of size epsilon that cover where the entry
#in the matrix reches the max number of iterations (on the bound). Hence the Ne in the
#juliaset definition is N(epsilon)  
def boxcounting(c):    
    a=juliaset(c,2)[1]
    if a == 0:
        return('error')
    else:
        return(np.log(a)/np.log(400))

print('Box counting dimension of Julia set with c=-1')
print(boxcounting(complex(-1, 0)))

#Investigating Symmetries and Dust (with box counting dimensions)
#Use juliaset fuction to create plots of julia sets with different c values
fig, ax = plt.subplots(2,2)
plt.suptitle('Figure 2')
ax[0,0].set_title("Figure 2A")  
ax[0,0].imshow(juliaset(complex(0, 0.5),2)[0], interpolation='nearest', cmap=cm.inferno, origin='lower')
plt.show()

ax[0,1].set_title("Figure 2B")
ax[0,1].imshow(juliaset(complex(-0.1,0.65),2)[0], interpolation='nearest', cmap=cm.inferno, origin='lower')
plt.show()

ax[1,0].set_title("Figure 2C")  
ax[1,0].imshow(juliaset(complex(0.285, 0),2)[0], interpolation='nearest', cmap=cm.inferno, origin='lower')
plt.show()

ax[1,1].set_title("Figure 2D")
ax[1,1].imshow(juliaset(complex(-0.481, 0),2)[0], interpolation='nearest', cmap=cm.inferno, origin='lower')
plt.show()

#We can see that Figure 2C and 2D are reflectionally symmetrical suggesting that
#Julia sets with where c is an element of the reals (i.e. in the form c = a+0i) 
#are reflection symmetric.
#We can see that Figure 2A and 2B are not reflection symmetric but have 
#rotational symmetry suggesting Julia sets with complex c are not reflection 
#symmetric but have rotational symmetry.
#Furthermore, Figure 2B and 2C are disconnected. Disconnected sets are completely 
#disconnected into a countably infinite group of isolated points (these can be
#from the light yellow regions on the plots). These points are arranged in 
#dense groups and any finite disk surrounding a point contains at least one 
#other point in the set (this can be seen from the more purple regions in the plot).
#These regions resemble dust so disconnected sets are often called Fatou sets.
#with the dust called Fatou dust 

print('Box counting dimensions for plots in Figure 2')
print('Figure 2A')
print(boxcounting(complex(0, 0.5)))
print('Figure 2B')
print(boxcounting(complex(-0.1, 0.65)))
print('Figure 2C')
print(boxcounting(complex(0.285, 0)))
print('Figure 2D')
print(boxcounting(complex(-0.481, 0)))

#The box counting dimension for Figure 2C returns error, this is because N(e)=0
#so there are no points that take the maximum number of iterations this can be seen
#from the plot as there are no light yellow regions

#Investigating Types of Cycle
#By looking at the iteration of z_n+1 = (z_n)^2 + c we can find the cycle of Julia set
#if it exists. So the function below produces a list of the absolute value of the output
#of each iteration
def cycle(c):
    mylist=[]
    m=c
    for i in range(16):
        x=m
        m=x**2+c
        mylist.append(abs(m))
    return(mylist)

fig, ax = plt.subplots(2,3)
plt.suptitle('Figure 3')
ax[0,0].set_title("Figure 3A")  
ax[0,0].imshow(juliaset(complex(-1.037,0.17),2)[0], interpolation='nearest', cmap=cm.inferno, origin='lower')
plt.show()
ax[1,0].set_title('Figure 3A Cycle')
ax[1,0].plot(np.arange(0,16),cycle(complex(-1.037,0.17)),'-co')
plt.show()

ax[0,1].set_title("Figure 3B")
ax[0,1].imshow(juliaset(complex(0.295,0.55),2)[0], interpolation='nearest', cmap=cm.inferno, origin='lower')
plt.show()
ax[1,1].set_title('Figure 3B Cycle')
ax[1,1].plot(np.arange(0,16),cycle(complex(0.295,0.55)),'-co')
plt.show()
 
ax[0,2].set_title("Figure 3C")
ax[0,2].imshow(juliaset(complex(-0.52,0.57),2)[0], interpolation='nearest', cmap=cm.inferno, origin='lower')
plt.show()
ax[1,2].set_title('Figure 3C Cycle')
ax[1,2].plot(np.arange(0,16),cycle(complex(-0.52,0.57)),'-co')
plt.show()

#From Figure 3 we can see there's a realtionship between the cycle and shape of the 
#Julia sets. Figure 3A has a 2-cycle and we can see that the image being repeated 
#in the Julia set has 2 sections this suggests the type of cycle it has corresponds
#to number of sections in the image being repeated in the Julia set. 
#This can seen more clearly in Figure 3B (4-cycle with 4 sections) and 
#3C (5-cycle with 5 sections) and their corresponding cycle plots. 

#Investigating Different Powers of z
fig, ax = plt.subplots(2,2)
plt.suptitle('Figure 4')
ax[0,0].set_title("Figure 4A")  
ax[0,0].imshow(juliaset(0.4,3)[0], interpolation='nearest', cmap=cm.inferno, origin='lower')
plt.show()

ax[0,1].set_title("Figure 4B")  
ax[0,1].imshow(juliaset(0.484,4)[0], interpolation='nearest', cmap=cm.inferno, origin='lower')
plt.show()

ax[1,0].set_title("Figure 4C")  
ax[1,0].imshow(juliaset(0.544,5)[0], interpolation='nearest', cmap=cm.inferno, origin='lower')
plt.show()

ax[1,1].set_title("Figure 4D")  
ax[1,1].imshow(juliaset(0.59,6)[0], interpolation='nearest', cmap=cm.inferno, origin='lower')
plt.show()

#From Figure 4 we can see that rotational symmetry of each shape corresponds to the power 
#of z that we use. So from previous Figures we see that Julia Set images of form z^2 + c all 
#repeat if we rotate them through exactly 180 degrees (rotational symmetry of 2). 
#In Figure 4 for z^3 + c  we can see the shapes self-map three times within a 360 degree 
#rotation (rotational symmetry of 3), for z4 the shapes self-map four times, and so on.

#Investigating How the Maximum Number of Iterations Affects the Julia Set Plot
nit_max=10
fig, ax = plt.subplots(2,2)
plt.suptitle('Figure 5')
ax[0,0].set_title("Figure 5A")  
ax[0,0].imshow(juliaset(complex(-0.78,0.3),2)[0], interpolation='nearest', cmap=cm.inferno, origin='lower')
plt.show()

nit_max=20
ax[0,1].set_title("Figure 5B")  
ax[0,1].imshow(juliaset(complex(-0.78,0.3),2)[0], interpolation='nearest', cmap=cm.inferno, origin='lower')
plt.show()

nit_max=50
ax[1,0].set_title("Figure 5C")  
ax[1,0].imshow(juliaset(complex(-0.78,0.3),2)[0], interpolation='nearest', cmap=cm.inferno, origin='lower')
plt.show()

nit_max=100
ax[1,1].set_title("Figure 5D")  
ax[1,1].imshow(juliaset(complex(-0.78,0.3),2)[0], interpolation='nearest', cmap=cm.inferno, origin='lower')
plt.show()

#From Figure 5 we can we see that the detail, and shapes can be modified by changing 
#the maximum number of iterations. As we increase the max number of iterations 
#it becomes nore detailed with some areas of the image shrinking and rotating slightly 
#to make spiral. We can also see that the 'dust' decreases too.
#Also the change in the plots from Figure 5A to Figure 5B are more significant than
#the plots from Figure 5C to 5D. So increasing the max iterations from 10 to 20 
#makes more of a difference than increasing it from 50 to 100. This is because
#at 50 iterations it's getting close to the true image so increasing the maximum
#iterations by more doesn't make as much of a difference. 

#set max iterations back to original 400
nit_max=400

#Plotting the Mandelbrot
#The Mandelbrot is the set of all values of c for which the corresponding Julia 
#sets are connected
#Again using the same image width and height as previously, create a matrix of zeros
M = np.zeros((plotwidth, plotheight))
#We want the reals to be plotted between -2 and 2 so we set the x values and 
#the imaginary component to be plotted between -1 and 1 so we set the y values
#we do this using the linspace function which returns number spaced evenly
#with respect to the interval.
xvalues = np.linspace(-2,2,plotwidth)
yvalues = np.linspace(-1,1,plotheight)
#the enumerate function adds a counter to an iterable
#the for loop binds u to the counter and x to xvalues. Same applies for v,y
#so we use u,v for the entry of the matrix M, and x,y for the c value
for u,x in enumerate(xvalues):
    for v,y in enumerate(yvalues):
        #The mandelbrot records the fate of the orbit of 0 for all possible c values
        #so we start with z=0
        z = 0 + 0j
        #Set the real and imaginary coponents scaling them to a 1x1 pixel
        c = complex(x,2*y)
        n=0
        #the while loop ensures the number of iterations is bounded
        while n<150:
            z = z**2 + c
            #We choose 2 to bound the absolute value of z as the Mandelbrot 
            #set lies within distance 2 of the origin. 
            #If it is not bounded the entry in the matrix stays zero and breaks
            #the while loop, when bounded it changes it to 1
            if abs(z) > 2.0:
                M[u,v]=0
                break
            else:
                M[u,v]=1
            n+=1
                
#transpose the matrix so graph is the correct way round                  
M=M.transpose()
#Plot
fig, ax = plt.subplots()
plt.suptitle('Figure 6')
ax.imshow(M,origin='lower', interpolation='nearest', cmap=cm.inferno)
plt.show()







