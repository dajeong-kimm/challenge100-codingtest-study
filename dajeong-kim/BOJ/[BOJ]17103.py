prime = []
check = [0] * 1000001 #0이면 소수, 1이면 합성수
check[0] = 1
check[1] = 1

for i in range(2,1000001):
    if check[i] == 0:
        prime.append(i)
        for j in range(i*2, 1000001, i):
            check[j] = 1
n = int(input())
for _ in range(n):
    num = int(input())
    count = 0
    for i in prime:
        if i >= num:
            break
        else:
            if check[num-i] == 0 and i <= num -i:
                count += 1
    print(count)

