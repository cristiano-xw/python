import matplotlib.pyplot as plt
import cv2
from skimage import data, color, img_as_ubyte,feature,transform 
from skimage.feature import canny
from skimage.transform import hough_ellipse 
from skimage.draw import ellipse_perimeter
from skimage import io


image_rgb=io.imread("D://opencv//test//s1.png")  
image_rgb=image_rgb[200:400,0:250] 
image_gray = color.rgb2gray(image_rgb)  
edges = feature.canny(image_gray, sigma=1.0,
              low_threshold=0.1, high_threshold=0.15) 

plt.imshow(edges)


# Perform a Hough Transform
# The accuracy corresponds to the bin size of a major axis.
# The value is chosen in order to get a single high accumulator.
# The threshold eliminates low accumulators 
#result = transform.hough_ellipse(edges)    
#result.sort(order='accumulator')
#n=len(result) 
#print(n) 
#print(result) 
# Estimated parameters for the ellipse
#best = list(result[-1])  
#yc, xc, a, b = [int(round(x)) for x in best[1:5]]
#orientation = best[5]

# Draw the ellipse on the original image
#cy, cx = ellipse_perimeter(yc, xc, a, b, orientation)
#image_rgb[cy, cx] = (0, 0, 255)
# Draw the edge (white) and the resulting ellipse (red)
#edges = color.gray2rgb(img_as_ubyte(edges))
#edges[cy, cx] = (250, 0, 0)

#fig2, (ax1, ax2) = plt.subplots(ncols=2, nrows=1, figsize=(8, 4),
#                               sharex=True, sharey=True)

#ax1.set_title('Original picture')    
#ax1.imshow(image_rgb) 

#ax2.set_title('Edge (white) and result (red)')
#ax2.imshow(edges)

plt.show()



