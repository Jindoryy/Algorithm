# 1번 문제

def solution(X, Y, D):
    
    distance = Y - X # X와 Y의 거리 차이
    cnt = distance // D # 점프한 횟수
    tmp = distance % D # 점프 후 남은 거리

    return cnt if tmp == 0 else cnt+1

# 2번 문제

def solution(A):
    
    chk = [0] * (len(A)+2)
    chk[0] = 1

    for i in A:
        chk[i] = 1

    return chk.index(0)
  
# 3번 문제 (시간초과 O(N*N))

def solution(A):
    
    ans = []

    for P in range(1, len(A)):
        num = abs(sum(A[:P]) - sum(A[P:]))
        
        ans.append(num)

    return min(ans)
  
# 3번 문제 (투 포인터를 이용해서 시간 초과 해결 O(N))
  
def solution(A):

    ptr = 0
    sum1, sum2 = 0, sum(A)
    ans = []

    for _ in range(len(A)-1):

        sum1 += A[ptr]
        sum2 -= A[ptr]

        num = abs(sum1 - sum2)
        ans.append(num) # O(1)
        
        ptr += 1

    return min(ans) 
