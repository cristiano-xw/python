import matplotlib.pyplot as plt #调用库
from skimage import data,draw,color,transform,feature #引用函数库
from skimage import io  
image_rgb=io.imread("D://opencv//test//s1.png")#提取出图像
#plt.imshow(image_rgb)
#image_rgb=color.rgba2rgb(image_rgb) #转换格式    
image_gray = color.rgb2gray(image_rgb)
edges = feature.canny(image_gray, sigma=1.0, low_threshold=0.15, high_threshold=0.25)
#执行椭圆变换  
#plt.imshow(edges)
edges=edges[200:400,0:200] 
plt.imshow(edges)  
#print(edges) 
result =transform.hough_ellipse(edges) 
result.sort(order='accumulator') #根据累加器排序

#print(result) 
#估计椭圆参数
best = list(result)  #排完序后取最后一个
print(best) 
yc, xc, a, b = [int(round(x)) for x in best[1:5]]
orientation = best

#在原图上画出椭圆
cy, cx =draw.ellipse_perimeter(yc, xc, a, b, orientation)
image_rgb[cy, cx] = (0, 0, 255) #在原图中用蓝色表示检测出的椭圆

# #分别用白色表示canny边缘，用红色表示检测出的椭圆，进行对比
edges = color.gray2rgb(edges)
edges[cy, cx] = (250, 0, 0) 

fig2, (ax1, ax2) = plt.subplots(ncols=2, nrows=1, figsize=(8, 4))

ax1.set_title('Original picture')
ax1.imshow(image_rgb)

ax2.set_title('Detect result')
ax2.imshow(edges)

plt.show()
