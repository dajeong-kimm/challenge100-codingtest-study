from collections import deque
from sys import stdin
def input():
    return stdin.readline().rstrip()

n = int(input())
number = list(map(int, input().split()))
q = deque(range(1,n+1))
answer = []
answer.append(q.popleft())
dir = number[0]
while q:
    if dir > 0:
        # 시계 방향
        for i in range(dir-1):
            q.append(q.popleft())
        num = q.popleft()
    elif dir < 0:
        dir = abs(dir)
        # 시계 반대 방향
        for i in range(dir-1):
            q.appendleft(q.pop())
        num = q.pop()
    
    answer.append(num)
    dir = number[num-1]
    
for a in answer:
    print(a,end=" ")
    