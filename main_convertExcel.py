from PIL import Image, ImageDraw, ImageFilter
import cv2
import numpy as np
import pandas as pd

# step1：将xlsx表格的文件的"RGB空格"数据转换为R->255,G->255,B->255，空格->0
# 转换方法：您可以使用Excel的查找与替换功能来填充空白单元格。
# 首先，选中要填充的数据区域，然后按Ctrl+G或者F5调出定位对话框，点击左下角的【定位条件】。
# 在【定位条件】中选择【空值】，然后点击【确定】按钮。按照上述操作完毕后，所有的空白单元格就都被选中了。
# 接下来，输入您想要填充的内容，然后按下Ctrl+Enter即可将所有选中的空白单元格填充为您输入的内容

# step2：将xlsx表格中的数值读取出来生成一个矩阵，然后生成一个图像
data = pd.read_excel('rgb_mask.xlsx') # 读取名为“file.xlsx”的Excel文件并将其转换为矩阵
matrix = data.values
img = Image.fromarray(matrix.astype('uint8'), 'L')
img.save('01_mask_excel.png')

# step3:使用opencv对图像进行水平方向缩小到原来的一半，竖直方向不变
# 这里也可以使用以下代码将彩色图像转换为灰度图像： gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
opencv_mask = cv2.imread('01_mask_excel.png', cv2.IMREAD_GRAYSCALE)
resized_image = cv2.resize(opencv_mask, (int(opencv_mask.shape[1]/2), opencv_mask.shape[0])) # 对图像进行水平缩放
ret, binary = cv2.threshold(resized_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # 灰度图转为二进制图
cv2.imwrite('01_mask_output.png', binary)