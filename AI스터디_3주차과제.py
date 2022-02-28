import numpy as np

arr1 = np.random.rand(5, 3) #5x3의 무작위 행렬 생성
arr2 = np.random.rand(3, 2) #3x2의 무작위 행렬 생성

dot = arr1.dot(arr2) #내적 연산 실행
print(dot, dot.shape) #결과값 출력
