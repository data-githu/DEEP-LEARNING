# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 16:10:51 2021

@author: Owner
"""

■ chapter1. Matplotlib 로 그래프 그리기

딥러닝 실험에서는 그래프 그리기와 데이터 시각화가 중요합니다.
matplotlib  그래프를 그리기 위한 라이브러리 입니다. 
matplotlib 를 이용하면 그래프 그리리가 쉬워집니다.

신경망에서 주로 사용하는 그래프는 라인 그래프입니다.
정확도가 점점 올라가는지 아니면 오차가 점점 떨어지는지 확인할 때 유용합니다.


예제1. 파이썬으로 산포도 그래프 그리는 방법
import numpy as np
import matplotlib.pyplot as plt

x = np.array( [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ] )
y = np.array( [ 9, 8, 7, 9, 8, 3, 2, 4, 3, 4 ] )

plt.scatter(x,y,color='red', s=80) # s는 점사이즈
plt.show()



문제15. 위의 그래프를 라인 그래프로 그리시오!
import numpy as np
import matplotlib.pyplot as plt

x = np.array( [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ] )
y = np.array( [ 9, 8, 7, 9, 8, 3, 2, 4, 3, 4 ] )

plt.plot(x,y,color='red') # s는 점사이즈
plt.show()



문제16. 위의 그래프에 제목을 "신경망 오차 그래프" 라고 하시오!
import  numpy   as  np
import  matplotlib.pyplot  as  plt
from matplotlib import font_manager, rc

font_path = "c:\\data\\malgun.ttf" 
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

x = np.array( [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ] )
y = np.array( [ 9, 8, 7, 9, 8, 3, 2, 4, 3, 4 ] )

plt.plot( x, y, color='red' ) 
plt.title("신경망 오차 그래프") 
plt.show()
