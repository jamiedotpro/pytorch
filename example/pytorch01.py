from __future__ import print_function
import torch

# 초기화되지 않은 5*3 행렬 생성
x = torch.Tensor(5, 3)
print(x)

# 무작위로 초기화된 행렬 생성
x = torch.rand(5, 3)
print(x)

# 행렬의 크기 구하기
print(x.size())