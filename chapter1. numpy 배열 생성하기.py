# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 16:09:27 2021

@author: Owner
"""

■ chapter1. numpy 배열 생성하기
numpy 란? python 언어에서 기본적으로 지원하지 않는 배열 (array) 혹은 행렬 (matrix) 이 계산을 쉽게 해주는 라이브러리
-> 머신러닝에서 많이 사용하는 선형대수학에 관련된 수식들을 python 에서 쉽게 프로그래밍 할 수 있게 해줍니다.

문제1. 아래의 행렬을 numpy 로 만드시오!
1 2
3 4

import numpy as np
a = np.array( [[1,2],[3,4]])
print(a)

문제2. 위의 a 행렬의 각 요소에 숫자 5를 더하시오!
import numpy as np
a = np.array( [[1,2],[3,4]])
print(a+5)

문제3. 두 행렬의 합을 구하시오!
import numpy as np
a = np.array( [[1,5],[6,7]])
b = np.array( [[3,4],[2,1]])
print(a+b)

※ numpy 의 유용한 기능 중 하나인 브로드캐스트(broadcast) ?
넘파이에서 형상이 다른 배열끼리도 계산을 할 수 있습니다.
숫자 10개가 2 x 2 행렬로 확대된 후 연산이 이루어지는 것을 브로드캐스트라고 합니다.

문제4. 아래의 브로드캐스트 기능을 numpy 로 구현하시오!
import numpy as np
a = np.array( [[1,2],[3,4]])
b = a*10
print(b)

문제5. 아래의 경우도 브로드캐스트가 되는지 확인하시오!
import  numpy  as  np
a = np.array( [ [1, 2], [3, 4] ] )
b = np.array( [ [10, 20]] )
print (a*b) 


문제6. 아래의 신경망을 numpy 로 구현하시오!
import numpy as np
x=np.array([2,4,8])
w=np.array([4,3,2])
k=np.sum(x*w)
print(k) # 36

문제7. 아래의 신경망을 numpy 행렬로 구현하시오!
import numpy as np
x=np.array([1,2])
w=np.array([[1,3,5],[2,4,6]])
k=np.dot(x,w)
print(k) # [ 5 11 17]

문제8. 아래의 신경망을 numpy 행렬로 구현하시오!
import numpy as np
x = np.array([1,2])
w1 = np.array([[1,3,5],[2,4,6]])
w2 = np.array([[3,4],[5,6],[7,8]])
k = np.dot(x,w1)
m = np.dot(k,w2)
print(m) # [189 222]

문제9. 아래와 같이 5 X 5 행렬을 생성하시오!
x = np.array([ [1,2,3,4,5], [2,4,3,2,4], [3,1,4,2,1], [2,7,3,5,4], [1,5,6,3,1] ] ) 
print (x.shape) 

※ 넘파이 배열(np.array) 은 N차원 배열을 작성할 수 있습니다.
1차원 배열, 2차원 배열, 3차원 배열처럼 원하는 차수의 배열을 만들 수 있습니다.
수학에서는 1차원 배열을 벡터(Vector) 라고 하고 2차원 배열을 행렬(matrix) 라고 부릅니다. 또 벡터와 행렬을 일반화 한 것을 텐서(tensor) 라고 합니다.

tensor(다차원) + flow(흐름) = 행렬이 계산되면서 흘러간다.

구글에서 만든 텐서플로우는 다차원 배열의 연산을 빠르게 할 수 있도록 구현되어 있습니다.
	1. 코드가 간결하다.
	2. 신경망 구현에 필요한 모든 함수들이 다 내장되어 있다.
	3. 속도가 아주 빠르다.
	4. GPU를 사용할 수 있다.

문제10. 행렬의 내적을 구현하시오!
import numpy as np
a=np.array([[3,4,2],[4,1,3]])
b=np.array([[1,5],[2,3],[4,1]])
k=np.dot(a,b)
print(k)


