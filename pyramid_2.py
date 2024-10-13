import cv2
import numpy as np
O=cv2.imread("lena.bmp")
#=================生成高斯金字塔======================
G0=O
G1=cv2.pyrDown(G0)
G2=cv2.pyrDown(G1)
G3=cv2.pyrDown(G2)
#===============生成拉普拉斯金字塔====================
L0=G0-cv2.pyrUp(G1) #拉普拉斯金字塔第0層
L1=G1-cv2.pyrUp(G2) #拉普拉斯金字塔第1層
L2=G2-cv2.pyrUp(G3) #拉普拉斯金字塔第2層
#=================復原G0======================
RG0=L0+cv2.pyrUp(G1)  #通過拉普拉斯圖像復原的原始圖像G0
print("G0.shape=",G0.shape)
print("RG0.shape=",RG0.shape)
result=RG0-G0  #將RG0和G0做減法
#計算result的絕對值，避免求和時負負為正3+(-3)=0
result=abs(result)
#計算result所有元素的和
print("原始圖像G0與恢復圖像RG0差值的絕對值和：",np.sum(result))
cv2.imshow("RG0",RG0)
#=================復原G1======================
RG1=L1+cv2.pyrUp(G2) #通過拉普拉斯圖像復原G1
print("G1.shape=",G1.shape)
print("RG1.shape=",RG1.shape)
result=RG1-G1  #將RG1和G1做減法
print("原始圖像G1與恢復圖像RG1差值的絕對值和：",np.sum(abs(result)))
cv2.imshow("RG1",RG1)
#=================復原G2======================
RG2=L2+cv2.pyrUp(G3) #通過拉普拉斯圖像復原G2
print("G2.shape=",G2.shape)
print("RG2.shape=",RG2.shape)
result=RG2-G2  #將RG2和G1做減法
print("原始圖像G2與恢復圖像RG2差值的絕對值和：",np.sum(abs(result)))
cv2.imshow("RG2",RG2)
#=======================================================
cv2.waitKey()
cv2.destroyAllWindows()

