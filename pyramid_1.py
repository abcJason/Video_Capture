
import cv2
import numpy as np
O=cv2.imread("lena.bmp")
G0=O
G1=cv2.pyrDown(G0)
L0=O-cv2.pyrUp(G1)
RO=L0+cv2.pyrUp(G1)  #通過拉普拉斯圖像復原的原始圖像
print("O.shape=",O.shape)
print("RO.shape=",RO.shape)
result=RO-O  #將o和ro做減法
#計算result的絕對值，避免求和時負負為正3+(-3)=0
result=abs(result)
#计算result所有元素的和
print("原始圖像O與恢復圖像RO差值的絕對值和：",np.sum(result))