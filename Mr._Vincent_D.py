N, M = map(int, input().split())

for i in range(N//2):
    print((".|."*(2*i+1)).center(M, '-'))
print("Welcome".center(M, '-'))
for i in range(N//2):
    print((".|."*((N-1)-(i*2+1))).center(M, '-'))
    # print(((N-1)-(i*2+1)))
