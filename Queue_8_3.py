# 숫자를 입력받는다. 
# 입력받은 숫자가 n이면, 1~n차례대로 push한다. 
# 첫번째는 get rid of 하고, 두번째는 제일 밑으로 보낸다. 이과정을 숫자가 1개남을때까지 반복한다.
# 1개가 남으면, 그 숫자를 출력한다.
import sys 
from collections import deque 
input = int(sys.stdin.readline())
queue = deque([i for i in range(1, input+1)])

while len(queue) > 1:
    queue.popleft()
    first = queue[0]
    queue.popleft()
    queue.append(first)
print(queue[0])
