A = int(input())
B = int(input())
N = int(input())
kops = B * N
finKops = kops % 100
rubs = A * N + kops // 100
print(rubs, finKops)
